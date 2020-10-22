import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sps
import datetime

# show complete records by changing rules
# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Load the dataset into the dataframe
df = pd.read_csv("update_FINAL.csv",dtype={'postcode':str})
df_edu = pd.read_csv("data_wrangling_education_2020_u7199704.csv")


# Remove Rows where there is no occupation listed
df = df[df['occupation'].notna()]

# Remove credit card and medicare number
del df['credit_card_number']
del df['medicare_number']

# Upper case State
df['state'] = df['state'].str.upper()

# Remove semi-colons from clinical notes
df['clinical_notes'] = df['clinical_notes'].str.replace(';','-')

# Fill in missing phone and email details
df['phone'].fillna("not_provided", inplace=True)
df['email'].fillna("not_provided", inplace=True)

# Update genders
def gender_update(row,attribute):
    if row['gender'] == row['gender_education']:
        return row['gender']
    else:
        return 'indeterminate'


df = df.rename(columns={'gender_medical': 'gender'})

attribute = "gender"
df[attribute] = df.apply(lambda row: gender_update(row,attribute), axis=1)
del df['gender_education']



"""Final Checks"""
print(df)
print(df_edu.isnull().sum(axis = 0))
print(df.isnull().sum(axis = 0))
# print(df['weight'].value_counts())
# print(df['age_at_consultation'].value_counts())

# Create a csv for the merged datasets
df.to_csv('FINAL_FINAL.csv', index=False)



# df[['weight']].plot.hist(bins=100)
#
# plt.show()


# TODO: Check Zero Salaries
# TODO: Lowercase States
# TODO:
# TODO:
# TODO: