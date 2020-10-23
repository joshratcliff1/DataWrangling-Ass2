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
df['middle_name'].fillna("not_specified", inplace=True)

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

# Update last postcodes
def postcode_update(row,attribute):
    if row['suburb'] == 'melville island' and row['state'] == 'NT':
        return '0822'
    elif row['suburb'] == 'victoria river' and row['state'] == 'NT':
        return '0852'
    elif row['suburb'] == 'daly' and row['state'] == 'NT':
        return '0822'

    elif row['suburb'] == 'launceston south' and row['state'] == 'TAS':
        return '7249'
    elif row['suburb'] == 'wynyard east' and row['state'] == 'TAS':
        return '7325'
    elif row['suburb'] == 'east tamar' and row['state'] == 'TAS':
        return '7248'
    elif row['suburb'] == 'devonport east' and row['state'] == 'TAS':
        return '7310'
    elif row['suburb'] == 'moonah west' and row['state'] == 'TAS':
        return '7009'
    elif row['suburb'] == 'teatree' and row['state'] == 'TAS':
        return '7007'
    elif row['suburb'] == 'shorewell' and row['state'] == 'TAS':
        return '7320'

    elif row['suburb'] == 'bokerup' and row['state'] == 'WA':
        return '6396'
    elif row['suburb'] == 'carnarvon north' and row['state'] == 'WA':
        return '6701'
    elif row['suburb'] == 'kalgoorie west' and row['state'] == 'WA':
        return '6430'

    elif row['suburb'] == 'kingston se' and row['state'] == 'SA':
        return '5275'

    elif row['suburb'] == 'paradise waters' and row['state'] == 'QLD':
        return '4217'
    elif row['suburb'] == 'spier' and row['state'] == 'QLD':
        return '4715'
    elif row['suburb'] == 'arcadia valley' and row['state'] == 'QLD':
        return '4702'
    elif row['suburb'] == 'nandowrie' and row['state'] == 'QLD':
        return '4722'
    elif row['suburb'] == 'tamborine village' and row['state'] == 'QLD':
        return '4270'
    elif row['suburb'] == 'groper creek' and row['state'] == 'QLD':
        return '4806'

    elif row['suburb'] == 'hill end' and row['state'] == 'QLD':
        return '4101'
    elif row['suburb'] == 'rannes' and row['state'] == 'QLD':
        return '4702'
    elif row['suburb'] == 'bilwon' and row['state'] == 'QLD':
        return '4880'
    elif row['suburb'] == 'teneriffe' and row['state'] == 'QLD':
        return '4005'
    elif row['suburb'] == 'belli' and row['state'] == 'QLD':
        return '4562'
    elif row['suburb'] == 'kirra' and row['state'] == 'QLD':
        return '4225'
    elif row['suburb'] == 'kupunn' and row['state'] == 'QLD':
        return '4405'
    elif row['suburb'] == 'mountain creek estate' and row['state'] == 'QLD':
        return '4557'

    elif row['suburb'] == 'kingsville south' and row['state'] == 'VIC':
        return '3015'
    elif row['suburb'] == 'ballarat south' and row['state'] == 'VIC':
        return '3350'
    elif row['suburb'] == 'lalalty' and row['state'] == 'VIC':
        return '3644'
    elif row['suburb'] == 'western port' and row['state'] == 'VIC':
        return '3984'
    elif row['suburb'] == 'emerald hill' and row['state'] == 'VIC':
        return '3782'
    elif row['suburb'] == 'canberra city' and row['state'] == 'ACT':
        return '2601'

    elif row['suburb'] == 'umina' and row['state'] == 'NSW':
        return '2257'
    elif row['suburb'] == 'jervis bay' and row['state'] == 'NSW':
        return '2540'
    elif row['suburb'] == 'kurrajong east' and row['state'] == 'NSW':
        return '2758'
    elif row['suburb'] == 'ettalong' and row['state'] == 'NSW':
        return '2257'
    elif row['suburb'] == 'the ridgeway' and row['state'] == 'NSW':
        return '2620'

    elif row['suburb'] == 'ballina east' and row['state'] == 'NSW':
        return '2478'
    elif row['suburb'] == 'gosford west' and row['state'] == 'NSW':
        return '2250'
    elif row['suburb'] == 'the retreat' and row['state'] == 'NSW':
        return '2355'
    elif row['suburb'] == 'denham beach' and row['state'] == 'NSW':
        return '2536'
    elif row['suburb'] == 'gosford north' and row['state'] == 'NSW':
        return '2250'

    elif row['suburb'] == 'wyong north' and row['state'] == 'NSW':
        return '2259'
    elif row['suburb'] == 'lismore south' and row['state'] == 'NSW':
        return '2480'
    elif row['suburb'] == 'harwood island' and row['state'] == 'NSW':
        return '2465'
    elif row['suburb'] == 'collaroy plateau' and row['state'] == 'NSW':
        return '2097'
    elif row['suburb'] == 'yatteyattah' and row['state'] == 'NSW':
        return '2539'

    elif row['suburb'] == 'uplands' and row['state'] == 'TAS':
        return '7320'
    elif row['suburb'] == 'galba' and row['state'] == 'NSW':
        return '2550'
    elif row['suburb'] == 'gosford east' and row['state'] == 'NSW':
        return '2250'
    elif row['suburb'] == 'bywong' and row['state'] == 'ACT':
        return '2621'

    else:
        return row['postcode']

'''
uplands	tas
bywong		ACT
'''



attribute = "postcode"
df[attribute] = df.apply(lambda row: postcode_update(row,attribute), axis=1)



"""Final Checks"""
print(df)
print(df.isnull().sum(axis = 0))
# print(df['weight'].value_counts())
# print(df['age_at_consultation'].value_counts())
print(df[df['postcode'].isnull()])


# Create a csv for the merged datasets
df.to_csv('data_wrangling_merged_2020_u7199704.csv', index=False)



# df[['weight']].plot.hist(bins=100)
#
# plt.show()


# TODO: Check Zero Salaries
# TODO: Lowercase States
# TODO:
# TODO:
# TODO:

# melville island nt 0822