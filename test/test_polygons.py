import unittest
from typing import Tuple, List
from numpy import sqrt

from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from atoms.polygon_2d import Polygon
from atoms.regular_polygon import RegularPolygon
from atoms.vector2d import Vector2D
from drawing.utils import get_figure


class TestPolygons(unittest.TestCase):
    @classmethod
    def tearDownClass(cls) -> None:
        plt.show()

    @staticmethod
    def _get_fig_axis() -> Tuple[Figure, Axes]:
        return plt.subplots()

    @staticmethod
    def _get_fig_and_axes(num_rows: int, num_cols: int) -> Tuple[Figure, List[Axes]]:
        fig: Figure = get_figure(num_rows, num_cols)
        axes: List[Axes] = fig.get_axes()

        return fig, axes

    @staticmethod
    def _finish_fig(figure: Figure, axis: Axes) -> None:
        axis.axis("off")
        axis.axis("equal")
        figure.show()

    def test_pentagon(self):
        figure, axis = TestPolygons._get_fig_axis()
        RegularPolygon(5, (0, 0), 2, 90.0).draw(axis)
        TestPolygons._finish_fig(figure, axis)

        self.assertEqual(True, True)

    def test_get_polygon_from_edges_and_angles(self):
        start_point = (1, 1)
        edge_list = [2, 3, 5]
        angle_list = [45, 60, 60]

        figure, axis = TestPolygons._get_fig_axis()
        Polygon.get_polygon_from_edges_and_angles(start_point, edge_list, angle_list).draw(axis)
        TestPolygons._finish_fig(figure, axis)

        self.assertEqual(True, True)

    def test_get_polygon_from_edges_and_angles_with_starting_vector(self):
        start_point_list: list = list()
        start_vector_list: list = list()
        edge_list_list: list = list()
        angle_list_list: list = list()

        start_point_list.append((1, 1))
        start_vector_list.append((2, 2))
        edge_list_list.append([2, 3])
        angle_list_list.append([45, 120])

        start_point_list.append((1, 1))
        start_vector_list.append((2, 2))
        edge_list_list.append([5, (Vector2D(start_vector_list[-1]) - Vector2D(start_point_list[-1])).norm()])
        angle_list_list.append([90, 90])

        figure = get_figure(len(start_point_list), 1)

        for idx, axis in enumerate(figure.get_axes()):
            Polygon.get_polygon_from_edges_and_angles_with_two_start_points(
                start_point_list[idx], start_vector_list[idx], edge_list_list[idx], angle_list_list[idx]
            ).draw(axis)
            axis.axis("equal")

        figure.show()

        self.assertEqual(True, True)

    def test_draw_two_eqiulateral_triangles(self):

        smaller_triangle = RegularPolygon(3, radius=1, angle_of_one_point=-90)
        bigger_triangle = RegularPolygon(3, radius=2, angle_of_one_point=90)

        fig, axes = TestPolygons._get_fig_and_axes(3, 2)

        for ax in axes:
            smaller_triangle.draw(ax, color="k", lw=1)
            bigger_triangle.draw(ax, color="k", lw=1)

            ax.axis("off")
            ax.axis("equal")

        bigger_triangle.draw(axes[1], color="r", lw=2)
        smaller_triangle.draw(axes[2], color="r", lw=2)

        RegularPolygon(3, radius=1, angle_of_one_point=90, center=(0, 1)).draw(axes[3], color="r", lw=2)
        RegularPolygon(3, radius=1, angle_of_one_point=90, center=(sqrt(3.0) / 2.0, -0.5)).draw(
            axes[4], color="r", lw=2
        )
        RegularPolygon(3, radius=1, angle_of_one_point=90, center=(-sqrt(3.0) / 2.0, -0.5)).draw(
            axes[5], color="r", lw=2
        )

        fig.show()

        fig.savefig("yyy.png")

        self.assertTrue(True)

    def test_pentagon_start(self):

        regular_pentagon = RegularPolygon(5, angle_of_one_point=90)

        fig, ax = TestPolygons._get_fig_axis()

        regular_pentagon.draw(ax)

        number_vertices = regular_pentagon.get_number_vertices()
        vertex_coor_array = regular_pentagon.vertex_coor_array

        for idx in range(number_vertices):
            tidx = (idx + 2) % number_vertices
            # line2d = Segment2D(vertex_coor_array[idx], vertex_coor_array[tidx])
            line2d = Polygon(vertex_coor_array[[idx, tidx]])
            line2d.draw(ax)

        TestPolygons._finish_fig(fig, ax)

        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
