import numpy as np

def get_metrics(real, pred):
    if len(real) != len(pred):
        print('error! arrays of unequal size')
        quit()

    real = np.array(real.reset_index(drop=True))
    pred = np.array(pred.reset_index(drop=True))

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
