import numpy as np

# Finds the parameters x_0 and y_0 for the Catenary Equation
def find_param(points):

    x_naught = points[np.where(points[:, 1] == points[:, 1].min()), :][0][0][0]
    y_naught = points[:, 1].min()

    return x_naught, y_naught

def catenary(x, y0, c, x0):
    return y0 + c * (np.cosh((x - x0) / c) - 1)

# Mean Squared Error Loss function with a specific Catenary Model
def loss(c, points, x0, y0):
    y_pred = catenary(points[:, 0], y0, c, x0)
    return np.mean((points[:, 1] - y_pred) ** 2)