import sklearn
import pickle
import numpy as np
path_train_word = '/home/molin/Documents/TensorFlow_RLRE/cnndata/selected_word.npy'
word = np.load(path_train_word, allow_pickle=True)
print(word)
