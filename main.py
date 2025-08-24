# This is a data cleaning application 
"""
please create a python application that can that can take dataset and clean the data
It should ask for dataset path and name
It should check number of duplicats and remove all duplicates
It should keep yhe copy of all the duplicates 
It should check for missing values
If any columns that is numeric it should replace nulls with mean else it should 
drop it
At the end it should save the dataset as clean data and aslo return 
duplicates record ,clean_data
"""

# importing dependencies
import pandas as pd
import numpy as np
import time 
import openpyxl
import xlrd
import os
import random

#data_path='C:\\Users\\win\\OneDrive\\Desktop\\Python_Automation_project\\Python_project\\Walmart.csv'
#data_name='Walm'
def data_cleaning_master(data_path,data_name):
    # checking path exists
    if not os.path.exists(data_path):
        print("please enter correct path  | ")
        return
    else:
        # checking the file type
        if data_path.endswith(".csv"):
            print("Dataset is CSV")
            data=pd.read_csv(data_path,encoding_errors='ignore')
        elif data_path.endswith(".xlsx"):
            print("Dataset is excle file")
            data=pd.read_excel(data_path)
        else:
            print("Unkown file type")
            return

    # showing number of records
    print(f"Dataset contain total rows : {data.shape[0]} \n Total columns : {data.shape[1]}")

    # clean the records

    duplicates=data.duplicated()
    total_duplicat=data.duplicated().sum()

    print(f"dataset has total duplicates : {total_duplicat}")

    # saving the duplicates
    if total_duplicat>0:
        duplicates_records=data[duplicates]
        duplicates_records.to_csv(f'C:\\Users\\win\\OneDrive\\Desktop\\Python_Automation_project\\Python_project\\{data_name}_Duplicates.csv',index=False)

    # deleting duplicates

    df=data.drop_duplicates()

    # find missing values

    total_missing_values=df.isnull().sum().sum()
    missing_values_columns=df.isnull().sum()


    print(f"Dataset has total missing values : {total_missing_values}")
    print(f"Dataset contain missing values by columns \n{missing_values_columns}")

    # deling with missing  values
    # fillna --int float
    # deopna -- any object

    columns=df.columns

    for col in columns:
        # filling mean for numeric columns
        if(df[col].dtype in (int,float)):
            df[col]=df[col].fillna(df[col].mean())
        
        else:
            df.dropna(subset=col,inplace=True) #update the dataframe


    # data is cleaned

    print(f"Congrats dataset is cleaned \nnumber of rows {df.shape[0]} \n number  of columns {df.shape[1]} ")

    # saving te dataset
    df.to_csv(f'C:\\Users\\win\\OneDrive\\Desktop\\Python_Automation_project\\Python_project\\{data_name}_clean.csv',index=False)


    print("Dataset is saved ")

    d=pd.read_csv(f'C:\\Users\\win\\OneDrive\\Desktop\\Python_Automation_project\\Python_project\\Walm_clean.csv')


if __name__=="__main__":
    print("Welcome to data Cleaning Master")
    data_path=input("Please enter dataset path : ")
    data_name=input("Please enter dataset name : ")

    # calling the function 
    data_cleaning_master(data_path,data_name)







