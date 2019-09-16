from typing import Iterable, List

from matplotlib.axes import Axes

from atoms.geo_object_2d import GeoObject2D


class GeoObjectCollection2D:
    """
    Implements 2D object collection.
    """

    def __init__(self, geo_object_2d_iter: Iterable[GeoObject2D]):
        self.geo_object_2d_list: List[GeoObject2D] = list(geo_object_2d_iter)

    def add_object(self, geo_object_2d: GeoObject2D) -> None:
        self.geo_object_2d_list.append(geo_object_2d)

    def draw(self, axis: Axes, *args, **kwargs):
        for geo_object_2d in self.geo_object_2d_list:
            geo_object_2d.draw(axis, *args, **kwargs)
