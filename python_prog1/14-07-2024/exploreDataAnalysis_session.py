import pandas as pd
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import seaborn as sb

data = pd.read_csv("housing_eda.csv")
print(data.shape)
print(data.info())
print(data.head())

print(data.describe())

numerical_columns = data.select_dtypes(include=["float64","int64"]).columns
print(numerical_columns)

categorical_columns = data.select_dtypes(include=['object']).columns
print(categorical_columns)

imputer_object = SimpleImputer(strategy="mean")
data[numerical_columns]=imputer_object.fit_transform(data[numerical_columns])

imputer_object = SimpleImputer(strategy="most_frequent")
data[categorical_columns] = imputer_object.fit_transform(data[categorical_columns])


for columns in numerical_columns:
    plt.figure(figsize=(10,4))
    sb.histplot(data[columns], kde=True)
    plt.title(f"histogram of {columns}")
    plt.show()

for columns in numerical_columns:
    plt.figure(figsize=(10,4))
    sb.boxplot(x=data[columns])
    plt.title(f"histogram of {columns}")
    plt.show()


plt.figure(figsize=(10,4))
sb.boxplot(x=data["population"])
plt.title(f"histogram of population")
plt.show()