import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sps
import datetime

# show complete records by changing rules
# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Load the dataset into the dataframe
df_merge = pd.read_csv("merge_FINAL.csv")
df_edu = pd.read_csv("unique_edu_A.csv")
df_med = pd.read_csv("unique_med_A.csv")


df_merge = df_merge.ssn
df_edu = df_edu.ssn
df_med = df_med.ssn

print(df_merge.nunique())
print(df_edu.nunique())
print(df_med.nunique())