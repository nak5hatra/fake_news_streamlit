import sys
import os
import pandas as pd
import numpy as np
import pickle
from fake_news_classification.exception.exception import NewsException


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

def save_npz(file_path: str, array):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_object:
            np.savez(file_object, array)
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