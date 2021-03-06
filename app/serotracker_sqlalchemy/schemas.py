from marshmallow import Schema, fields, validate

class AirtableSourceSchema(Schema):
    source_id = fields.UUID(allow_none=True)
    source_name = fields.Str(allow_none=True)
    #publication_date = fields.DateTime()
    first_author = fields.Str(validate=validate.Length(max=128), allow_none=True)
    url = fields.Str(allow_none=True)
    source_type = fields.Str(validate=validate.Length(max=64), allow_none=True)
    source_publisher = fields.Str(validate=validate.Length(max=256), allow_none=True)
    summary = fields.Str(allow_none=True)
    study_type = fields.Str(validate=validate.Length(max=128), allow_none=True)
    study_status = fields.Str(validate=validate.Length(max=32), allow_none=True)
    country = fields.Str(validate=validate.Length(max=64), allow_none=True)
    lead_organization = fields.Str(validate=validate.Length(max=128), allow_none=True)
    #sampling_start_date = fields.DateTime()
    #sampling_end_date = fields.DateTime()
    sex = fields.Str(validate=validate.Length(max=16), allow_none=True)
    sampling_method = fields.Str(validate=validate.Length(max=128), allow_none=True)
    sensitivity = fields.Float(allow_none=True, allow_nan=True)
    specificity = fields.Float(allow_none=True, allow_nan=True)
    include_in_n = fields.Boolean(allow_none=True)
    # Should be an int but doing this so that we can guard against NaN values
    denominator_value = fields.Float(allow_none=True, allow_nan=True)
    numerator_definition = fields.Str(allow_none=True)
    serum_pos_prevalence = fields.Float(allow_none=True, allow_nan=True)
    overall_risk_of_bias = fields.Str(validate=validate.Length(max=128), allow_none=True)
    isotype_igg = fields.Boolean(allow_none=True)
    isotype_igm = fields.Boolean(allow_none=True)
    isotype_iga = fields.Boolean(allow_none=True)
    estimate_grade = fields.Str(validate=validate.Length(max=32), allow_none=True)
    #created_at = fields.DateTime()
    # Multi select fields
    city = fields.List(fields.Str(validate=validate.Length(max=128)), allow_none=True)
    state = fields.List(fields.Str(validate=validate.Length(max=128)), allow_none=True)
    age = fields.List(fields.Str(validate=validate.Length(max=64)), allow_none=True)
    population_group = fields.List(fields.Str(validate=validate.Length(max=128)), allow_none=True)
    test_manufacturer = fields.List(fields.Str(validate=validate.Length(max=128)), allow_none=True)
    approving_regulator = fields.List(fields.Str(validate=validate.Length(max=256)), allow_none=True)
    test_type = fields.List(fields.Str(validate=validate.Length(max=256)), allow_none=True)
    specimen_type = fields.List(fields.Str(validate=validate.Length(max=64)), allow_none=True)

