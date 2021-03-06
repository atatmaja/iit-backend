from flask_restplus import Resource, Namespace
from flask import jsonify, make_response, request

from .data_provider_service import get_record_details, get_country_seroprev_summaries
from .data_provider_schema import RecordDetailsSchema, RecordsSchema, StudyCountSchema
from app.utils import validate_request_input_against_schema, get_filtered_records,\
    get_paginated_records, convert_start_end_dates

data_provider_ns = Namespace('data_provider', description='Endpoints for getting database records.')


@data_provider_ns.route('/records', methods=['GET', 'POST'])
class Records(Resource):
    @data_provider_ns.doc('An endpoint for getting all records from database with or without filters.')
    def get(self):
        # Parse pagination request args if they are present
        sorting_key = request.args.get('sorting_key', None, type=str)
        reverse = request.args.get('reverse', None, type=bool)
        page_index = request.args.get('page_index', None, type=int)
        per_page = request.args.get('per_page', None, type=int)

        result = get_filtered_records(filters=None, columns=None, start_date=None, end_date=None)

        # Only paginate if all the pagination parameters have been specified
        if page_index is not None and per_page is not None and sorting_key is not None and reverse is not None:
            result = get_paginated_records(result, sorting_key, page_index, per_page, reverse)
        return jsonify(result)

    def post(self):
        # Convert input payload to json and throw error if it doesn't exist
        data = request.get_json()
        if not data:
            return {"message": "No input payload provided"}, 400
        # All of these params can be empty, in which case, our utility functions will just return all records
        filters = data.get('filters')

        # Validate input payload
        payload, status_code = validate_request_input_against_schema(data, RecordsSchema())
        if status_code != 200:
            # If there was an error with the input payload, return the error and 422 response
            return make_response(payload, status_code)

        sorting_key = data.get('sorting_key')
        page_index = data.get('page_index')
        per_page = data.get('per_page')
        reverse = data.get('reverse')
        columns = data.get('columns')
        start_date, end_date = convert_start_end_dates(data)

        result = get_filtered_records(filters, columns, start_date=start_date, end_date=end_date)

        # Only paginate if all the pagination parameters have been specified
        if page_index is not None and per_page is not None and sorting_key is not None and reverse is not None:
            result = get_paginated_records(result, sorting_key, page_index, per_page, reverse)
        return jsonify(result)


@data_provider_ns.route('/record_details/<string:source_id>', methods=['GET'])
@data_provider_ns.param('source_id', 'The primary key of the Airtable Source table that identifies a record.')
class RecordDetails(Resource):
    @data_provider_ns.doc('An endpoint for getting the details of a record based on source id.')
    def get(self, source_id):
        # Validate input
        payload, status_code = validate_request_input_against_schema({'source_id': source_id}, RecordDetailsSchema())
        if status_code != 200:
            # If there was an error with the input payload, return the error and 422 response
            return make_response(payload, status_code)

        # Get record details based on the source_id of the record
        record_details = get_record_details(source_id)
        return jsonify(record_details)


@data_provider_ns.route('/country_seroprev_summary', methods=['GET', 'POST'])
class GeogStudyCount(Resource):
    @data_provider_ns.doc('An endpoint for summarizing the seroprevalence data of a country.')
    def get(self):
        # Query all the records with no filters but only grab certain columns
        columns = ['country', 'denominator_value', 'serum_pos_prevalence', 'estimate_grade']
        records = get_filtered_records(filters=None, columns=columns, start_date=None, end_date=None)

        # Compute seroprevalence summaries per country per estimate grade level
        country_seroprev_summaries = get_country_seroprev_summaries(records)
        return jsonify(country_seroprev_summaries)

    def post(self):
        # Ensure payload is present
        json_input = request.get_json()
        if not json_input:
            return make_response({"message": "No input payload provided"}, 400)

        # Validate input payload
        payload, status_code = validate_request_input_against_schema(json_input, StudyCountSchema())
        if status_code != 200:
            # If there was an error with the input payload, return the error and 422 response
            return make_response(payload, status_code)

        # Query all the records with the desired filters. Pull only country, denom, and seroprev cols
        filters = json_input['filters']
        start_date, end_date = convert_start_end_dates(json_input)
        columns = ['country', 'denominator_value', 'serum_pos_prevalence', 'estimate_grade']
        records = get_filtered_records(filters, columns, start_date=start_date, end_date=end_date)

        # Compute seroprevalence summaries per country per estimate grade level
        country_seroprev_summaries = get_country_seroprev_summaries(records)
        return jsonify(country_seroprev_summaries)
