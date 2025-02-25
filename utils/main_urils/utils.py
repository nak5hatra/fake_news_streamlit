import sys
import os
import pandas as pd
import numpy as np
import pickle
from fake_news_classification.exception.exception import NewsException
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score


def read_data(file_path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        raise NewsException(e, sys)
    
def save_npy(file_path: str, array):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_object:
            np.save(file_object, array)
    except Exception as e:
        raise NewsException(e, sys)

def load_files(file_path):
    try:
        data = np.load(file_path, allow_pickle=True)
        return data
    except Exception as e:
        raise NewsException(e, sys)
    

def save_models(file_path: str, model):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as model_object:
            pickle.dump(model, model_object)
    except Exception as e:
        raise NewsException(e, sys)
    
def evaluate_model(y_true, y_pred):
    print(f"F1_score: {f1_score(y_true=y_true, y_pred=y_pred)}")
    print(f"Recall_score: {recall_score(y_true=y_true, y_pred=y_pred)}")
    print(f"Precision_score: {precision_score(y_true=y_true, y_pred=y_pred)}")
    print(f"Accuracy_score: {accuracy_score(y_true=y_true, y_pred=y_pred)}")