import numpy as np

def map_value(current_min, current_max, new_min, new_max, value):
    n = (value - current_min) / (current_max - current_min)
    r = (new_max - new_min) * n + new_min
    return r

def x_rotation(vector, theta):
    new_vector = np.array([[1, 0, 0], [0, np.cos(theta), -np.sin(theta)], [0, np.sin(theta), np.cos(theta)]])
    return np.dot(new_vector, vector)


def y_rotation(vector, theta):
    new_vector = np.array([[np.cos(theta), 0, np.sin(theta)], [0, 1, 0], [-np.sin(theta), 0, np.cos(theta)]])
    return np.dot(new_vector, vector)


def z_rotation(vector, theta):
    new_vector = np.array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]])
    return np.dot(new_vector, vector)
