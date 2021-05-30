#!/usr/bin/env python3

import numpy as np
import pylab as plt
import seaborn as sns

from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.metrics import classification_report

import nltk, re, json
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

#nltk.download('stopwords')
#STOPWORDS = set(stopwords.words('english'))
#st=PorterStemmer()


def plot_history(history, ax=None):
    
    if ax is None:
        (fig, ax) = plt.subplots(1,2, figsize=(12,4))
    #plt.figure(figsize=(12,4))
    #ax[0].subplot(121)
    ax[0].plot(history.history['loss'], label='Training loss')
    ax[0].plot(history.history['val_loss'], label='validation loss')
    ax[0].set_grid()
    ax[0].legend()

    ax[1].subplot(122)
    ax[1].plot(history.history['accuracy'], label='Training accuracy')
    ax[1].plot(history.history['val_accuracy'], label='validation accuracy')
    ax[1].grid()
    ax[1].legend()


def calc_prediction(model, X_test, y_test, categorical=False, ax=None, title=None):
    data_dir="./"

    with open(data_dir+"label_dict.json", 'r') as fp:
        label_dict = json.load(fp)
        labels = label_dict.keys()

    y_pred = model.predict(X_test)
    
    if categorical:
        y_pred = np.argmax(y_pred, axis=1)
        y_test = np.argmax(y_test, axis=1)
            
    report = classification_report(y_test, y_pred)

    if title: print ("Method:",title)
    print ("Classification Report:\n", report)
    print ()

    confusionmatrix=confusion_matrix( y_test, y_pred)
    if ax==None:
        (fig, ax) = plt.subplots(1,1,figsize=(6,6))
    sns.heatmap(confusionmatrix, cmap='viridis', annot=True, cbar=False, ax=ax,
            xticklabels=labels, yticklabels=labels)
    ax.set_title(title, fontsize=16)
    
#calc_prediction(model_bow, X_test_bow, y_test_bow, title="LR (BOW)")


def tpr(actual, pred):
    tp = np.sum((actual==1) & (pred == 1))
    fn = np.sum((actual==1) & (pred == 0))
    return tp/(tp+fn)

def fpr(actual, pred):
    fp = np.sum((actual == 0) & (pred == 1))
    tn = np.sum((actual == 0) & (pred == 0))
    return fp/(fp+tn)

def acc(actual, pred):
    return np.sum(actual==pred)/len(actual)
