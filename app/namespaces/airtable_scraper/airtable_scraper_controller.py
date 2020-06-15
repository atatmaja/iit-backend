import os
from datetime import datetime

from flask_restplus import Resource, Namespace
from flask import jsonify, current_app as app

from .airtable_scraper_service import get_all_records
from app.utils import write_to_json, read_from_json

airtable_scraper_ns = Namespace('airtable_scraper', description='An endpoint for scraping airtable data.')


@airtable_scraper_ns.route('/records', methods=['GET'])
class AirtableScraper(Resource):
    @airtable_scraper_ns.doc('An endpoint for getting all records of airtable data.')
    def get(self):
        try:
            # Check how long it has been since cached_results.json was last updated
            current_time = datetime.now()
            file_created_datetime =\
                datetime.fromtimestamp(os.path.getmtime('app/namespaces/airtable_scraper/cached_results.json'))
            hour_diff = ((current_time - file_created_datetime).total_seconds())/3600
            # If longer than value of time diff param, generate a new cache
            generate_new_cache = True if hour_diff > app.config['AIRTABLE_TIME_DIFF'] else False
        except FileNotFoundError:
            # If cached_results.json has never been created, generate a new cache
            generate_new_cache = True
            file_created_datetime = datetime.now()
        if generate_new_cache:
            # Get all records from using airtable API
            records, status_code = get_all_records()
            if status_code == 200:
                # Write new records to json only if the airtable API request was successful
                write_to_json(records, app.config['AIRTABLE_CACHED_RESULTS_PATH'])
        else:
            # Read records from json cache layer
            records = read_from_json(app.config['AIRTABLE_CACHED_RESULTS_PATH'])
            status_code = 200
        result = {"airtable_request_status_code": status_code, "records": records, "updated_at": file_created_datetime}
        return jsonify(result)

