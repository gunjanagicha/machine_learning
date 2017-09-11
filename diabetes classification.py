# https://archive.ics.uci.edu/ml/datasets/pima+indians+diabetes 
import pandas as pd
import numpy as np
from sklearn import model_selection, neighbors

df= pd.read_csv('dataset/prima-indians-diabetes.txt')

x= np.array(df.drop(['Class variable'],1))
y= np.array(df['Class variable'])

x_train, x_test, y_train, y_test= model_selection.train_test_split(x,y,test_size=0.2)

clf=neighbors.KNeighborsClassifier()
clf.fit(x_train, y_train)

accuracy=clf.score(x_test,y_test)
print(accuracy)
#0.74025974026
