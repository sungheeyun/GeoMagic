from typing import Iterable, Union

from atoms.polygon import Polygon


class LineSegment2D(Polygon):
    def __init__(self, first_point: Iterable[Union[float, int]], second_point: Iterable[Union[float, int]]):
        super(LineSegment2D, self).__init__((first_point, second_point))
