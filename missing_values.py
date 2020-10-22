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






