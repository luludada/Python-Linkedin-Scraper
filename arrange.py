import csv
with open('1000result4.csv', 'r') as infile, open('1000Reorder4.csv', 'a') as outfile:
    # output dict needs a list for new column ordering
    fieldnames = ['', 'name', 'job_title', 'location', 'url', 'skills',
    'school_1_name', 'school_1_years', 'school_ 1_program', 
    'school_2_name', 'school_2_years', 'school_ 2_program', 
    'school_3_name', 'school_3_years', 'school_ 3_program', 
    'school_4_name', 'school_4_years', 'school_ 4_program', 
    'experience_1_company', 'experience_1_years', 'experience_1_position_1', 'experience_1_position_2', 'experience_1_position_3', 'experience_1_position_4', 'experience_1_position_5', 'experience_1_position_6', 'experience_1_position_7', 'experience_1_position_8', 'experience_1_position_9', 'experience_1_position_10',
    'experience_2_company', 'experience_2_years', 'experience_2_position_1', 'experience_2_position_2', 'experience_2_position_3', 'experience_2_position_4', 'experience_2_position_5', 'experience_2_position_6', 'experience_2_position_7', 'experience_2_position_8',
    'experience_3_company', 'experience_3_years', 'experience_3_position_1', 'experience_3_position_2', 'experience_3_position_3', 'experience_3_position_4', 'experience_3_position_5',
    'experience_4_company', 'experience_4_years', 'experience_4_position_1', 'experience_4_position_2', 'experience_4_position_3', 'experience_4_position_4', 'experience_4_position_5',
    'experience_5_company', 'experience_5_years', 'experience_5_position_1', 'experience_5_position_2', 'experience_5_position_3', 'experience_5_position_4',
    'experience_6_company', 'experience_6_years', 'experience_6_position_1', 'experience_6_position_2', 'experience_6_position_3',
    'experience_7_company', 'experience_7_years', 'experience_7_position_1', 'experience_7_position_2',
    'experience_8_company', 'experience_8_years', 'experience_8_position_1', 'experience_8_position_2',
    'experience_9_company', 'experience_9_years', 'experience_9_position_1',
    'experience_10_company', 'experience_10_years', 'experience_10_position_1',
    'experience_11_company', 'experience_11_years', 'experience_11_position_1',
    'experience_12_company', 'experience_12_years', 'experience_12_position_1',
    'experience_13_company', 'experience_13_years', 'experience_13_position_1',
    'experience_5_position_5', 'experience_6_position_6', 'experience_7_position_7', 'experience_8_position_8', 'experience_9_position_9', 'experience_10_position_10', 'experience_11_position_11', 'experience_12_position_12']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    # reorder the header first
    writer.writeheader()
    for row in csv.DictReader(infile):
        # writes the reordered rows to the new file
        writer.writerow(row)