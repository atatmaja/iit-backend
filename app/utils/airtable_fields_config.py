dashboard_fields = ['Source Name', 'Publication Date', 'First Author Full Name', 'URL', 'Source Type',
                    'Source Publisher', 'One-Line Summary', 'Study Type', 'Study Status', 'Country',
                    'Lead Organization', 'State/Province', 'County/City', 'Sampling Start Date', 'Sampling End Date',
                    'Sample Frame (sex)', 'Sample Frame (age)', 'Sample Frame (groups of interest)', 'Sampling Method',
                    'Test Manufacturer', 'Approving Regulator', 'Test Type', 'Specimen Type', 'Isotype(s) Reported',
                    'Sensitivity', 'Specificity', 'Include in N?', 'Denominator Value', 'Numerator Definition',
                    'Serum positive prevalence', 'Overall Risk of Bias (JBI)']

research_fields = ['Source Name', 'Publication Date', 'First Author Full Name', 'URL', 'Source Type',
                   'Source Publisher', 'One-Line Summary', 'Study Type', 'Study Status', 'Country',
                   'Lead Organization', 'State/Province', 'County/City', 'Sampling Start Date', 'Sampling End Date',
                   'Sample Frame (sex)', 'Sample Frame (age)', 'Sample Frame (groups of interest)', 'Sampling Method',
                   'Test Manufacturer', 'Approving Regulator', 'Test Type', 'Specimen Type', 'Isotype(s) Reported',
                   'Sensitivity', 'Specificity', 'Include in N?', 'Denominator Value', 'Numerator Definition',
                   'Serum positive prevalence', 'Serum + prevalence, 95% CI Lower', 'Serum + prevalence, 95% CI Upper',
                   'Overall Risk of Bias (JBI)', 'Included?', 'Grade of Estimate Scope',
                   'Sub-grouping Variable', 'Geography Type', 'JBI 1', 'JBI 2', 'JBI 3', 'JBI 4', 'JBI 5', 'JBI 6',
                   'JBI 7', 'JBI 8', 'JBI 9', 'Superceded?', 'Test Adjustment', 'Population Adjustment', 
                   'Sensitivity Denominator', 'Specificity Denominator', 'Test Validation', 'Independent Se', 
                   'Independent Se n', 'Independent Sp', 'Independent Sp n', 'Independent Eval Link',
                   'Independent Eval Lab', 'Average age', 'Measure of age', 'Age variation', 'Age variation measure',
                   'Number of females', 'Number of males']

full_airtable_fields = {'Source Name': 'SOURCE_NAME',
                        'Publication Date': 'PUB_DATE',
                        'First Author Full Name': 'FIRST_AUTHOR',
                        'URL': 'URL',
                        'Source Type': 'SOURCE_TYPE',
                        'Source Publisher': 'PUBLISHER',
                        'One-Line Summary': 'SUMMARY',
                        'Study Type': 'STUDY_TYPE',
                        'Grade of Estimate Scope': 'ESTIMATE_GRADE',
                        'Study Status': 'STUDY_STATUS',
                        'Country': 'COUNTRY',
                        'Lead Organization': 'LEAD_ORG',
                        'State/Province': 'STATE',
                        'County/City': 'CITY',
                        'Sampling Start Date': 'SAMPLING_START',
                        'Sampling End Date': 'SAMPLING_END',
                        'Sample Frame (sex)': 'SEX',
                        'Sample Frame (age)': 'AGE',
                        'Sample Frame (groups of interest)': 'POPULATION_GROUP',
                        'Sampling Method': 'SAMPLING',
                        'Test Manufacturer': 'MANUFACTURER',
                        'Approving Regulator': 'APPROVAL',
                        'Test Type': 'TEST_TYPE',
                        'Specimen Type': 'SPECIMEN_TYPE',
                        'Isotype(s) Reported': 'ISOTYPES',
                        'Sensitivity': 'SENSITIVITY',
                        'Specificity': 'SPECIFICITY',
                        'Include in N?': 'INCLUDE_IN_N',
                        'Denominator Value': 'DENOMINATOR',
                        'Numerator Definition': 'NUM_DEFINITION',
                        'Serum positive prevalence': 'SERUM_POS_PREVALENCE',
                        'Serum + prevalence, 95% CI Lower': 'SEROPREV_95_CI_LOWER',
                        'Serum + prevalence, 95% CI Upper': 'SEROPREV_95_CI_UPPER',
                        'Overall Risk of Bias (JBI)': 'OVERALL_RISK_OF_BIAS',
                        'Included?': 'INCLUDED',
                        'Sub-grouping Variable': 'SUBGROUP_VAR',
                        'Geography Type': 'GEOG_TYPE',
                        'JBI 1': 'JBI_1',
                        'JBI 2': 'JBI_2',
                        'JBI 3': 'JBI_3',
                        'JBI 4': 'JBI_4',
                        'JBI 5': 'JBI_5', 
                        'JBI 6': 'JBI_6',
                        'JBI 7': 'JBI_7', 
                        'JBI 8': 'JBI_8', 
                        'JBI 9': 'JBI_9', 
                        'Superceded?': 'SUPERCEDED', 
                        'Test Adjustment': 'TEST_ADJ', 
                        'Population Adjustment': 'POP_ADJ', 
                        'Sensitivity Denominator': 'SE_N', 
                        'Specificity Denominator': 'SP_N', 
                        'Test Validation': 'TEST_VALIDATION', 
                        'Independent Se': 'IND_SE', 
                        'Independent Se n': 'IND_SE_N', 
                        'Independent Sp': 'IND_SP', 
                        'Independent Sp n': 'IND_SP_N', 
                        'Independent Eval Link': 'IND_EVAL_LINK', 
                        'Independent Eval Lab': 'IND_EVAL_LAB',
                        'Average age': 'AVERAGE_AGE',
                        'Measure of age': 'MEASURE_OF_AGE',
                        'Age variation': 'AGE_VARIATION',
                        'Age variation measure': 'AGE_VARIATION_MEASURE',
                        'Number of females': 'NUMBER_OF_FEMALES',
                        'Number of males': 'NUMBER_OF_MALES'}

airtable_fields_config = {'dashboard': {k: full_airtable_fields[k] for k in dashboard_fields},
                          'research': {k: full_airtable_fields[k] for k in research_fields}}
