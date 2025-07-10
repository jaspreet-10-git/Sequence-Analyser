import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#to create a dataframe by importing the data from the csv file
print('The dataframe for analysing the effect of Whey Protein is given:')
print('*                                                              *')
df = pd.read_csv('/Users/jaspreetmarwaha/Library/Mobile Documents/com~apple~TextEdit/Documents/protein_whey_data.csv')
print(df)
print('----------------------------------------------------------------------------------------------------------------------------------------------------------------')

#to display information about the dataframe
print('The information about the dataframe is displayed:')
print('*                                                              *')
print(df.info())
print('----------------------------------------------------------------------------------------------------------------------------------------------------------------')
 
#define TimePoint as a categorical variable
print('The TimePoint variable will now be displayed as a categorical variable:')
print('*                                                                *')
timeorder = [ 'Pre-intervention','Post-intervention']
categories = timeorder
df['TimePoint'] = pd.Categorical(df['TimePoint'],categories,ordered = True)
print(df['TimePoint'].dtype)
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------')

#pivoting the data
print('The dataframe is pivoted to analyse the Pre-intervention and Post-intervention changes across all variables:')
df_pivot = df.pivot_table(index=['PatientID','Age','Sex','Group'],columns='TimePoint', values=['BodyWeight_kg','FatMass_kg','FatFreeMass_kg','BF_pct','BenchPress_1RM_kg','LegPress_1RM_kg'])
df_pivot.columns = ['_'.join(col).strip()
                    if isinstance(col,tuple) and col[1] else col[0]
                    for col in df_pivot.columns.values]
print(df_pivot.head())
print('------------------------------------------------------------------------------------------------------------------------------------------------------------------')

#calculating absolute changes
#df_pivot['BF_pct_ch'] = df_pivot['BF_pct_Post-intervention']-df_pivot['BF_pct_Pre-intervention']
#print(df_pivot['BF_pct_ch'])
#creating a single code to calculate the absolute changes instead of writing individual codes for each variable
#this is done by using a for loop
measurements_var= ['BodyWeight_kg',
                   'FatMass_kg',
                   'FatFreeMass_kg',
                   'BF_pct',
                   'BenchPress_1RM_kg',
                   'LegPress_1RM_kg']

for var in measurements_var:
    pre_col = f'{var}_Pre-intervention'
    post_col = f'{var}_Post-intervention'
    change_col = f'{var}_change_col'

    df_pivot[change_col]= df_pivot[post_col]-df_pivot[pre_col]
print(df_pivot[change_col])
print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------')

#calculate percentage changes 
measurements_pct = [ 'BodyWeight_kg',
                   'FatMass_kg',
                   'FatFreeMass_kg',
                   'BF_pct',
                   'BenchPress_1RM_kg',
                   'LegPress_1RM_kg'
    
]

for var_pct in measurements_pct:

    pre_pct = f'{var_pct}_Pre-intervention'
    post_pct = f'{var_pct}_Post-intervention'
    change_pct = f'{var_pct}_change_col_pct'

    df_pivot[change_pct]= ((df_pivot[post_pct]-df_pivot[pre_pct])/df_pivot[pre_pct])*100
    print(df_pivot[change_pct])
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------')

#calculate central tendency measures
var_statistics=[ 'BodyWeight_kg',
                   'FatMass_kg',
                   'FatFreeMass_kg',
                   'BF_pct',
                   'BenchPress_1RM_kg',
                   'LegPress_1RM_kg'
]

for var_st in var_statistics:
    var_mean= f'{var_st}_Pre-intervention'
    var_median= f'{var_st}_Post-intervention'
    pre_mean=df_pivot[var_mean].mean()
    post_mean=df_pivot[var_median].mean()
    pre_median=df_pivot[var_mean].mean()
    post_median=df_pivot[var_median].median()
    values_stats=['BodyWeight_kg_Pre-intervention','BodyWeight_kg_Post-intervention',
                   'FatMass_kg_Pre-intervention','FatMass_kg_Post-intervention',
                   'FatFreeMass_kg_Pre-intervention','FatFreeMass_kg_Post-intervention',
                   'BF_pct_Pre-intervention','BF_pct_Post-intervention',
                   'BenchPress_1RM_kg_Pre-intervention','BenchPress_1RM_kg_Post-intervention',
                   'LegPress_1RM_kg_Pre-intervention','LegPress_1RM_kg_Post-intervention']
    values_stats_groupby = df_pivot.groupby('Group')[values_stats].describe()
    print(values_stats_groupby)
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------')



    

