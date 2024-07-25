import pandas as pd
import numpy as np
import matplotlib.pyplot as mtpt
import sklearn as sl

data = pd.read_csv("housing.csv")
print(data.head(5))

# finding_null = data.isnull()
# print(finding_null)

data.fillna(2000, inplace=True)
print(data.head(5))