from typing import Iterable, Union, List, Optional
from copy import deepcopy

from matplotlib.axes import Axes

from atoms.geo_object_ndim import GeoObjectNDim
from atoms.line_segment_ndim import LineSegmentNDim
from atoms.box_ndim import BoxNDim
from transformation.transformation_base import TransformationBase


class LineSegmentNDimCollection(GeoObjectNDim):
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

    def get_smallest_containing_box(self) -> BoxNDim:
        return sum([segment_ndim.get_smallest_containing_box() for segment_ndim in self.segment_ndim_list])

    def draw2d(self, axis: Axes, **kwargs):
        for segment in self.segment_ndim_list:
            segment.draw2d(axis, **kwargs)

    def draw3d(self, axis: Axes, **kwargs):
        for segment in self.segment_ndim_list:
            segment.draw3d(axis, **kwargs)

    def apply_transformation(self, transformer: TransformationBase) -> GeoObjectNDim:
        seg_collection_ndim: LineSegmentNDimCollection = LineSegmentNDimCollection(self.get_num_dimensions())

        for segment_ndim in self.segment_ndim_list:
            seg_collection_ndim.segment_ndim_list.append(segment_ndim.apply_transformation(transformer))

        return seg_collection_ndim

    def __add__(self, other: GeoObjectNDim) -> GeoObjectNDim:
        """
        Combine two LineSegmentNDimCollection's into one LineSegmentNDimCollection.
        """
        if not (self.get_num_dimensions() == other.get_num_dimensions()):
            except_msg_1: str = "The dimensions of the two objects should be the same to be summed;"
            except_msg_2: str = f"they are {self.get_num_dimensions()} and {other.get_num_dimensions()}."
            raise Exception(f"{except_msg_1} {except_msg_2}")

        seg_collection_ndim_summed: LineSegmentNDimCollection = deepcopy(self)

        for segment_ndim in other.segment_ndim_list:
            seg_collection_ndim_summed.segment_ndim_list.append(deepcopy(segment_ndim))

        return seg_collection_ndim_summed
