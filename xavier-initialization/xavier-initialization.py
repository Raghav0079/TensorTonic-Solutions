import math

def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    # Compute the Xavier uniform bound
    limit = math.sqrt(6.0 / (fan_in + fan_out))
    
    # Map each raw weight from [0, 1] to [-limit, limit]
    # Formula: W_new = W_old * 2 * limit - limit
    scaled_W = []
    for row in W:
        scaled_row = [float(val * 2.0 * limit - limit) for val in row]
        scaled_W.append(scaled_row)
        
    return scaled_W