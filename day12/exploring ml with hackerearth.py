import pandas as pd
train  = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
train.info()

print ("The train data has",train.shape)
print ("The test data has",test.shape)

