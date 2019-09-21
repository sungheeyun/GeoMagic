from numpy.core._multiarray_umath import ndarray
from transformation.transformer_base import TransformerBase


class CompositeTransformer(TransformerBase):
    """
    Implements the composit transformer.
    Given f and g, it implements g(f(x)).

    """
    def __init__(self, f_transformer: TransformerBase, g_transformer: TransformerBase):
        self.f_transformer: TransformerBase = f_transformer
        self.g_transformer: TransformerBase = g_transformer

    def _transform(self, x_array: ndarray) -> ndarray:
        y_array: ndarray = self.f_transformer._transform(x_array)
        z_array: ndarray = self.g_transformer._transform(y_array)
        return z_array
