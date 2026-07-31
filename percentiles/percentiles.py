import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation from scratch.
    """
    x = np.asarray(x, dtype=float)
    is_scalar = np.isscalar(q)
    q = np.atleast_1d(q).astype(float)
    
    # Sort data in ascending order
    x_sorted = np.sort(x)
    n = len(x_sorted)
    
    
    indices = (q / 100.0) * (n - 1)
    
    lower_idx = np.floor(indices).astype(int)
    upper_idx = np.ceil(indices).astype(int)
    fraction = indices - lower_idx
    
    lower_idx = np.clip(lower_idx, 0, n - 1)
    upper_idx = np.clip(upper_idx, 0, n - 1)
    
    
    lower_val = x_sorted[lower_idx]
    upper_val = x_sorted[upper_idx]
    result = lower_val + fraction * (upper_val - lower_val)
    

    return result.item() if is_scalar else result