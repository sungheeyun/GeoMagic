import os
from typing import Iterable

import numpy as np
from numpy import cos, ndarray, pi, sin

PROJECT_DIR = os.curdir
FIGURES_DIR = os.path.join(PROJECT_DIR, 'figures')


def angle_iter_to_unit_circil_coor_array(angle_iter: Iterable[float]) -> ndarray:
    rad_angle_array = np.array(angle_iter) * pi / 180.0
    return np.vstack((cos(rad_angle_array), sin(rad_angle_array))).T
