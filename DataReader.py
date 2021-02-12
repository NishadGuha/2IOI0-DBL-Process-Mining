import pandas as pd
import os
from sklearn.model_selection import train_test_split

# read input
dataset = input("Please enter the path of the training set (CSV file): ")
csv_train = input("Please enter the path of the training set (CSV file): ")
csv_test = input("Please enter the path of the test set (CSV file): ")
output_name = input("Please enter the name (and path) of the output file")
df_train = pd.read_csv(csv_train)
df_test = pd.read_csv(csv_test)

# combine the dataframe
frames = [df_train, df_test]
df = pd.concat(frames)

# sort by timestamp in ascending order
pd.to_datetime(df['event time:timestamp'], format = '%d-%m-%Y %H:%M:%S.%f')

# split into train set and test set (80/20)
train, test = train_test_split(df, test_size=0.2, shuffle = False)

# output
test.to_csv(output_name + ".csv")