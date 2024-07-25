import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
#
# x=(1,2,3,4,5)
# y=(2,4,6,8,10)
#
# df = pd.DataFrame({"in":x,"out":y})
# sns.scatterplot(x="in",y="out",data = df)
# plt.xlabel("x data")
# plt.ylabel("y data")
# plt.grid(True)
# plt.show();

#box plot to identify least and max deviate data in the data set
np.random.seed(42)  #to generate dataset by ourselves

#any input that has mean value around 0 and std deviation around 1 is called normally distributed data

good_data = np.random.normal(size=100)
good_df = pd.DataFrame(good_data, columns=["Good_data_performance"])
print(good_df)

#here we are directly mentioning mean should be 50 (i.e-loc) and std as 5 (i.e-scale) for random data size 100

good_data = np.random.normal(loc=50, scale=5, size=100)
good_df=pd.DataFrame(good_data, columns=["Good_data_performance"])
print(good_df)

# df = pd.DataFrame(good_data, columns=["Good"])
# print(df)
#
# plt.boxplot(df["Good"], vert=False)
# plt.title("Good_data")
# plt.show()

# input_data = [0.496714, -0.138264, 0.647689, 1.523030,-0.234153]
# final = np.array(input_data)
# print(final)
#
# mean_data = final.mean()
# print(mean_data)
#
# std_data = fina

#create a bad data that means the data which is not in order

bad_data = np.random.normal(loc=50, scale=5, size=100)
print(bad_data)

bad_data=np.append(bad_data, [80,90,100])

df = pd.DataFrame(bad_data, columns=["Bad Data"])
print(df)

plt.boxplot(df["Bad Data"], vert=False)
plt.title("Bad outlier data")
plt.show()