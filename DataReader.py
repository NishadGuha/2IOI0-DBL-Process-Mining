import pandas as pd
import os

#read input
csv_train = input("Please enter the path of the training set (CSV file): ")
csv_test = input("Please enter the path of the test set (CSV file): ")
output_name = input("Please enter the name (and path) of the output file")
df_train = pd.read_csv(csv_train)
df_test = pd.read_csv(csv_test)

#process
df_result = df_train

#output
df_result.to_csv(output_name + ".csv")