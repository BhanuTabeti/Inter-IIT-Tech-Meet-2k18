import pickle
# import csv
import numpy as np
# datafile = open('X.csv', 'r')
# Data Set
# datareader = csv.reader(datafile, delimiter=';')
X = []
# for row in datareader:
#     myarray = np.fromstring(row, dtype=float, sep=',')
#     # dat2 = []
#     # for col in row:
#     # 	dat2.append(float(line.strip())l)
#     #  	pass 
#     X.append(row)
with open("X.csv") as f:
	lis=[list(map(np.float64,x.split(","))) for x in f]
	X.append(lis)
# import numpy as np
# with open('X.csv') as f:
#     lines=f.readlines()
#     for line in lines:
#         myarray = np.fromstring(line, dtype=float, sep=',')
#         # print(myarray)
#         X.append(myarray)
# print(X[0])
# # # y = ['You','',,'asa']
y = []
with open('Y.dat') as inputfile:
	for line in inputfile:
		d = line.strip()
		y.append(d)

print(y)
# y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# Importing Library
from sklearn.neighbors import KNeighborsClassifier
# Making Object
neigh = KNeighborsClassifier(n_neighbors=3)
# Traning Data
neigh.fit(X, y)
# Testing 
filename = '33_model.sav'
pickle.dump(neigh, open(filename, 'wb'))
# Printing
print('Saved to finalized_model.sav')