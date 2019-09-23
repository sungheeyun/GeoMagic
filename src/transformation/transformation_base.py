from typing import Iterable, Optional
from abc import ABC, abstractmethod
from numpy import ndarray, array


class TransformationBase(ABC):
    def __call__(self, x_iter: Iterable) -> Iterable:
        x_array: ndarray = array(x_iter, float)

        if x_array.ndim == 1:
            return self._transform(x_array)

        return array([self(_array) for _array in x_array])

    @abstractmethod
    def _transform(self, x_array: ndarray) -> ndarray:
        pass

    @abstractmethod
    def get_input_dimension(self) -> Optional[int]:
        pass

    @abstractmethod
    def get_output_dimension(self) -> Optional[int]:
        pass
