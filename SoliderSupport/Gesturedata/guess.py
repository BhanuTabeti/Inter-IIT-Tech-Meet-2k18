import pickle

filename = '17model.sav'
loaded_model = pickle.load(open(filename, 'rb'))


# Testing 
output = loaded_model.predict([[0, 0, 1, 1, 1, 170, 90.28571, 353.1515, -1.89313, 3.946565, -0.9923664, 253.9355, 99.15538, 330.354, -2.80916, -0.09923664, 1.152672]])
print(output[0])
# Printing Probability
print(loaded_model.predict_proba([[0, 0, 1, 1, 1, 170, 90.28571, 353.1515, -1.89313, 3.946565, -0.9923664, 253.9355, 99.15538, 330.354, -2.80916, -0.09923664, 1.152672]]))