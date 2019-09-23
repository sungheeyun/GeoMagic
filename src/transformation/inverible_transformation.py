from abc import abstractmethod

from transformation.transformation_base import TransformationBase


class InvertibleTransformation(TransformationBase):
    @abstractmethod
    def get_inverse_transformation(self) -> TransformationBase:
        pass
