from typing import Union

from numpy import ndarray

from atoms.directed_line_segment_ndim import DirectedLineSegmentNDim
from transformation.shifting import Shifting
from transformation.composite_transformer import CompositeTransformation
from transformation.rotation_around_subspace_axis import RotationAroundSubspaceAxis


class RotationAround3dSegment(CompositeTransformation):
    """
    Implements 3-D rotation around an axis represented by a DirectedLineSegmentNDim.
    """

    def __init__(self, angle: Union[float, int], axis: DirectedLineSegmentNDim):
        axis_point_1: ndarray = axis.point_1
        axis_point_2: ndarray = axis.point_2

        super(RotationAround3dSegment, self).__init__(
            (
                Shifting(-axis_point_1),
                RotationAroundSubspaceAxis(angle, [axis_point_2 - axis_point_1]),
                Shifting(axis_point_1),
            )
        )
