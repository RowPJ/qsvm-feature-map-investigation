import numpy as np

# These are implemented from the suzuki2020.pdf paper
def data_map_one(parameters):
    "xi->xi, xj-xj, (xi,xj)->pi*xi*xj"
    # case for xi and xj individually
    if len(parameters) == 1:
        return parameters[0]
    # case for xi, xj pair
    xi = parameters[0]
    xj = parameters[1]
    return np.pi * xi * xj
def data_map_two(parameters):
    "xi->xi, xj-xj, (xi,xj)->(pi/2)(1-xi)(1-xj)"
    if len(parameters) == 1:
        return parameters[0]
    xi = parameters[0]
    xj = parameters[1]
    return (np.pi/2) * (1-xi) * (1-xj)
def data_map_three(parameters):
    "xi->xi, xj-xj, (xi,xj)->exp((|xi-xj|^2) / (8/ln(pi))"
    if len(parameters) == 1:
        return parameters[0]
    xi = parameters[0]
    xj = parameters[1]
    return np.exp(((xi-xj)*(xi-xj)) / (8/np.log(np.pi))) # numpy log is to base e
def data_map_four(parameters):
    "xi->xi, xj-xj, (xi,xj)->pi/(3cos(xi)cos(xj))"
    if len(parameters) == 1:
        return parameters[0]
    xi = parameters[0]
    xj = parameters[1]
    return np.pi/(3*np.cos(xi)*np.cos(xj)) # numpy trig functions use radians
def data_map_five(parameters):
    "xi->xi, xj-xj, (xi,xj)->(pi)cos(xi)cos(xj)"
    if len(parameters) == 1:
        return parameters[0]
    xi = parameters[0]
    xj = parameters[1]
    return np.pi * np.cos(xi) * np.cos(xj)
