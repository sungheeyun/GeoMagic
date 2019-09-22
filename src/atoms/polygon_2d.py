from typing import Iterable, List, Tuple, Union

import matplotlib.patches as mp
import numpy as np
from matplotlib.axes import Axes
from numpy import arctan2, cos, ndarray, pi, sin, vstack

from atoms.geo_object_2d import GeoObject2D
from atoms.vector2d import Vector2D


class Polygon(GeoObject2D):
    """
    Implements a polygon.
    """

    def __init__(self, vertex_coor_iter: Iterable[Iterable[float]]):
        self.vertex_coor_array: ndarray = np.array(vertex_coor_iter)

    def get_number_vertices(self) -> int:
        return self.vertex_coor_array.shape[0]

    def get_name(self) -> str:
        return f"{self.vertex_coor_array.size[0]}-gon"

    def rotate(self, angle: Union[float, int]) -> GeoObject2D:
        assert False
        # XXX

    def translate(self, delta: Union[object, Tuple[Union[float, int], Union[float, int]]]) -> object:
        delta_vec: Vector2D = Vector2D(delta)
        return Polygon(vstack([(Vector2D(vertex) + delta_vec).coordinate for vertex in self.vertex_coor_array]))

    def get_mirror_symmetry(
        self,
        first_point: Union[Vector2D, Tuple[Union[float, int], Union[float, int]]],
        second_point: Union[Vector2D, Tuple[Union[float, int], Union[float, int]]],
    ) -> GeoObject2D:

        coordinate_list = list()
        for vertex in self.vertex_coor_array:
            vertex: Vector2D = Vector2D(vertex)
            coordinate_list.append(vertex.get_mirror_symmetry(first_point, second_point).coordinate)

        return Polygon(vstack(coordinate_list))

    def draw(self, ax: Axes, **kargs) -> mp.Polygon:
        dkargs = dict(fill=False)
        dkargs.update(kargs)

        polygon_patch = mp.Polygon(self.vertex_coor_array, **dkargs)
        ax.add_patch(polygon_patch)

        return polygon_patch

    @classmethod
    def get_polygon_from_edges_and_angles(
        cls,
        start_point: Union[Vector2D, Tuple[Union[float, int], Union[float, int]]],
        edge_length_iter: Iterable[float],
        angle_iter: Iterable[float],
    ) -> GeoObject2D:
        start_point: Vector2D = Vector2D(start_point)

        vector_list: List[Vector2D] = list()
        vector_list.append(start_point)

        sum_angle = 0.0
        for idx, (edge_length, angle) in enumerate(zip(edge_length_iter, angle_iter)):
            if idx != 0:
                angle = 180.0 - angle
            sum_angle += angle
            sum_angle_rad = sum_angle * pi / 180.0
            delta_vector: Vector2D = Vector2D((cos(sum_angle_rad) * edge_length, sin(sum_angle_rad) * edge_length))
            vector_list.append(vector_list[-1] + delta_vector)

        point_array_2d: ndarray = Vector2D.get_2d_array_from_vectors(vector_list)

        return Polygon(point_array_2d)

    @classmethod
    def get_polygon_from_edges_and_angles_with_two_start_points(
        cls,
        start_point_1: Union[Vector2D, Tuple[Union[float, int], Union[float, int]]],
        start_point_2: Union[Vector2D, Tuple[Union[float, int], Union[float, int]]],
        edge_length_iter: Iterable[Union[float, int]],
        angle_iter: Iterable[Union[float, int]],
    ) -> GeoObject2D:
        delta_vector: Vector2D = Vector2D(start_point_2) - start_point_1

        starting_vector_length = delta_vector.norm()
        starting_vector_angle = arctan2(*delta_vector.coordinate[::-1]) * 180.0 / pi

        return Polygon.get_polygon_from_edges_and_angles(
            start_point_1, [starting_vector_length] + list(edge_length_iter), [starting_vector_angle] + list(angle_iter)
        )
