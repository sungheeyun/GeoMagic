from typing import Iterable
import os

from numpy import cos, ndarray, pi, sin, array, vstack, arccos
from numpy.linalg import norm

PROJECT_DIR = os.curdir
FIGURES_DIR = os.path.join(PROJECT_DIR, "figures")


def angle_iter_to_unit_circil_coor_array(angle_iter: Iterable[float]) -> ndarray:
    rad_angle_array = array(angle_iter) * pi / 180.0
    return vstack((cos(rad_angle_array), sin(rad_angle_array))).T


def outer_product_3d(array_1: ndarray, array_2: ndarray) -> ndarray:
    return array(
        (
            array_1[1] * array_2[2] - array_1[2] * array_2[1],
            array_1[2] * array_2[0] - array_1[0] * array_2[2],
            array_1[0] * array_2[1] - array_1[1] * array_2[0],
        ),
        float,
    )


def get_angle(x_array: ndarray, y_array: ndarray) -> float:
    return arccos(x_array.dot(y_array) / norm(x_array) / norm(y_array)) * 180.0 / pi
