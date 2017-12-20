import pickle

filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

a = input()
print(a)
# Testing 
output = loaded_model.predict([[a]])
print(output[0])
# Printing Probability
print(loaded_model.predict_proba([[a]]))