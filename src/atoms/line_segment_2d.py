from typing import Iterable, Union
from logging import Logger, getLogger

from matplotlib.axes import Axes

from atoms.polygon import Polygon

logger: Logger = getLogger('geomagic')


class LineSegment2D(Polygon):
    """
    Implements a line segment in 2D space by inheriting

    """
    def __init__(self, first_point: Iterable[Union[float, int]], second_point: Iterable[Union[float, int]]):
        super(LineSegment2D, self).__init__((first_point, second_point))

    def draw(self, ax: Axes, **kwargs) -> None:
        logger.debug(f"self.vertex_coor_array = {self.vertex_coor_array}")
        ax.plot(self.vertex_coor_array[:, 0], self.vertex_coor_array[:, 1], **kwargs)
