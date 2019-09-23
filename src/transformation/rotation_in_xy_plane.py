from typing import Union

from numpy import pi, cos, sin, ndarray, eye

from transformation.invertible_unitary_transformation import InvertibleUnitaryTransformation


class RotationInXYPlane(InvertibleUnitaryTransformation):
    """
    Implements a rotation transformation in xy-plane.
    """

    def __init__(self, angle: Union[float, int], num_dimensions: int):
        if num_dimensions < 2:
            raise Exception(f"num_dimensions should be at least 2; it's {num_dimensions}")

        self.angle: float = float(angle)

        angle_rad: float = self.angle * pi / 180.0
        cos_value: float = cos(angle_rad)
        sin_value: float = sin(angle_rad)

        xy_plane_rotation_array: ndarray = eye(num_dimensions)
        xy_plane_rotation_array[0, 0] = cos_value
        xy_plane_rotation_array[0, 1] = -sin_value
        xy_plane_rotation_array[1, 0] = sin_value
        xy_plane_rotation_array[1, 1] = cos_value

        super(RotationInXYPlane, self).__init__(xy_plane_rotation_array)
