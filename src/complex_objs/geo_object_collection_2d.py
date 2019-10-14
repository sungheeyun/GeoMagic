from typing import Iterable, List, Union, Tuple, Any
from logging import Logger, getLogger

from matplotlib.axes import Axes

from atoms.geo_object_2d import GeoObject2D
from atoms.line_segment_2d import LineSegment2D
from atoms.box_ndim import BoxNDim

logger: Logger = getLogger('geomagic')


class GeoObjectCollection2D(GeoObject2D):
    """
    Implements GeoObject2D collection.
    TODO Change the name of this class to GeoObject2DCollection AND the name of this file accordingly.
    """

    def __init__(self, geo_object_2d_iter: Iterable[GeoObject2D]):
        self.geo_object_2d_list: List[GeoObject2D] = list(geo_object_2d_iter)

    def get_name(self) -> str:
        return "GeoObjectCollection2D"

    def add_object(self, geo_object_2d: GeoObject2D) -> None:
        self.geo_object_2d_list.append(geo_object_2d)

    def draw(self, axis: Axes, *args, **kwargs):
        LineSegment2D
        for geo_object_2d in self.geo_object_2d_list:
            logger.debug(geo_object_2d.__class__)
            logger.debug(geo_object_2d.vertex_coor_array)
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

    def get_smallest_containing_box(self) -> BoxNDim:
        return sum([geo_object_2d.get_smallest_containing_box() for geo_object_2d in self.geo_object_2d_list])
