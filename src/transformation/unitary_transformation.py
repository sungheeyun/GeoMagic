from numpy import ndarray, allclose, eye

from transformation.linear_transformation import LinearTransformation


class UnitaryTransformation(LinearTransformation):
    """
    Implements a unitary transformation.
    """

    def __init__(self, unitary_array: ndarray):
        super(UnitaryTransformation, self).__init__(unitary_array)
        self._check_attrs()

    def _check_attrs(self):
        if not allclose(self.array_2d_T * self.array_2d, eye(self.array_2d.shape[1])):
            raise Exception("Error: array_2d does not confirm to the unitary transformation.")
