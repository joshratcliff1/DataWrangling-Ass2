import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sps
import datetime

# show complete records by changing rules
# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


# Read in the unique datasets
df_med_A = pd.read_csv("unique_med_A.csv")
df_edu_A = pd.read_csv("unique_edu_A.csv")


def SLK_column(row):
    SLK = ""

    # Get family name value
    #
    fam_name = row['last_name']
    fam_name = str(fam_name)

    if (fam_name == ''):
        SLK += '999'
    else:
        fam_name = fam_name.replace('-', '')  # Remove non letter characters
        fam_name = fam_name.replace(",", '')
        fam_name = fam_name.replace('_', '')

        if (len(fam_name) >= 5):
            SLK += (fam_name[1] + fam_name[2] + fam_name[4])
        elif (len(fam_name) >= 3):
            SLK += (fam_name[1] + fam_name[2] + '2')
        elif (len(fam_name) >= 2):
            SLK += (fam_name[1] + '22')

    # Get given name value
    #
    giv_name = row['first_name']
    giv_name = str(giv_name)

    if giv_name == '':
        SLK += '99'
    else:
        giv_name = giv_name.replace('-', '')  # Remove non letter characters
        giv_name = giv_name.replace(",", '')
        giv_name = giv_name.replace('_', '')

        if (len(giv_name) >= 3):
            SLK += (giv_name[1] + giv_name[2])
        elif (len(giv_name) >= 2):
            SLK += (giv_name[1] + '2')

    # DoB structure we use: dd/mm/yyyy

    # Get date of birth
    #
    dob = row['birth_date']

    dob_list = row['birth_date'].split('/')

    # Add some checks
    #
    if len(dob_list[0]) < 2:
        dob_list[0] = '0' + dob_list[0]  # Add leading zero for days < 10
    if len(dob_list[1]) < 2:
        dob_list[1] = '0' + dob_list[1]  # Add leading zero for months < 10

    dob = ''.join(dob_list)  # Create: ddmmyyyy

    assert len(dob) == 8, dob

    SLK += dob

    # Get gender
    #
    gender = row['gender'].lower()

    if (gender == 'm'):
        SLK += '1'
    elif (gender == 'f'):
        SLK += '2'
    else:
        SLK += '9'

    return SLK


df_edu_A['SLK'] = df_edu_A.apply(lambda row: SLK_column(row), axis=1)
df_med_A['SLK'] = df_med_A.apply(lambda row: SLK_column(row), axis=1)

# print(df_edu_A[['last_name','first_name','birth_date','gender','SLK']])
# print(df_med_A[['last_name','first_name','birth_date','gender','SLK']])

# Merge the datasets on SLK key
df_merge = pd.merge(left=df_med_A, right=df_edu_A, left_on='SLK', right_on='SLK')
print(df_merge)
# print(df_merge[['first_name_x','last_name_x','birth_date_x','first_name_y','middle_name_y','last_name_y','birth_date_y']])

# Create a csv for the merged datasets
# df_merge.to_csv('data_wrangling_merged_2020_u7199704.csv', index=False)


# Pull out the records that did not have matching ssn's for both datasets
# unique_med = df_med_A[df_med_A.SLK.isin(df_edu_A.SLK) == False]
# unique_edu = df_edu_A[df_edu_A.SLK.isin(df_med_A.SLK) == False]

# print(unique_med)
# print(unique_edu)

# Turn the unique datasets into csv's (Stage A)
# unique_med.to_csv('unique_med_A.csv', index=False)
# unique_edu.to_csv('unique_edu_A.csv', index=False)
