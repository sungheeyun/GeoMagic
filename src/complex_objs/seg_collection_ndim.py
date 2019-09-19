from typing import Iterable, Union, List, Optional

from matplotlib.axes import Axes

from atoms.geo_object_ndim import GeoObjectNDim
from atoms.segment_ndim import SegmentNDim
from atoms.directed_segment_ndim import DirectedSegmentNDim


class SegCollectionNDim(GeoObjectNDim):
    """
    Implements n-dimensional object consisting of segments.
    """

    def __init__(self, ndim: int, coor_array: Iterable[Iterable[Union[float, int]]]):
        self.ndim: int = ndim
        self.segment_ndim_list: List[SegmentNDim] = list()

        self.add_segments(coor_array)

    def add_segments(self, coor_array: Iterable[Iterable[Union[float, int]]]) -> None:
        for coordinate in coor_array:
            if len(coordinate) != self.get_num_dimensions():
                raise Exception(
                    f"The coordinate should consist of {self.get_num_dimensions()} numbers; we got {coor_array}!"
                )

        for idx in range(len(coor_array) - 1):
            self.segment_ndim_list.append(DirectedSegmentNDim(coor_array[idx], coor_array[idx + 1]))

    def get_name(self) -> str:
        return f"{self.get_num_dimensions()}-D segment collection"

    def get_num_dimensions(self) -> Optional[int]:
        return self.ndim

    def draw3d(self, axis: Axes, **kwargs):
        if self.get_num_dimensions() != 3:
            raise Exception(f"The dimension should be 3; it's {self.get_num_dimensions()}")

        for segment in self.segment_ndim_list:
            segment.draw3d(axis, **kwargs)