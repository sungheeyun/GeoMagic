from typing import Iterable, List, Tuple, Union, Any

import matplotlib.patches as mp
import numpy as np
from matplotlib.axes import Axes
from numpy import arctan2, cos, ndarray, pi, sin, vstack

from atoms.geo_object_2d import GeoObject2D
from atoms.vector2d import Vector2D
from atoms.box_ndim import BoxNDim
from exceptions.geo_magic_exception import GeoMagicException


class Polygon(GeoObject2D):
    """
    Implements a polygon.
    """

    def __init__(self, vertex_coor_iter: Iterable[Iterable[Union[float, int]]]):
        self.vertex_coor_array: ndarray = np.array(vertex_coor_iter, float)

        if self.vertex_coor_array.shape[1] != 2:
            raise GeoMagicException("Vertices should be in 2D space")

    def get_number_vertices(self) -> int:
        return self.vertex_coor_array.shape[0]

    def get_name(self) -> str:
        return f"{self.vertex_coor_array.size[0]}-gon"

    def rotate(self, angle: Union[float, int]) -> GeoObject2D:
        # TODO (1) implement Polygon.rotate
        assert False

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

    def draw(self, ax: Axes, **kwargs) -> None:
        drawing_kwargs = dict(fill=False)
        drawing_kwargs.update(kwargs)

        polygon_patch = mp.Polygon(self.vertex_coor_array, **drawing_kwargs)
        ax.add_patch(polygon_patch)

    def get_smallest_containing_box(self) -> BoxNDim:
        return BoxNDim(self.vertex_coor_array.min(axis=0), self.vertex_coor_array.max(axis=0))

    @classmethod
    def get_polygon_from_edges_and_angles(
        cls,
        start_point: Union[Vector2D, Tuple[Union[float, int], Union[float, int]]],
        edge_length_iter: Iterable[float],
        angle_iter: Iterable[float],
    ) -> Any:
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
    ) -> Any:
        delta_vector: Vector2D = Vector2D(start_point_2) - start_point_1

        starting_vector_length = delta_vector.norm()
        starting_vector_angle = arctan2(*delta_vector.coordinate[::-1]) * 180.0 / pi

        return Polygon.get_polygon_from_edges_and_angles(
            start_point_1, [starting_vector_length] + list(edge_length_iter), [starting_vector_angle] + list(angle_iter)
        )
