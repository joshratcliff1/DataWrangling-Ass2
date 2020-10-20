import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sps
import datetime

# show complete records by changing rules
# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Load the dataset into the dataframe
df_merge = pd.read_csv("partial_merges/merge_J.csv")

df_final = df_merge[['ssn','rec_id_medical','rec_id_education','first_name','middle_name','last_name',
                     'maiden_name','gender_medical','gender_education','age_at_consultation','birth_date',
                     'current_age','medicare_number','street_address', 'suburb','postcode', 'state','phone',
                     'email','marital_status','height','weight','bmi','blood_pressure','cholesterol_level',
                     'smoking_status','clinical_notes','consultation_timestamp','education','occupation',
                     'salary','credit_card_number','years_of_experience','employment_timestamp']]

print(df_final)


# Create a csv for the merged datasets
df_final.to_csv('merge_FINAL.csv', index=False)




"""
Order of partial merges:
A - raw merged
B - updated middle name
C - Updated email
D - Updated phone
E - Updated last name
F - Updated names for gender and rec_id attributes
G - Changed maiden name to “Not Applicable” when not required
H - Updated Address data
I - Changed birthdate name
"""