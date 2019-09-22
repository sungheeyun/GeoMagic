from typing import Union, Iterable, Optional

from numpy import ndarray, matrix, eye, pi, cos, sin, array, hstack
from numpy.linalg import qr
from transformation.transformer_base import TransformerBase
from utils import outer_product_3d


class Rotation(TransformerBase):
    """
    Implements general rotation transformation in N-dimensional space.
    """

    def __init__(self, angle: Union[float, int], axis_2d_array: Iterable = ndarray((0, 2), float)):
        self.angle: float = float(angle)
        self.axis_2d_array: ndarray = array(axis_2d_array, float)
        self.rotation_2d_array: matrix = None

        self._check_attr()
        self._initialize()

    def _check_attr(self):
        if self.axis_2d_array.ndim != 2:
            raise Exception(f"axis_2d_array should be a 2-D array; axis_2d_array.ndim = {self.axis_2d_array.ndim}")
        num_rows, num_cols = self.axis_2d_array.shape
        if num_cols != num_rows + 2:
            raise Exception(f"axis_2d_array should be (N-2)-by-N array; its shape is {self.axis_2d_array.shape}")

    def _initialize(self):
        # perform QR-decomposition to form an orthonormal coordinate vectors
        q_array, r_array = qr(hstack((self.axis_2d_array.T, eye(self.axis_2d_array.shape[1]))))
        orthogonal_basis_2d_array: ndarray = hstack((q_array[:, -2:], q_array[:, :-2]))

        if orthogonal_basis_2d_array.shape[0] == 3:
            vector_1: ndarray = orthogonal_basis_2d_array[:, 0].copy()
            vector_2: ndarray = orthogonal_basis_2d_array[:, 1].copy()
            vector_3: ndarray = orthogonal_basis_2d_array[:, 2].copy()

            if vector_3.dot(self.axis_2d_array[0]) < 0.0:
                orthogonal_basis_2d_array[:, 2] = - orthogonal_basis_2d_array[:, 2]
                vector_3 = - vector_3

            if outer_product_3d(vector_1, vector_2).dot(vector_3) > 0.0:
                orthogonal_basis_2d_array[:, 0] = - orthogonal_basis_2d_array[:, 0]

        angle_rad: float = self.angle * pi / 180.0
        cos_value: float = cos(angle_rad)
        sin_value: float = sin(angle_rad)
        xy_plane_rotation_array: ndarray = eye(self.get_input_dimension())
        xy_plane_rotation_array[0, 0] = cos_value
        xy_plane_rotation_array[0, 1] = -sin_value
        xy_plane_rotation_array[1, 0] = sin_value
        xy_plane_rotation_array[1, 1] = cos_value

        self.rotation_2d_array = orthogonal_basis_2d_array.dot(xy_plane_rotation_array).dot(orthogonal_basis_2d_array.T)

    def get_input_dimension(self) -> Optional[int]:
        return self.axis_2d_array.shape[1]

    def get_output_dimension(self) -> Optional[int]:
        return self.axis_2d_array.shape[1]

    def _transform(self, x_array: ndarray) -> ndarray:
        return x_array.dot(self.rotation_2d_array)
