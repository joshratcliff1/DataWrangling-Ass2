import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sps
import datetime

# show complete records by changing rules
# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Load the dataset into the dataframe
df_merge = pd.read_csv("partial_merges/merge_I.csv")

# Function to update when there are missing values
def attribute_update(row,attribute):
    att_x = attribute + "_x"
    att_y = attribute + "_y"
    if row[att_x] == row[att_y]:
        return row[att_x]
    elif pd.isnull(row[att_x]):
        return row[att_y]
    elif pd.isnull(row[att_y]):
        return row[att_x]

    # Used these for emails only.
    # elif "@" not in row[att_x]:
    #     return row[att_y]
    # elif "@" not in row[att_y]:
    #     return row[att_x]

    elif row['consultation_timestamp'] >= row['employment_timestamp']:
        return row[att_x]
    elif row['employment_timestamp'] >= row['consultation_timestamp']:
        return row[att_y]
    else:
        return "discrepancy"


def last_name(row,attribute):
    if row['consultation_timestamp'] >= row['employment_timestamp']:
        return row[att_x]
    elif row['employment_timestamp'] >= row['consultation_timestamp']:
        return row[att_y]

def maiden_name(row,attribute):
    att_x = attribute + "_x"
    att_y = attribute + "_y"
    if row[att_x] == row[att_y]:
        return "Not Applicable"

    elif row['consultation_timestamp'] >= row['employment_timestamp']:
        return row[att_y]
    elif row['employment_timestamp'] >= row['consultation_timestamp']:
        return row[att_x]


'''Updating address data'''
# attribute = "street_address"
# df_merge[attribute] = df_merge.apply(lambda row: attribute_update(row,attribute), axis=1)

# attribute = "suburb"
# df_merge[attribute] = df_merge.apply(lambda row: attribute_update(row,attribute), axis=1)

# attribute = "postcode"
# df_merge[attribute] = df_merge.apply(lambda row: attribute_update(row,attribute), axis=1)

# attribute = "state"
# df_merge[attribute] = df_merge.apply(lambda row: attribute_update(row,attribute), axis=1)

# attribute = "birth_date"
# df_merge[attribute] = df_merge.apply(lambda row: attribute_update(row,attribute), axis=1)

attribute = "first_name"
df_merge[attribute] = df_merge.apply(lambda row: attribute_update(row,attribute), axis=1)

# df_merge['last_name'] = df_merge.apply(lambda row: last_name(row,attribute), axis=1)
# df_merge['maiden_name'] = df_merge.apply(lambda row: maiden_name(row,attribute), axis=1)

# Check the maiden name values
# maiden = df_merge.loc[df_merge['last_name'] != df_merge['maiden_name']]
# print(maiden[[att_x,'consultation_timestamp','last_name','maiden_name',att_y,'employment_timestamp']])

# update the naming of the columns
# df_merge.rename(columns={'gender_x': 'gender_medical', 'gender_y': 'gender_education'}, inplace=True)
# df_merge.rename(columns={'rec_id_x': 'rec_id_medical', 'rec_id_y': 'rec_id_education'}, inplace=True)


print(df_merge)
# print(df_merge[attribute].describe())

# discrepancy = df_merge.loc[df_merge[attribute] == "discrepancy"]
# print(discrepancy[[att_x,attribute,att_y]])


# Create a csv for the merged datasets
df_merge.to_csv('merge_J.csv', index=False)