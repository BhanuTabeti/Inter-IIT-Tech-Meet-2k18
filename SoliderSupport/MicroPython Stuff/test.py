import pickle
import numpy as np

filename = 'np.sav'
pickle.dump(np, open(filename, 'wb'))
# Printing
print('Saved to finalized_model.sav')