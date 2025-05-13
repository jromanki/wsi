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

    def _find_most_common(y):
        counts = Counter(y)
        most_common = counts.most_common(1)
        return most_common[0][0]

    def _id3(self, X, y, features):
        # if all samples have same class
        if len(np.unique(y)) == 1:
            return y[0]
        
        # If no features left return most common
        if len(features) == 0:
            return self._find_most_common(y)
        
        best_feature = None
        best_gain = -1 # impossible gain
        best_value = None
        
        for feature in features:
            for value in np.unique(X[:, feature]):
                gain = self._information_gain(X[:, feature], y, value)
                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature
                    best_value = value
        
        if best_gain == 0:  # No gain possible
            return self._find_most_common(y)
        
        # Split the data
        left_mask = X[:, best_feature] == best_value
        right_mask = ~left_mask
        
        
        new_features = features.copy()
        new_features.remove(best_feature)
        
        # recursively build subtrees
        left_subtree = self._id3(X[left_mask], y[left_mask], new_features)
        right_subtree = self._id3(X[right_mask], y[right_mask], new_features)
        
        return {
            'feature': best_feature,
            'value': best_value,
            'left': left_subtree,
            'right': right_subtree
        }

    def fit(self, X, y):
        """
        Fit the Random Forest to the given data.
        X: pandas DataFrame (features)
        y: pandas Series (integer class labels)
        """
        X = np.array(X.reset_index(drop=True))
        y = np.array(y.reset_index(drop=True))
        
        n_samples, n_features = X.shape
        self.trees = []
        
        for _ in range(self.n_estimators):
            # For each tree get random  samples of X and y
            # Each sample set is slightly different becaudse of replace=True
            indices = np.random.choice(n_samples, n_samples, replace=True)
            X_sample = X[indices]
            y_sample = y[indices]
            
            features = range(n_features) # indexing features
            
            # Build tree using ID3
            tree = self._id3(X_sample, y_sample, features)
            self.trees.append(tree)
    
    def predict(self, X):
        """
        Predict class for each row of X using majority voting
        X: pandas DataFrame (features)
        Returns: numpy array of predicted integer class labels
        """
        pass