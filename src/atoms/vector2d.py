from typing import Iterable, Tuple, Union

from matplotlib.patches import Patch
from numpy import arctan2, array, cos, ndarray, pi, sin, vstack
from numpy.linalg import norm

from atoms.geo_object_2d import GeoObject2D


class Vector2D(GeoObject2D):
    """
    Implements a vector in n-dimensional space.
    """

    def translate(self, delta: Union[object, Tuple[Union[float, int], Union[float, int]]]) -> object:
        delta_vec: Vector2D = Vector2D(delta)
        return self + delta_vec

    def rotate(self, angle: Union[float, int]) -> GeoObject2D:
        x, y = self.coordinate
        angle_rad: float = float(angle) * pi / 180.0

        return Vector2D((cos(angle_rad) * x - sin(angle_rad) * y, sin(angle_rad) * x + cos(angle_rad) * y))

    def get_name(self) -> str:
        aa = ', '.join([f'{x:.2f}' for x in self.coordinate])
        return f'Vector2D({aa})'

    def get_mirror_symmetry(
            self,
            first_point: Union[object, Tuple[Union[float, int], Union[float, int]]],
            second_point: Union[object, Tuple[Union[float, int], Union[float, int]]]
    ) -> object:
        first_point: Vector2D = Vector2D(first_point)
        second_point: Vector2D = Vector2D(second_point)

        delta_vector: Vector2D = second_point - first_point
        delta_angle_rad = arctan2(*delta_vector.coordinate[::-1])

        shifted_point: Vector2D = self - first_point
        rotated_point: Vector2D = shifted_point.rotate(- delta_angle_rad * 180. / pi)
        upside_down_point: Vector2D = Vector2D((rotated_point.coordinate[0], -rotated_point.coordinate[1]))
        rotated_back_point: Vector2D = upside_down_point.rotate(delta_angle_rad * 180. / pi)
        shifted_back_point: Vector2D = rotated_back_point + first_point

        return shifted_back_point

    def draw(self, ax) -> Patch:
        assert False

    def __init__(self, coordinate_or_point: Union[Iterable[float], object]):
        if isinstance(coordinate_or_point, Vector2D):
            coordinate = coordinate_or_point.coordinate
        else:
            coordinate = coordinate_or_point

        self.coordinate: ndarray = array(coordinate)

        if self.coordinate.ndim != 1:
            raise Exception(
                f"The dimension of the array representing a Vector2D should be 1; it is {self.coordinate.ndim}!"
            )

    def get_dimension(self) -> int:
        return len(self.coordinate)

    def norm(self, *pargs, **kwargs) -> float:
        return norm(self.coordinate, *pargs, **kwargs)

    def __neg__(self) -> object:
        return Vector2D(-self.coordinate)

    def __add__(self, other) -> object:
        other: Vector2D = Vector2D(other)
        return Vector2D(self.coordinate + other.coordinate)

    def __sub__(self, other) -> object:
        other: Vector2D = Vector2D(other)
        return self + (-other)

    def __repr__(self) -> str:
        return self.get_name()

    @classmethod
    def get_2d_array_from_vectors(cls, vector_iter: Iterable[object]) -> ndarray:
        vector_iter: Iterable[Vector2D] = vector_iter
        return vstack([vector.coordinate for vector in vector_iter])
