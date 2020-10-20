import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sps
import datetime

# show complete records by changing rules
# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


# Read in the datasets
df_med = pd.read_csv("data_wrangling_medical_2020_u7199704.csv")
df_edu = pd.read_csv("data_wrangling_education_2020_u7199704.csv")
df_merge = pd.read_csv("data_wrangling_merged_2020_u7199704.csv")

# check for duplicate ssn's
med_duplicates = df_med[df_med.duplicated(['ssn'], keep=False)]

edu_duplicates = df_edu[df_edu.duplicated(['ssn'], keep=False)]
edu_duplicates = edu_duplicates.sort_values('ssn', ascending=False)

# print(med_duplicates)
# print(edu_duplicates)




# Merge the datasets on ssn
df_merge = pd.merge(left=df_med, right=df_edu, left_on='ssn', right_on='ssn')
# print(df_merge)

# Create a csv for the merged datasets
df_merge.to_csv('merge_A.csv', index=False)


# Pull out the records that did not have matching ssn's for both datasets
# unique_med = df_med[df_med.ssn.isin(df_edu.ssn) == False]
# unique_edu = df_edu[df_edu.ssn.isin(df_med.ssn) == False]

# Turn the unique datasets into csv's (Stage A)
# unique_med.to_csv('unique_med_A.csv', index=False)
# unique_edu.to_csv('unique_edu_A.csv', index=False)


# print(df_merge.dtypes)



# print(unique_edu)