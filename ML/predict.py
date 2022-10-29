
import numpy as np
import pickle

with open('model.pkl', 'rb') as f:
    clf = pickle.load(f)

sample1 = [0.2 ,0.2 ,0.2 ,0.2 ,0.2 ,0 ,0 ,0 ,0.5 ,0.5]
sample2 = [0 ,0 ,0 ,0.5 ,0.5, 0.2 ,0.2 ,0.2 ,0.2 ,0.2]

pred = clf.predict(np.array([sample1, sample2]))
print(f'prediction:{pred}')