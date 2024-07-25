from tarfile import data_filter

import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

lineSeparator = "******************************************************************************************"

"""sample dataset from web"""
dataobj = pd.read_csv("Chennai_housing_sale.csv")
#print(dataobj)

"""print first 5 rows and last 5 rows"""
print("---------------------------FIRST 5 ROWS---------------------------")
print(dataobj.head(5))
print(lineSeparator)
print("---------------------------LAST 5 ROWS----------------------------")
print(dataobj.tail(5))

"""File meta data"""
print(lineSeparator)
print("---------------------------No of dimensions in the dataset----------------------------")
print(dataobj.ndim)
print("---------------------------ROWS and COLUMNS of the dataset----------------------------")
print(dataobj.shape)
print("---------------------------MEAN,STD, 25%, 50%, 75%, MAX, MIN values----------------------------")
print(dataobj.describe())
print("---------------------------STATISTICAL info of the dataset----------------------------")
print(dataobj.info())

print(lineSeparator)
print("---------------------retrieve the cell value of specific integer based index location----------------------")
print(dataobj.iloc[2,4])
print("---------------------retrieve the cell value of specific integer based index location excluding final row --------------------")
print(dataobj.iloc[2:4,4])
print("---------------------retrieve the cell value of specific index location INCLUDING final row with column name--------------------")
print(dataobj.loc[2:4,'SALE_COND'])
print("---------------------retrieve the cell value of specific index location INCLUDING final row row with multiple column names--------------------")
print(dataobj.loc[1:5,['AREA','SALE_COND']])

print(lineSeparator)
print("---------------------Create Dictionary object and upload the data to csv using Dataframe----------------------")
dataDictObj = {"Name":["Prithiviraj","Ramesh"],"Assignment_Date":["06-07-2024","07-07-2024"],"Completion_Status":["COMPLETED","IN_PROGRESS"]}
print(dataDictObj)
dataFrameObj = pandas.DataFrame(dataDictObj)
print(dataFrameObj)
print("---------------------Column details of new csv data set----------------------")
dataFrameColmObj = dataFrameObj.columns
print(dataFrameColmObj)
print("---------------------CSV file creation with new dataset using dataframe object----------------------")
csvConversionObj = dataFrameObj.to_csv("assignment_status.csv")

print(lineSeparator)
findingNull = dataobj.isnull()
print(findingNull.head(10))

#dataobj.fillna("NOVALUE",inplace=True)
#print(dataobj.head(10))

print("------------------------To see the impact of following 2 lines execution, comment the line numnbers 59 & 60--------------------")
#dataobj["AREA"].fillna("NOVALUE", inplace=True)
#print(dataobj.head(10))

#COMMIS,INT_SQFT,DATE_SALE
dataobj.fillna({"INT_SQFT":0000,"DATA_SALE":"99-99-9999","COMMIS":00000}, inplace=True)
print(dataobj.head(10))