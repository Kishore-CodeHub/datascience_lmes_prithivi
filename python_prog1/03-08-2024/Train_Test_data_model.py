from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd

# df = pd.read_csv("housing.csv")
#
# x = df[["total_rooms","total_bedrooms","population"]]
# y = df["median_house_value"]

data = {"Year" : [2000,2001,2002,2003,2004,2005],"Price":[4000,5000,6000,7000,8000,9000]}

df = pd.DataFrame(data)

x = df[["Year"]]
y = df["Price"]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)
#random_state attribute means- to select always same no of(set of) data , instead of mixed row nos
#train_size attribute means to choose specific percentage of data from the dataset to train , eg 0.8 means 80% of data
#test_size attribute means to choose specific percentage of data from the dataset to test , eg 0.2 means 20% of data
#
# print("------------x_train_data---------------")
# print(x_train)

# print("------------y_train_data---------------")
# print(y_train)
#
# print("------------x_test_data---------------")
# print(x_test)
# print("------------y_test_data---------------")
# print(y_test)

model = LinearRegression()
model.fit(x_train,y_train)
print("------x-test-------")
print(x_test)
print("------y-test-------")
print(y_test)
prediction = model.predict(x_test)

#prediction = model.predict(pd.DataFrame({"Year": [2010]}))
#prediction = model.predict(pd.DataFrame({"Year": [2010]}))
#print(prediction)

#How do we assess our preediction is right or wrong ?
#Using metrics

from sklearn.metrics import r2_score
r2_score_output = r2_score(y_test, prediction)
print(r2_score_output)

#plot the data
plt.scatter(x_test,y_test, color="blue", label="Actual_input_data")
plt.plot(x_test, prediction, color="red", label ="Predicted_values_by_model")
plt.legend()
plt.show()