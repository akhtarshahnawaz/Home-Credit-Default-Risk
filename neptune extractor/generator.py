from sklearn.externals import joblib
import os

print "Loading Files"
train_df = joblib.load('data/train_features')['features']
test_df = joblib.load('data/test_features')['features']

print "Saving Files as CSV"
train_df.to_csv("data/train.csv", index=False)
test_df.to_csv("data/test.csv", index=False)

print "Removing Raw Files"
os.remove('data/train_features')
os.remove('data/test_features')