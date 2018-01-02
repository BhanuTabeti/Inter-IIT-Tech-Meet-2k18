import pickle

filename = '33_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))


# Testing 
output = loaded_model.predict([[1631, 2929, 3027, 2582, 2757, 268.8176, 265.0323, 257.1719, -42.07633, 37.34351, -201.1527, 173.7493, 106.3623, 1.737264, 16.96947, -5.328244, -22.69466]])
print(output[0])
# Printing Probability
print(loaded_model.predict_proba([[1631, 2929, 3027, 2582, 2757, 268.8176, 265.0323, 257.1719, -42.07633, 37.34351, -201.1527, 173.7493, 106.3623, 1.737264, 16.96947, -5.328244, -22.69466],
]))