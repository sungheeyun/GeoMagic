import unittest

from numpy import vstack, hstack, zeros, sqrt
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D

from drawing.utils import get_figure
from atoms.regular_polygon import RegularPolygon
from complex_objs.seg_collection_ndim import SegCollectionNDim


class TestSegmentCollection(unittest.TestCase):
    def test_basic_functionalities(self):
        # create 3-dimnesional segment collection
        regular_triangle = RegularPolygon(3)

        coor_2d_array = vstack((regular_triangle.vertex_coor_array, regular_triangle.vertex_coor_array[0]))
        coor_3d_array = hstack((coor_2d_array, zeros((coor_2d_array.shape[0], 1))))

        north_point = [0, 0, sqrt(2.0)]

        seg_collection_ndim = SegCollectionNDim(3, coor_3d_array)
        for idx in range(len(coor_3d_array)-1):
            vertex = coor_3d_array[idx]
            print(vertex.shape)
            seg_collection_ndim.add_segments(vstack((vertex, north_point)))

        for segment in seg_collection_ndim.segment_ndim_list:
            print(segment)

        fig: Figure = get_figure(1, 2, projection='3d')
        axis1, axis2 = fig.get_axes()

        seg_collection_ndim.draw3d(axis1)
        seg_collection_ndim.draw3d(axis2)

        axis1.axis('off')

        fig.show()
        plt.show()

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
