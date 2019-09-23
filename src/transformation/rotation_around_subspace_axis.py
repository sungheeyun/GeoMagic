from typing import Union, Iterable

from numpy import ndarray, array
from transformation.rotation_in_xy_plane import RotationInXYPlane
from transformation.unitary_coordinate_change_around_subspace_axis import UnitaryCoordinateChangeAroundSubspaceAxis
from transformation.composite_transformer import CompositeTransformation


class RotationAroundSubspaceAxis(CompositeTransformation):
    """
    Implements general rotation transformation in N-dimensional space.
    """

    def __init__(self, angle: Union[float, int], axis_2d_array: Iterable = ndarray((0, 2), float)):
        axis_2d_array = array(axis_2d_array, float)
        rotation_in_xy_plane: RotationInXYPlane = RotationInXYPlane(angle, axis_2d_array.shape[1])
        unitary_coordinate_change_around_subspace_axis: UnitaryCoordinateChangeAroundSubspaceAxis =\
            UnitaryCoordinateChangeAroundSubspaceAxis(axis_2d_array)

        super(RotationAroundSubspaceAxis, self).__init__(
            (
                unitary_coordinate_change_around_subspace_axis,
                rotation_in_xy_plane,
                unitary_coordinate_change_around_subspace_axis.get_inverse_transformation(),
            )
        )
