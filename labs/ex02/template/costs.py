import numpy as np

def compute_loss(y, tx, w):
    """Calculate the loss using either MSE or MAE.

    Args:
        y: numpy array of shape=(N, )
        tx: numpy array of shape=(N,2)
        w: numpy array of shape=(2,). The vector of model parameters.

    Returns:
        the value of the loss (a scalar), corresponding to the input parameters w.
    """
    # ***************************************************
    # INSERT YOUR CODE HERE
    # TODO: compute loss by MSE
    N = len(y)
    Xw = tx @ w
    MSE = (1 / (2 * N) ) * np.sum((y[:] - Xw[:])**2)
    return MSE
    # ***************************************************
    #raise NotImplementedError