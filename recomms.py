# Import libraries necessary for this project
import numpy as np
import pandas as pd

# start specifying some data types
# TODO: specify all dtypes


# Load the data sets
try:
    data_train = pd.read_csv("train_ver2.csv")
    data_test = pd.read_csv("test_ver2.csv")
    print "Santander Product Recommendation dataset has {} samples with {} features each.".format(*data_train.shape)
except:
    print "Dataset could not be loaded. Is the dataset missing?"

print data_train.head(30)
