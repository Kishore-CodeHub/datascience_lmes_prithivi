import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

data = pd.read_csv("housing.csv")
print(data.head(5))
print(data.tail(5))

mean_imputer = SimpleImputer(strategy="mean")
data['latitude'] = mean_imputer.fit_transform(data[['latitude']])
print(data)

#Various strategy which we can use for
#strategy="median"
#strategy="most_frequent"
#strategy="constant"