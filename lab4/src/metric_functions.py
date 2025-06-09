import numpy as np

def get_metrics(real, pred):
    real = np.array(real.reset_index(drop=True))

    if len(real) != len(pred):
        print('error! arrays of unequal size')
        quit()

    tp, tn, fp, fn = 0, 0, 0, 0
    for i in range(len(real)):
        if pred[i] == 1:
            if real[i] == 1:
                tp += 1
            else:
                fp += 1
        else: # predicted 0
            if real[i] == 0:
                tn += 1
            else:
                fn += 1
    accuracy = (tp + tn) / len(real)
    precision = tp / (tp + fp) if (tp + fp) else 0
    recall = tp / (tp + fn) if (tp + fn) else 0

    metrics = {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
    }

    return metrics

def roc_curve(y_true, y_prob):
    y_true = np.array(y_true.reset_index(drop=True))

    thresholds = np.linspace(0, 1, num=100)
    fpr = []
    tpr = []
    

    for threshold in thresholds:
        # Classify based on threshold
        y_pred = (y_prob >= threshold).astype(int)
        
        # Calculate the confusion matrix components
        tp = np.sum((y_true == 1) & (y_pred == 1))  # True Positives
        fp = np.sum((y_true == 0) & (y_pred == 1))  # False Positives
        tn = np.sum((y_true == 0) & (y_pred == 0))  # True Negatives
        fn = np.sum((y_true == 1) & (y_pred == 0))  # False Negatives
        
        # Calculate TPR (True Positive Rate) and FPR (False Positive Rate)
        tpr_value = tp / (tp + fn) if (tp + fn) > 0 else 0  # Avoid division by zero
        fpr_value = fp / (fp + tn) if (fp + tn) > 0 else 0  # Avoid division by zero
        
        # Append to lists
        fpr.append(fpr_value)
        tpr.append(tpr_value)
    
    return np.array(fpr), np.array(tpr), thresholds