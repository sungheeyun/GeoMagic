from typing import Iterable, Union, List, Optional

from matplotlib.axes import Axes

from atoms.geo_object_ndim import GeoObjectNDim
from atoms.line_segment_ndim import LineSegmentNDim
from transformation.transformer_base import TransformerBase


class SegCollectionNDim(GeoObjectNDim):
    """
    Implements n-dimensional object consisting of segments.
    """

    def __init__(self, num_dimensions: int, coor_array: Optional[Iterable[Iterable[Union[float, int]]]] = None):
        self.num_dimensions: int = num_dimensions
        self.segment_ndim_list: List[LineSegmentNDim] = list()

        if coor_array is None:
            coor_array = list()

        self.add_segments(coor_array)

    def add_segments(self, coor_array: Iterable[Iterable[Union[float, int]]]) -> None:
        for coordinate in coor_array:
            if len(coordinate) != self.get_num_dimensions():
                raise Exception(
                    f"The coordinate should consist of {self.get_num_dimensions()} numbers; we got {coor_array}!"
                )

        for idx in range(len(coor_array) - 1):
            self.segment_ndim_list.append(LineSegmentNDim(coor_array[idx], coor_array[idx + 1]))

    def get_name(self) -> str:
        return f"{self.get_num_dimensions()}-D segment collection"

    def get_num_dimensions(self) -> Optional[int]:
        return self.num_dimensions

    def draw3d(self, axis: Axes, **kwargs):
        if self.get_num_dimensions() != 3:
            raise Exception(f"The dimension should be 3; it's {self.get_num_dimensions()}")

        for segment in self.segment_ndim_list:
            segment.draw3d(axis, **kwargs)

    def apply_transformation(self, transformer: TransformerBase) -> GeoObjectNDim:
        seg_collection_ndim: SegCollectionNDim = SegCollectionNDim(self.get_num_dimensions())

        for segment_ndim in self.segment_ndim_list:
            seg_collection_ndim.segment_ndim_list.append(segment_ndim.apply_transformation(transformer))

        return seg_collection_ndim
