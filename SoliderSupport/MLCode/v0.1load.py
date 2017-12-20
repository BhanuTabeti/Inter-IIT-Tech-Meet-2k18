import pickle

filename = '10_GestureModel.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# a = input()
# print(a)
# Testing 
output = loaded_model.predict([[1,1,1,1,1,15.26,72,8.29,200.72,241.56,191]])
print(output[0])
# Printing Probabilitysc
# print(loaded_model.predict_proba([[1,1,1,1,1,333.12,88.07,359.02,240.14,228.08,237.41]]))