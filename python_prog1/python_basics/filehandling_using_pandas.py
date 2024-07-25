import pandas

fileobj = pandas.read_csv("../06-07-2024_session/housing.csv")

#print(fileobj.head())

#print(fileobj.values)

## dictionary

data = {"Name":["prabhu","kishore"],"Age":[34,30]}
print(data)
print(type(data))

print("----------------------------------")

#df = pandas.DataFrame(data)
#print(df)
#print(type(df))

#column = df.columns
#print(column)

#covert to csv file
#convert_to_csv = df.to_csv("testData.csv")

print(fileobj.ndim)  #tells about no of dimensions in the dataset
print(fileobj.shape) # tells about no of rows and columns of the dataset
print(fileobj.describe()) #  tells about mean, std, 25%, 50%, 75% , max , min values of dataset
print(fileobj.info()) # tells about statistical info of the dataset

print(fileobj.iloc[2,4]) # returns the corresponding value of the mentioned specific integer based location
print(fileobj.iloc[2:4,4]) # returns the corresponding value of the mentioned specific integer based location
# 2:4 specifies the rows range from the index 2,3 alone (exlcufing the final number , here refering as 4)
# 4 specifies the column index position

print(fileobj.loc[2:4,"total_bedrooms"])
# 2:4 specifies the rows range from the index 2,3 and 4 (including the final number , here referring as 4)
# "total_bedrooms" specifies the column name

print(fileobj.loc[2:4,["total_bedrooms","ocean_proximity"]])