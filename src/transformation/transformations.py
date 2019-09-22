from typing import Union

from numpy import ndarray

from atoms.directed_line_segment_ndim import DirectedLineSegmentNDim
from transformation.transformer_base import TransformerBase
from transformation.shifting import Shifting
from transformation.composite_transformer import CompositeTransformer
from transformation.rotation import Rotation


def get_3d_rotaiton_around_segment(angle: Union[float, int], axis: DirectedLineSegmentNDim) -> TransformerBase:

    axis_point_1: ndarray = axis.point_1
    axis_point_2: ndarray = axis.point_2

    return CompositeTransformer((
        Shifting(-axis_point_1),
        Rotation(angle, [axis_point_2 - axis_point_1]),
        Shifting(axis_point_1)
    ))
