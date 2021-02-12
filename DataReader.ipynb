# This cell should be run. It will ask to give the path of the dataset as input and a name for the output file. Since the dataset is included in the same foler, the filename as 
# BPI_2012.csv can be given. The output will contain the predictions results for both prediction model 1 and model 2 as a column in the stored csv file.

import pandas as pd
import os
from sklearn.model_selection import train_test_split
from scipy.stats import mode
import operator
import functools
import datetime 

def process_data():
    # Read input
    dataset = input("Please enter the path of the CSV file: ")
    output_name = input("Please enter the name (and path) of the output file: ")
    df = pd.read_csv(dataset)

    # Parse the timestamp and convert it into y-m-d form
    df['event time:timestamp'] = pd.to_datetime(df['event time:timestamp'], format = '%d-%m-%Y %H:%M:%S.%f')

    # Sort data by timestamp in ascending order
    df.sort_values(['event time:timestamp'], axis=0, inplace=True)
    
    # split into train set and test set (80/20)
    df_train, df_test = train_test_split(df, test_size=0.2, shuffle = False)

    # Reset index
    df_train.reset_index(drop=True, inplace=True)
    df_test.reset_index(drop=True, inplace=True)

    return (df_train, df_test, output_name)


def make_pred(df_train, df_test):
    
    '''Parameters: df_train: training set
                   df_test: test set           '''

    
    # Assign position number to each event
    df_sort = df_train.set_index(df_train.groupby('case concept:name').cumcount(), append = True)
    df_sort = df_sort.reset_index()
    df_sort2 = df_sort[["level_1", "event concept:name"]]

    # Find the most frequent event in each position using mode
    df_new = df_sort2.groupby('level_1')['event concept:name'].apply(lambda x: mode(x)[0][0]).reset_index()
    df_new = df_new.rename(columns={'level_1':'position', 'event concept:name':'Predicted event'})


    df_sort = df_sort.set_index(df_sort.groupby('case concept:name').cumcount(), append = True)
    df_sorted = df_sort.sort_values(['case concept:name','level_1'])#reset_index()

    # Calculating Expected Time
    correct = {}
    temp = []
    previous = []
    for count,row in df_sorted.iterrows():
        
        i = row["level_1"];   
        if i == 0:
                temp = row["case REG_DATE"]
                if len(temp) == 25:
                    part1,part2 = temp.split("+")
                    part1 = part1 + ".000+"
                    temp = part1+part2

                temp = temp.replace("T"," ")
                temp,_ = temp.split("+")
                date_time_obj = datetime.datetime.strptime(temp, '%Y-%m-%d %H:%M:%S.%f')
                calc  = row["event time:timestamp"] - date_time_obj
        if i != 0:
                calc  = row["event time:timestamp"] - previous["event time:timestamp"]
        if i in correct:
                    correct[i].append(calc)
        else:
                    correct[i] = [calc]
        previous = row

    actual = []
    for key in correct:
            actual.append(str(functools.reduce(operator.add, correct[key])/len(correct[key])))
    actual
    df_new["Expected time"] = actual

    return df_new

def save_results(output_name):
    result.to_csv(output_name + ".csv")

df_train, df_test, output_name = process_data()
result = make_pred(df_train, df_test)
save_results(output_name)
