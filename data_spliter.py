import pandas as pd

train_df = pd.read_csv('./dataset/NYC/NYC_train.csv')
test_df = pd.read_csv('./dataset/NYC/NYC_test.csv')
val_df = pd.read_csv('./dataset/NYC/NYC_val.csv')

n_train = train_df.shape[0]
n_val = val_df.shape[0]

train_df.loc[:n_train-n_val].to_csv('./dataset/NYC/NYC_train_new.csv')
train_df.loc[n_train-n_val:].to_csv('./dataset/NYC/NYC_val_new.csv')
pd.concat([val_df, test_df]).to_csv('./dataset/NYC/NYC_test_new.csv')