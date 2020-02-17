#!/usr/bin/env python3

import numpy as np
from scipy.io import loadmat

def load_data(filename, verbose=True):
    # Loading the data from the E-Coli Matrix and then extracting data for their respective types.
    print(f"Loading dataset: {filename}...")
    data = loadmat(filename)
    x_train_np = data['xTrain']
    y_train_np = data['yTrain']
    x_test_np = data['xTest']
    y_test_np = data['yTest']

    if verbose:
        print("\nSome information about the given data:")
        print(x_train_np.shape[0],"total training samples having",x_train_np.shape[1],"features each")
        print(x_test_np.shape[0],"total testing samples having",x_test_np.shape[1],"features each")

    # Converting the numpy arrays in raw python dictionaries for training data
    x_train_list = [list(x) for x in x_train_np]
    x_train = [{'feature_' + str(n+1):v for n,v in enumerate(x)} for x in x_train_list ]
    y_train = ['class_' + str(el) for el in y_train_np.reshape(-1)]

    # Converting the numpy arrays in raw python dictionaries for testing data
    x_test_list = [list(x) for x in x_test_np]
    x_test = [{'feature_' + str(n+1):v for n,v in enumerate(x)} for x in x_test_list ]
    y_test = ['class_' + str(el) for el in y_test_np.reshape(-1)]

    return x_train, y_train, x_test, y_test

def assess_accuracy(filename, pred):
    print(f"Loading dataset: {filename}...")
    data = loadmat(filename)
    x_test_np = data['xTest']
    y_test_np = data['yTest']

    nb = np.array(pred)
    _, cor_count = np.unique(y_test_np.reshape(-1) == nb, return_counts=True)
    pred_inc, pred_cor = tuple(cor_count)
    print ('Accuracy:', pred_cor/(pred_cor+pred_inc))
    print("\n")

    for label in range(1, 6):
        _, pred_count = np.unique(nb == label, return_counts=True)
        pred_neg, pred_pos = tuple(pred_count)
        truth = y_test_np.reshape(-1) == label
        _, cond_count = np.unique(y_test_np.reshape(-1) == label, return_counts=True)
        cond_neg, cond_pos = tuple(cond_count)
        true_pos = np.unique(np.logical_and(nb == label, y_test_np.reshape(-1) == label), return_counts=True)[1][1]
        print ("Class", label)
        print ('Prediction positive:', pred_pos)
        print ('Condition positive:', cond_pos)
        print ('True positive:', true_pos)
        print ('Precision:', true_pos/pred_pos)
        print ('Recall:', true_pos/cond_pos)
        print ('\n')

# eof
