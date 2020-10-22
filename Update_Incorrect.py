import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps
import datetime

# show complete records by changing rules
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Load the dataset into the dataframe
df = pd.read_csv("merge_FINAL.csv")


'''Doing checks on Salary'''

# This line takes any salary values below 0 and replaces them with NaN
df['salary'] = df['salary'].mask(df['salary'].between(-10000, 0))

# Adds a dummy value for the salaries.
df['salary'].fillna(85191.99, inplace=True)

'''
# print(df.isnull().sum(axis = 0))
# Looking at Salaries
# df[['salary']].plot.hist(bins=200)
# plt.show()
# print(df['salary'].mean())
# print(df['salary'].median())
'''


# print(df.isnull().sum(axis = 0))

# Update Marital Status
df['marital_status'].fillna("Not_Specified", inplace=True)
print(df['marital_status'].describe())


# Doing checks on weight
# print(df['weight'].describe())

'''Updating Weight Values, using BMI'''
def weight(row):
    if row['weight'] < 0:
        row['weight'] = int(round(row['bmi'] * row['height'] * row['height'] / 100 / 100))
    return row['weight']


df['weight'] = df.apply(lambda row: weight(row), axis=1)


'''
df_weight = df.loc[df['weight'] <= 0]
print(df_weight)
'''




# Load the postcode dataset into the dataframe
df_pc = pd.read_csv("postcode-suburb-state-2005-original.csv", dtype=str)
df_pc['Locality'] = df_pc['Locality'].str.lower()
df_pc['State'] = df_pc['State'].str.lower()
df_pc = df_pc.drop_duplicates(['Locality','State'],keep= 'first')
# print(df_pc)

# strip the whitespace from suburb
df['suburb'] = df['suburb'].str.strip()
df['suburb'] = df['suburb'].str.replace('  ',' ')
df['suburb'] = df['suburb'].str.lower()
df['state'] = df['state'].str.lower()

# add the correct postcode's to the original data
df_med = pd.read_csv("data_wrangling_medical_2020_u7199704.csv", dtype=str)
df_med = df_med[['ssn','postcode']]
df_med = df_med.rename(columns={'postcode': 'new_pc'})

df = pd.merge(left=df, right=df_med, left_on='ssn', right_on='ssn')
df['postcode'] = df['new_pc']
del df['new_pc']


# Merge the datasets on suburb-state
df = pd.merge(how='left',left=df, right=df_pc, left_on=['suburb','state'], right_on=['Locality','State'])
# df['postcode'] = df.Pcode


# Function to update when there are missing values
def attribute_update(row,attribute):
    if row['postcode'] == row['Pcode']:
        return row['postcode']
    elif pd.isnull(row['Pcode']):
        return row['postcode']
    else:
        return row['Pcode']


attribute = "postcode"
df[attribute] = df.apply(lambda row: attribute_update(row,attribute), axis=1)

'''
# Check for incorrect postcodes
df['postcode_fd'] = df.postcode.str[0:1]

state_list = [('0','nt'),('7','tas'),('6','wa'),('5','sa'),('4','qld'),('3','vic'),('2','act')]


for i in range(len(state_list)):
    state = state_list[i][1]
    pc_num = state_list[i][0]

    df_postcode = df.loc[(df['state'].str.lower() == state) & (df['postcode_fd'] != pc_num)]
    print(df_postcode[['postcode_fd', 'postcode', 'Pcode', 'suburb', 'state']])
'''

# Remove columns used for checking postcodes
del df['Pcode']
del df['Locality']
del df['State']

'''Final Checks - Printing Values'''
print(df)
# print(df.isnull().sum(axis = 0))
# print(df.describe())

# Create a csv for the merged datasets
df.to_csv('update_FINAL.csv', index=False)


"""
List of Updates:
A - Updated the missing salaries
"""
