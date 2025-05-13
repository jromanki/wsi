import numpy as np
import pandas as pd
from solver import Solver
from collections import Counter

class RandomForestSolver(Solver):
    """A Random Forest implementation using ID3 algorithm with majority voting"""
    
    def __init__(self, n_estimators: int = 100):
        self.n_estimators = n_estimators
        self.trees = []  # Will store our decision trees
    
    def get_parameters(self):
        return {'n_estimators': self.n_estimators}
    
    def _entropy(data):
        """Calculate entropy for integer class labels"""
        counts = np.bincount(data)
        probabilities = counts / len(data)
        return -np.sum([p * np.log2(p) for p in probabilities if p > 0])

    
    def fit(self, X, y):
        """
        Fit the Random Forest to the given data.
        X: pandas DataFrame (features)
        y: pandas Series (integer class labels)
        """
        X = np.array(X.reset_index(drop=True))
        y = np.array(y.reset_index(drop=True))
    
    def predict(self, X):
        """
        Predict class for each row of X using majority voting
        X: pandas DataFrame (features)
        Returns: numpy array of predicted integer class labels
        """
        pass