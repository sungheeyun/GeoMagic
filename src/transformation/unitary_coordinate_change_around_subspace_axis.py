from typing import Iterable, Union

from numpy import hstack, ndarray, eye, array
from numpy.linalg import qr

from utils import outer_product_3d
from transformation.invertible_unitary_transformation import InvertibleUnitaryTransformation


class UnitaryCoordinateChangeAroundSubspaceAxis(InvertibleUnitaryTransformation):
    """
    Implements a unitary coordinate changea around a subspace.
    Let V be the n-dimensional space we reside in and
    let Y be the subspace of V around which we consider this unitary coordinate change.
    Let X be the orthogonal complement of Y.
    Then we want to find an orthonormal basis for X together with one for Y.
    Let u_1, ... u_k be one for X and u_{k+1}, ... u_n be one for Y.
    Let U = [u_1 ... u_n]. Then this class instance performs the transformation of
        f(x) = U^T x.

    The subspace Y is the range of axis_2d_array.T.
    """

    def __init__(self, axis_2d_iter: Iterable[Iterable[Union[float, int]]]):
        # perform QR-decomposition to form an orthonormal coordinate vectors
        self.axis_2d_array: ndarray = array(axis_2d_iter, float)

        num_axis_vectors, num_dimensions = self.axis_2d_array.shape
        q_array, r_array = qr(hstack((self.axis_2d_array.T, eye(num_dimensions))))
        orthogonal_basis_2d_array: ndarray = hstack((q_array[:, num_axis_vectors:], q_array[:, :num_axis_vectors]))

        if num_dimensions == 3 and num_axis_vectors == 1:
            vector_1: ndarray = orthogonal_basis_2d_array[:, 0].copy()
            vector_2: ndarray = orthogonal_basis_2d_array[:, 1].copy()
            vector_3: ndarray = orthogonal_basis_2d_array[:, 2].copy()

            if vector_3.dot(self.axis_2d_array[0]) < 0.0:
                orthogonal_basis_2d_array[:, 2] = -orthogonal_basis_2d_array[:, 2]
                vector_3 = -vector_3

            if outer_product_3d(vector_1, vector_2).dot(vector_3) < 0.0:
                orthogonal_basis_2d_array[:, 0] = -orthogonal_basis_2d_array[:, 0]

        super(UnitaryCoordinateChangeAroundSubspaceAxis, self).__init__(orthogonal_basis_2d_array.T)
