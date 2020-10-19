import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sps
import datetime

# show complete records by changing rules
# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df_med = pd.read_csv("data_wrangling_medical_2020_u7199704.csv")
df_edu = pd.read_csv("data_wrangling_education_2020_u7199704.csv")
df_merge = pd.read_csv("data_wrangling_merged_2020_u7199704.csv")


# df_merge = pd.merge(left=df_med, right=df_edu, left_on='ssn', right_on='ssn')
# print(df_merge)
# df_merge.to_csv('data_wrangling_merged_2020_u7199704.csv', index=False)

# unique_med = df_med[df_med.ssn.isin(df_edu.ssn) == False]
unique_edu = df_edu[df_edu.ssn.isin(df_med.ssn) == False]

print(unique_edu)