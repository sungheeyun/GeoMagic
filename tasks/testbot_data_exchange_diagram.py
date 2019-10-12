import os

from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

from atoms.arrow import Arrow
from atoms.box import Box
from atoms.geo_object_2d import GeoObject2D
from atoms.segment_2d import Segment2D

if __name__ == "__main__":

    gap_between_components = 200.0
    component_box_width = 120.0
    component_box_height = 30.0

    data_flow_start_y = 50.0
    small_box_width = 10.0
    small_box_height = 30.0

    info_box_width = 120
    info_box_height = 20

    line_height = 500.0

    component_name_list = ["RL Agent", "MLP Translator", "Test Agent", "App Simulator"]

    component_box_list = list()

    for idx, component_name in enumerate(component_name_list):
        left_x = gap_between_components * float(idx)
        box = Box((left_x, 0.0), (component_box_width, component_box_height), text=component_name)
        component_box_list.append(box)

        line_x = component_box_list[-1].get_mid_x_coor()
        Segment2D((line_x, component_box_height), (line_x, line_height))

    print(GeoObject2D.component_list)

    data_flow_list = list()
    data_flow_list.append((0, 1, "State"))
    data_flow_list.append((1, 2, "App Page"))
    data_flow_list.append((2, 3, "Drive App"))
    data_flow_list.append((3, 2, "fetch Page Info"))
    data_flow_list.append((2, 1, "Page & Objects"))
    data_flow_list.append((1, 0, "State & Actions"))
    data_flow_list.append((0, 1, "Action"))
    data_flow_list.append((1, 2, "Action on Object"))
    data_flow_list.append((2, 3, "Click/Type"))
    data_flow_list.append((3, 2, "fetch Page Info"))
    data_flow_list.append((2, 1, "Page & Objects"))
    data_flow_list.append((1, 0, "(Repeat)"))

    draw_to_box = True
    for idx, value in enumerate(data_flow_list):
        from_comp_num, to_comp_num, info_text = value

        from_comp_box = component_box_list[from_comp_num]
        to_comp_box = component_box_list[to_comp_num]

        from_comp_box_mid_x_coor = from_comp_box.get_mid_x_coor()
        to_comp_box_mid_x_coor = to_comp_box.get_mid_x_coor()

        float_is_from_less_than_to = 1.0 if from_comp_num < to_comp_num else -1.0

        line_y_coor = data_flow_start_y + (float(idx) + 1.0) * small_box_height
        arrow_length = to_comp_box_mid_x_coor - from_comp_box_mid_x_coor - float_is_from_less_than_to * small_box_width
        mid_x_coor = (to_comp_box_mid_x_coor + from_comp_box_mid_x_coor) / 2.0

        from_box = Box(
            (from_comp_box_mid_x_coor - small_box_width / 2.0, line_y_coor - small_box_height),
            (small_box_width, small_box_height),
        )

        if draw_to_box:
            to_box = Box(
                (to_comp_box_mid_x_coor - small_box_width / 2.0, line_y_coor), (small_box_width, small_box_height)
            )

        Arrow(
            (from_comp_box_mid_x_coor + float_is_from_less_than_to * small_box_width / 2.0, line_y_coor),
            (arrow_length, 0.0),
        )

        Box(
            (mid_x_coor - info_box_width / 2.0, line_y_coor - info_box_height / 2.0),
            (info_box_width, info_box_height),
            text=info_text,
            edgecolor=None,
        )

        print(from_comp_num, to_comp_num, info_text)

    fig: Figure = plt.figure(figsize=(10, 10))
    axis: Axes = fig.add_subplot(111)
    GeoObject2D.draw_all_components(axis)
    fig.savefig(os.path.join(os.curdir, "figures", "test_bot_mlp_workflow.png"))

    if "__file__" in dir():
        plt.show()
