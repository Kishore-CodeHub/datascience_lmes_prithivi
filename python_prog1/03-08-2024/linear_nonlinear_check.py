import pandas as pd

data = pd.DataFrame({
    "flu" : [0,1,0,1,0],
    "smell" : [1,1,0,0,1],
    "fever" : [100,101.4,98,102.3,99],
    "fatigue" : [1,2,3,2,1],
    "corona" : [0,1,0,1,0]
})

covariance_matrix = data.corr()
print(covariance_matrix)

covariance_matrix = data.corr()
print(covariance_matrix["corona"])
