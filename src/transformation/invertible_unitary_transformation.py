from numpy import ndarray

from transformation.unitary_transformation import UnitaryTransformation
from transformation.inverible_transformation import InvertibleTransformation


class InvertibleUnitaryTransformation(UnitaryTransformation, InvertibleTransformation):
    """
    Implements an intertible unitary transformation.
    """

    def __init__(self, invertible_unitary_array: ndarray):
        UnitaryTransformation.__init__(self, invertible_unitary_array)
        self._check_attrs()

    def _check_attrs(self):
        if self.array_2d.shape[0] != self.array_2d.shape[1]:
            raise Exception(f"array_2d should be a square array; its shape is {self.array_2d.shape}!")

    def get_inverse_transformation(self) -> UnitaryTransformation:
        return InvertibleUnitaryTransformation(self.array_2d_T)
