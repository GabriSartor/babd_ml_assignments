# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 18:17:06 2021

@author: Gabry
"""

#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

import seaborn as sns


df_data = pd.read_csv("1_joined_dataframe_all_columns.csv", index_col=0)

def transform_to_bool(df, column, true_value):
    df.fillna({column: False}, inplace=True)
    df.replace({column: true_value}, True, inplace=True)
    df.astype({column: 'bool'})

transform_to_bool(df_data, 'DIED', 'Y')
transform_to_bool(df_data, 'L_THREAT', 'Y')
transform_to_bool(df_data, 'ER_VISIT', 'Y')
transform_to_bool(df_data, 'HOSPITAL', 'Y')
transform_to_bool(df_data, 'X_STAY', 'Y')
transform_to_bool(df_data, 'DISABLE', 'Y')
transform_to_bool(df_data, 'BIRTH_DEFECT', 'Y')
transform_to_bool(df_data, 'OFC_VISIT', 'Y')
transform_to_bool(df_data, 'ER_ED_VISIT', 'Y')

df_data['DATEDIED'] =  pd.to_datetime(df_data['DATEDIED'], infer_datetime_format=True)
df_data['VAX_DATE'] =  pd.to_datetime(df_data['VAX_DATE'], infer_datetime_format=True)
df_data['ONSET_DATE'] =  pd.to_datetime(df_data['ONSET_DATE'], infer_datetime_format=True)
df_data['TODAYS_DATE'] =  pd.to_datetime(df_data['TODAYS_DATE'], infer_datetime_format=True)

df_data[df_data['AGE_YRS'] < 3].to_csv("2_babies_subset.csv", index=False)

indexNames = df_data[df_data['AGE_YRS'] < 3].index
# Delete these row indexes from dataFrame
df_data.drop(indexNames , inplace=True)

#DROP COLUMNS
df_data = df_data.drop(columns=['CAGE_YR', 'CAGE_MO'])
df_data = df_data.drop(columns=['RPT_DATE'])
df_data = df_data.drop(columns=['V_FUNDBY'])
df_data = df_data.drop(columns=['FORM_VERS'])

df_data.to_csv("2_clean_dataset.csv", index=False)

