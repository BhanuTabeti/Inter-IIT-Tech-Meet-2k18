import pickle

filename = '33_model_2.sav'
loaded_model = pickle.load(open(filename, 'rb'))
names = ['Ammunition','Breacher','Column Formation','Come','Cover This Area','Crouch','Dog','Door','Enemy','File Formation','Freeze','Gas','Hostage','Hurry Up','I Dont Understand','I Understand','Leader','Line Formation','Listen','Me','Move Up','Pistol','Point Of Entry','Rally Point','Rifle','See','Shotgun','Sniper','Stop','Vehicle','Wedge Formation','Window','You']

# val = [1423, 2674, 2407, 2065, 2177, 355.6943, 42.30696, 355.2917, -53.92366, -23.91603, 81.0458, 176.082, 106.8297, 1.077965, 6.175572, 15.29008, -27.41221],
val = [2335, 4095, 3863, 3847, 4095, 81.23892, 87.29589, 16.59894, -3.801527, 3.862595, 0.832061, 247.3043, 141.9844, 287.9246, -3.229008, 2.198473, 1.503817],




# Testing 
output = loaded_model.predict(val)
print(output[0])
# Printing Probability
proba = (loaded_model.predict_proba(val))

for x in xrange(0,len(proba[0])):
	if proba[0][x]:
		print proba[0][x], "-", names[x]
		pass
	pass