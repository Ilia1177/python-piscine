import cv2
import numpy as np

def check_array(array):
    if not isinstance(family, list):
        raise TypeError("family must be a list")
    if not all(isinstance(row, list) for row in family):
        raise TypeError("family must be a list of lists")
    if len({len(row) for row in family}) > 1:
        raise ValueError("All rows must have the same length")

def ft_invert(array) ->  np.ndarray:
    """Inverts image colors."""
    return 255 - array

#need security check if array is grey (one channel)
def ft_red(array: np.ndarray) -> np.ndarray:
    """delete blue and green channels of received image"""
    result = array.copy()
    result[:, :, 1] = 0
    result[:, :, 2] = 0
    return result

def ft_green(array):
    """delete blue and red channels of received image"""
    result = array.copy()
    result[:, :, (0, 2)] = 0
    return result

def ft_blue(array):
    """delete red and green channels of received image"""
    result = array.copy()
    result[:, :, (0, 1)] = 0
    return result  

def ft_grey(array: np.ndarray) -> np.ndarray:
    """delete red and green channels of received image"""
    gray = cv2.cvtColor(array, cv2.COLOR_RGB2GRAY)
    return np.repeat(gray[:, :, np.newaxis], 3, axis=2)
