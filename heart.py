import pandas as pd
import numpy as np



train_lbl = pd.read_csv('train_labels.csv',header=0)
train_val = pd.read_csv('train_values.csv',header=0)


print(train_val.head(15))