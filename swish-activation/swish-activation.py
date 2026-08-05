import numpy as np

def swish(x, beta=1.0):
    """
    Implement Swish activation function.
    
    Parameters:
    x (numpy.ndarray or scalar): Input tensor or scalar value.
    beta (float): Parameter controlling the magnitude of the smooth transition.
    
    Returns:
    numpy.ndarray or scalar: Swish activation applied to x.

    
    """

    x = np.asarray( x , dtype = float)
    z = beta * x

    sigmoid = np.where(
        z >= 0 ,
        1 / (1 + np.exp(-z)),
        np.exp(z) / ( 1+ np.exp(z))
    )

    return x * sigmoid