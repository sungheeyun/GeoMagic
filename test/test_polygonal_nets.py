import unittest

from matplotlib import pyplot as plt

from atoms.polygon import Polygon
from atoms.regular_polygon import RegularPolygon
from complex_objs.polygonal_prism_net import PolygonalPrismNet

# from utils import FIGURES_DIR


class TestPolygonalNets(unittest.TestCase):
    @classmethod
    def tearDownClass(cls) -> None:
        plt.show()

    def test_polygonal_prism_nets(self):

        base_polygon: Polygon = RegularPolygon(5)
        # base_polygon = Polygon([[0, 0], [1, 1], [-2, 10], [-3, 1]])
        polygonal_prism_net: PolygonalPrismNet = PolygonalPrismNet(base_polygon, 2)

        figure, axis = plt.subplots()
        polygonal_prism_net.draw(axis)

        axis.axis("off")
        axis.axis("equal")
        figure.show()

        # figure.savefig(os.path.join(FIGURES_DIR, 'pentagonal_prisum_net.png'))
        # figure.savefig(os.path.join(FIGURES_DIR, 'heptagonal_prisum_net.png'))

        self.assertEqual(True, True)


if __name__ == "__main__":
    unittest.main()
