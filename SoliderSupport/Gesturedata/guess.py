import pickle

filename = '17model.sav'
loaded_model = pickle.load(open(filename, 'rb'))


# Testing 
output = loaded_model.predict([[1, 0, 1, 1, 0, 352.23, 200.00, 247.99, 0, 0, 0, 250, 111.11, 46.5, 0, 0, 0]])
print(output[0])
# Printing Probability
print(loaded_model.predict_proba([[1, 0, 1, 1, 0, 352.23, 200.00, 247.99, 0, 0, 0, 250, 111.11, 46.5, 0, 0, 0]]))