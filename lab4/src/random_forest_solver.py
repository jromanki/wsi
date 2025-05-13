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
    
    def _entropy(y):
        """Calculate entropy for integer class labels"""
        counts = np.bincount(y)
        probabilities = counts / len(y)
        return -np.sum([p * np.log2(p) for p in probabilities if p > 0])

    def _information_gain(self, X_col, y, value):
        # returns information gain for a specific value
        value_mask = X_col == value # True if  X_col[i] == value
        not_value_mask = ~not_value_mask
        
        n = len(y)
        n_value, n_not_value = np.sum(value_mask), np.sum(not_value_mask)
        
        if n_value == 0 or n_not_value == 0:
            return 0
        
        parent_entropy = self._entropy(y)
        child_entropy = (n_value/n) * self._entropy(y[value_mask]) + (n_not_value/n) * self._entropy(y[not_value_mask])
        return parent_entropy - child_entropy
    
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