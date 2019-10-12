import unittest

from numpy import allclose, ndarray, ones, ones_like
from numpy.random import rand

from transformation.scaling import Scaling
from transformation.shifting import Shifting
from transformation.composite_transformer import CompositeTransformation


class TestTransformers(unittest.TestCase):
    SCALE_FACTOR = 3.0
    SCALAR_SHIFT_DELTA = 10.0

    def test_basic_functionality(self):
        x_array_1d: ndarray = rand(5)

        shift_vector: ndarray = TestTransformers.SCALAR_SHIFT_DELTA * ones_like(x_array_1d)

        scaler: Scaling = Scaling(TestTransformers.SCALE_FACTOR)
        shifter: Shifting = Shifting(shift_vector)

        self.assertTrue(allclose(scaler(x_array_1d), x_array_1d * TestTransformers.SCALE_FACTOR))
        self.assertTrue(allclose(shifter(x_array_1d), x_array_1d + shift_vector))

        x_array_ndim: ndarray = rand(5, 3, 2)

        shift_vector: ndarray = TestTransformers.SCALAR_SHIFT_DELTA * ones(x_array_ndim.shape[-1])
        shifter: Shifting = Shifting(shift_vector)
        shifter(x_array_ndim)
        x_array_ndim + shift_vector

        self.assertTrue(allclose(scaler(x_array_ndim), x_array_ndim * TestTransformers.SCALE_FACTOR))
        self.assertTrue(allclose(shifter(x_array_ndim), x_array_ndim + shift_vector))

    def test_composite_transformers(self):
        x_array_ndim: ndarray = rand(5, 3, 2)

        shift_vector: ndarray = TestTransformers.SCALAR_SHIFT_DELTA * ones(x_array_ndim.shape[-1])

        scaler: Scaling = Scaling(TestTransformers.SCALE_FACTOR)
        shifter: Shifting = Shifting(shift_vector)

        composite_transformer_1 = CompositeTransformation((scaler, shifter))
        composite_transformer_2 = CompositeTransformation((shifter, scaler))

        self.assertTrue(
            allclose(
                composite_transformer_1(x_array_ndim),
                x_array_ndim * TestTransformers.SCALE_FACTOR + TestTransformers.SCALAR_SHIFT_DELTA,
            )
        )

        self.assertTrue(
            allclose(
                composite_transformer_2(x_array_ndim),
                (x_array_ndim + TestTransformers.SCALAR_SHIFT_DELTA) * TestTransformers.SCALE_FACTOR,
            )
        )


if __name__ == "__main__":
    unittest.main()
