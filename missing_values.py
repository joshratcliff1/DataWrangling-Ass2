import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps
import datetime

# show complete records by changing rules
# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Load the dataset into the dataframe
df = pd.read_csv("merge_FINAL.csv")

# print(df.isnull().sum(axis = 0))


att1 = 'occupation'
att2 = 'salary'
att3 = 'credit_card_number'
att4 = 'marital_status'
att5 = 'email'
att6 = 'phone'
att7 = 'middle_name'

# Checks on missing values
# print(df[df[att1,att2,att3].isnull()])
# print(df.isnull().groupby([att1,att2,att3]).size())
# print(df.isnull().groupby([att1,att2,att3,att4,att5,att6,att7]).size())
# print(df.isnull().groupby([att1,att2,att3]).size())
# print(df.isnull().groupby([att1,att2,att4]).size())
# print(df.isnull().groupby([att1,att3,att4]).size())
# print(df.isnull().groupby([att2,att3,att4]).size())
# print(df.isnull().groupby([att1,att2,att5]).size())
# print(df.isnull().groupby([att1,att2,att6]).size())
# print(df.isnull().groupby([att1,att3,att5]).size())

test = ['marital_status', 'email', 'phone', 'middle_name']
best_so_far = "occupation  credit_card_number  marital_status"

df['salary'] = df['salary'].mask(df['salary'].between(-10000, 0))

# print(df.isnull().sum(axis = 0))

# Looking at Salaries
# df[['salary']].plot.hist(bins=200)
#
# plt.show()


# print(df['salary'].mean())
#
# print(df['salary'].median())

df['salary'].fillna(85191.999, inplace=True)

# print(df.isnull().sum(axis = 0))


# Doing checks on weight
# print(df['weight'].describe())

df_weight = df.loc[df['weight'] <= 0]

# print(df_weight)


df['postcode_fd'] = df.postcode.astype(str)

df['postcode_fd'] = df.postcode_fd.str[0:1]

state_list = [('0','nt'),('7','tas'),('6','wa'),('5','sa'),('4','qld'),('3','vic'),('2','act')]

for i in range(len(state_list)):
    state = state_list[i][1]
    pc_num = state_list[i][0]

    df_postcode = df.loc[(df['state'].str.lower() == state) & (df['postcode_fd'] != pc_num)]
    print(df_postcode[['postcode_fd', 'postcode', 'suburb', 'state']])

# print(df[['postcode_fd','postcode']])


# Create a csv for the merged datasets
# df.to_csv('update_B.csv', index=False)


"""
List of Updates:
A - Updated the missing salaries
"""
