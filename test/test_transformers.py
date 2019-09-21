import unittest

from numpy import allclose, ndarray
from numpy.random import rand

from transformation.scaling import Scaling
from transformation.shift import Shift
from transformation.composite_transformer import CompositeTransformer


class TestTransformers(unittest.TestCase):
    SCALE_FACTOR = 3.0
    SHIFT_DELTA = 10.0

    def test_basic_functionalities(self):
        scaler: Scaling = Scaling(TestTransformers.SCALE_FACTOR)
        shifter: Shift = Shift(TestTransformers.SHIFT_DELTA)

        x_array_1d: ndarray = rand(5)

        self.assertTrue(allclose(scaler(x_array_1d), x_array_1d * TestTransformers.SCALE_FACTOR))
        self.assertTrue(allclose(shifter(x_array_1d), x_array_1d + TestTransformers.SHIFT_DELTA))

        x_array_ndim: ndarray = rand(5, 3, 2)

        self.assertTrue(allclose(scaler(x_array_ndim), x_array_ndim * TestTransformers.SCALE_FACTOR))
        self.assertTrue(allclose(shifter(x_array_ndim), x_array_ndim + TestTransformers.SHIFT_DELTA))

    def test_composite_transformers(self):
        scaler: Scaling = Scaling(TestTransformers.SCALE_FACTOR)
        shifter: Shift = Shift(TestTransformers.SHIFT_DELTA)

        x_array_ndim: ndarray = rand(5, 3, 2)

        composite_transformer_1 = CompositeTransformer(scaler, shifter)
        composite_transformer_2 = CompositeTransformer(shifter, scaler)

        self.assertTrue(
            allclose(
                composite_transformer_1(x_array_ndim),
                x_array_ndim * TestTransformers.SCALE_FACTOR + TestTransformers.SHIFT_DELTA,
                )
        )

        self.assertTrue(
            allclose(
                composite_transformer_2(x_array_ndim),
                (x_array_ndim + TestTransformers.SHIFT_DELTA) * TestTransformers.SCALE_FACTOR,
            )
        )


if __name__ == "__main__":
    unittest.main()
