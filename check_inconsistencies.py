import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sps
import datetime

# show complete records by changing rules
# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df_merge = pd.read_csv("data_wrangling_merged_2020_u7199704.csv")

def attribute_check(row,attribute):
    att_x = attribute + "_x"
    att_y = attribute + "_y"
    if row[att_x] == row[att_y]:
        return True
    else:
        return False


check_attribute = "email"
check_x = check_attribute + "_x"
check_y = check_attribute + "_y"

df_merge['same_name'] = df_merge.apply(lambda row: attribute_check(row,check_attribute), axis=1)

same_name = df_merge.loc[df_merge['same_name'] == False]

# print(same_name[[check_x,check_y]])
print(same_name)