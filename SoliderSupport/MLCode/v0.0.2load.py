import pickle

filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Testing 
output = loaded_model.predict([[147.08,225.45,147.49]])
print(output[0])
# Printing Probability
print(loaded_model.predict_proba([[147.08,225.45,147.49]]))