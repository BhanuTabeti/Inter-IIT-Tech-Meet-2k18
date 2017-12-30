import pickle

filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))


# Testing 
output = loaded_model.predict([[1, 0, 1, 1, 1, 328.8553, 77.08623, 352.12, -6.022901, 1.89313, -2.274809, 245.2188, 104.6553, 330.1744, -3.427481, 1.587786, 1.641221]])
print(output[0])
# Printing Probability
print(loaded_model.predict_proba([[1, 0, 1, 1, 1, 328.8553, 77.08623, 352.12, -6.022901, 1.89313, -2.274809, 245.2188, 104.6553, 330.1744, -3.427481, 1.587786, 1.641221]]))