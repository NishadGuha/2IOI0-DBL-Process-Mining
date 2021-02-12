import pandas as pd
import os
from sklearn.model_selection import train_test_split

# Read input
dataset = input("Please enter the path of the CSV file: ")
output_name = input("Please enter the name (and path) of the output file: ")
df = pd.read_csv(dataset)

#csv_train = input("Please enter the path of the training set (CSV file): ")
#csv_test = input("Please enter the path of the test set (CSV file): ")
#df_train = pd.read_csv(csv_train)
#df_test = pd.read_csv(csv_test)

# Combine the dataframe
#frames = [df_train, df_test]
#df = pd.concat(frames)
#df = df.reset_index(drop=True, inplace=True)

# Parse the timestamp and convert it into y-m-d form
df['event time:timestamp'] = pd.to_datetime(df['event time:timestamp'], format = '%d-%m-%Y %H:%M:%S.%f')

# Sort data by timestamp in ascending order
df.sort_values(['event time:timestamp'], axis=0, inplace=True)

# split into train set and test set (80/20)
df_train, df_test = train_test_split(df, test_size=0.2, shuffle = False)

# Reset index
df_train.reset_index(drop=True, inplace=True)
df_test.reset_index(drop=True, inplace=True)

# Assign position number to each event
df_sort = df.set_index(df.groupby('case concept:name').cumcount(), append = True)

# Calculate the most common activity at each position
#df_new = df_sort.groupby(level=1)["event concept:name"].transform(lambda x: x.value_counts().index[0])
#df_new = df_new.to_frame()
#df_new = df_new.rename(columns = {'event concept:name' : "common activity"})

# Append to a new column
#df_sort = df_sort.join(df_new["common activity"])

def make_event_pred(df_train, df_test):

    '''Parameters: df_train: training set
                   df_test: test set
                   
       We can change to csv as input and making the sets or create a different function for it'''
    preds = pd.DataFrame() # we can return this df in order to et only the predictions for accuracy scores
    
    df_sort = df_train.set_index(df_train.groupby('case concept:name').cumcount(), append = True)
    df_new = df_sort.groupby(level=1)["event concept:name"].transform(lambda x: x.value_counts().index[0])
    df_new = df_new.to_frame()
    common_acts = df_new.rename(columns = {'event concept:name' : "common activity"})
    
    test = df_test.set_index(df_test.groupby('case concept:name').cumcount(), append = True)
    
    # Here we can implement the average time to add later in the dataframe
    test = test.rename(columns = {'event time:timestamp' : "timestamp"})
    test['timestamp'] = pd.to_datetime(test.timestamp) 
    
    
    max_list = common_acts.groupby(level=1).apply(max).copy() # Get process with max(N) for predictions
    
    for i, df in test.groupby('case concept:name'):
        length = len(df)
        test = test.append({'case concept:name':int(i),
                            'event concept:name': max_list.loc[length, 'common activity']}, ignore_index=True)
                            #'timestamp': dt.datetime(2012, 2, 14, 23, 59, 59)}, ignore_index=True)
                            # here we can add the time of the added new event
                
        preds = preds.append({'case concept:name':int(i),
                            'event concept:name': max_list.loc[length, 'common activity']}, ignore_index=True)
                            #'timestamp': dt.datetime(2012, 2, 14, 23, 59, 59)}, ignore_index=True) 
            
    test = test.set_index(test.groupby('case concept:name').cumcount(), append = True)
    
    # Depending on how we want it we should sort: test = test.sort_values(time, case name, etc.)
    test = test.sort_values('timestamp') # now sorted by time
    
    return preds #test

result = make_event_pred(df_train, df_test)

# Save the output
result.to_csv(output_name + ".csv")