import numpy as np

def _entropy(y):
    """
    Helper: Compute Shannon entropy (base 2) for labels y.
    """
    y = np.asarray(y)
    if y.size == 0:
        return 0.0
    vals, counts = np.unique(y, return_counts=True)
    p = counts / counts.sum()
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum()) if p.size else 0.0

def information_gain(y, split_mask):
    """
    Compute Information Gain of a binary split on labels y.
    Use the _entropy() helper above.
    """
    y = np.asarray(y)
    split_mask = np.asarray(split_mask, dtype=bool)
    
    if y.size == 0:
        return 0.0
        
    parent_entropy = _entropy(y)
    
    # Split the target values using the boolean mask
    left_y = y[split_mask]
    right_y = y[~split_mask]
    
    # Compute the proportions for the weighted average
    w_left = left_y.size / y.size
    w_right = right_y.size / y.size
    
    # Calculate the weighted children entropy
    children_entropy = (w_left * _entropy(left_y)) + (w_right * _entropy(right_y))
    
    return parent_entropy - children_entropy