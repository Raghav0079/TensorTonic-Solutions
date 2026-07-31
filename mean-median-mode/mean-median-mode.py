import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    arr = np.array(x, dtype=float)
    
    mean_val = float(np.mean(arr))
    median_val = float(np.median(arr))
    
    counts = Counter(x)
    max_freq = max(counts.values())
    modes = [k for k, v in counts.items() if v == max_freq]
    mode_val = sorted(modes)[0]
    
    return mean_val, median_val, mode_val