from typing import Tuple, Union

import numpy as np
from numpy import cos, ndarray, pi

from atoms.polygon import Polygon
from atoms.vector2d import Vector2D
from utils import angle_iter_to_unit_circil_coor_array


class RegularPolygon(Polygon):
    """
    Implements a regular polygon.

    """

    def __init__(
        self,
        num_vertices: int,
        center: Union[Vector2D, Tuple[Union[float, int], Union[float, int]]] = (0.0, 0.0),
        edge_length: Union[float, int] = 1.0,
        angle_of_one_point: Union[float, int] = 0.0,
    ):
        self.num_vertices: int = num_vertices
        self.center_coor: Vector2D = Vector2D(center)
        self.edge_length: float = float(edge_length)
        self.angle_of_one_point: float = float(angle_of_one_point)

        radius = 0.5 * self.edge_length / cos(pi * (0.5 - 1.0 / float(self.num_vertices)))

        angle_array: ndarray = np.linspace(0.0, 360.0, num=self.num_vertices, endpoint=False) + self.angle_of_one_point
        vertex_coor_array: ndarray = angle_iter_to_unit_circil_coor_array(
            angle_array
        ) * radius + self.center_coor.coordinate

        super(RegularPolygon, self).__init__(vertex_coor_array)
