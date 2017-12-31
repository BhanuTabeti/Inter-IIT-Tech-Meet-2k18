import pickle

filename = '33_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))


# Testing 
output = loaded_model.predict([[2110, 4095, 4095, 4095, 4095, 113.9911, 112.1776, 42.40707, -37.54199, 29.28244, -250.1374, 229.699, 119.2348, 326.3524, -2.587786, 0.09923664, -7.931298]])
print(output[0])
# Printing Probability
print(loaded_model.predict_proba([[2110, 4095, 4095, 4095, 4095, 113.9911, 112.1776, 42.40707, -37.54199, 29.28244, -250.1374, 229.699, 119.2348, 326.3524, -2.587786, 0.09923664, -7.931298]]))