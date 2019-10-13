from typing import Iterable, List, Union, Tuple, Any

from matplotlib.axes import Axes

from atoms.geo_object_2d import GeoObject2D


class GeoObjectCollection2D(GeoObject2D):
    """
    Implements GeoObject2D collection.
    """

    def __init__(self, geo_object_2d_iter: Iterable[GeoObject2D]):
        self.geo_object_2d_list: List[GeoObject2D] = list(geo_object_2d_iter)

    def add_object(self, geo_object_2d: GeoObject2D) -> None:
        self.geo_object_2d_list.append(geo_object_2d)

    def draw(self, axis: Axes, *args, **kwargs):
        for geo_object_2d in self.geo_object_2d_list:
            geo_object_2d.draw(axis, *args, **kwargs)

    def get_mirror_symmetry(self, first_point: Union[object, Tuple[Union[float, int], Union[float, int]]],
                            second_point: Union[object, Tuple[Union[float, int], Union[float, int]]]) -> Any:
        return GeoObjectCollection2D(
            [geo_object_2d.get_mirror_symmetry(first_point, second_point) for geo_object_2d in self.geo_object_2d_list]
        )

    def translate(self, delta: Union[object, Tuple[Union[float, int], Union[float, int]]]) -> Any:
        return GeoObjectCollection2D(
            [geo_object_2d.translate(delta) for geo_object_2d in self.geo_object_2d_list]
        )

    def rotate(self, angle: Union[float, int]) -> Any:
        return GeoObjectCollection2D(
            [geo_object_2d.rotate(angle) for geo_object_2d in self.geo_object_2d_list]
        )
