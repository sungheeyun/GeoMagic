
from abc import ABC, abstractmethod

import numpy as np
from matplotlib import pyplot as plt


def get_figure(
        nrow, ncol,
        l_margin, r_margin, b_margin, t_margin,
        spWidth, spHeight,
        wPadding=0.0, hPadding=0.0,
        **kargs
):
    num = kargs.pop( 'num', None )

    l_margin, r_margin, b_margin, t_margin\
        = float(l_margin), float(r_margin), float(b_margin), float(t_margin)

    def tolist(l, n):
        assert n >= 0, ( 'FATAL', n )
        if n == 0: return []
        if isinstance( l, int ): l = float(l)
        if isinstance( l, float ): l = [l] * n
        return np.array(l,float)

    spWidthList = tolist(spWidth, ncol)
    spHeightList = tolist(spHeight, nrow)
    wPaddingList = tolist(wPadding, ncol-1)
    hPaddingList = tolist(hPadding, nrow-1)

    figwidth = l_margin + r_margin + sum(spWidthList) + sum(wPaddingList)
    figheight = b_margin + t_margin + sum(spHeightList) + sum(hPaddingList)

    fig = plt.figure(num=num, figsize=(figwidth, figheight))
    # fig = pl.figure( figsize = ( figwidth, figheight ), facecolor = 'lightgoldenrodyellow' )
    # fig = pl.figure( figsize = ( figwidth, figheight ), facecolor = 'red' )
    # print( 'fig.get_facecolor() =', fig.get_facecolor() )

    for i in range(nrow):
        for j in range(ncol):
            l = (l_margin + sum(spWidthList[:j]) + sum(wPaddingList[:j])) / figwidth
            b = (b_margin + sum(spHeightList[i + 1:]) + sum(hPaddingList[i:])) / figheight
            w = spWidthList[j] / figwidth
            h = spHeightList[i] / figheight

            fig.add_axes([l, b, w, h], **kargs)

    return fig


class DiagramObject(ABC):
    component_list = list()
    DEFAULT_KARGS = dict()

    def __init__(self, default_plotting_kargs, plotting_kargs_):
        DiagramObject.component_list.append(self)

        self.plotting_kargs = DiagramObject.DEFAULT_KARGS.copy()
        self.plotting_kargs.update(default_plotting_kargs)
        self.plotting_kargs.update(plotting_kargs_)

    def get_plotting_kargs(self):
        return self.plotting_kargs

    @abstractmethod
    def draw(self, ax):
        pass

    @staticmethod
    def draw_all_components(**kargs):
        #fig, ax = plt.subplots(**kargs)

        fig = get_figure(1, 1, 0, 0, 0, 0, 10, 8)
        ax = fig.get_axes()[0]

        for component in DiagramObject.component_list:
            component.draw(ax)

        ax.axis('equal')
        ax.axis('off')

        fig.show()

        return fig

class Line(DiagramObject):
    def __init__(self, start_coor, end_coor):
        super(Line, self).__init__({})
        self.start_coor  = start_coor
        self.end_coor = end_coor

        self.coor_array = np.vstack((self.start_coor, self.end_coor))

    def draw(self, ax, **kargs):
        plotting_kargs = self.get_plotting_kargs(kargs)
        ax.plot(self.coor_array[:,0], -self.coor_array[:,1], **plotting_kargs)


class Box(DiagramObject):

    BOX_DEFAULT_PLOTTING_KARGS = dict(
        facecolor='w',
        edgecolor='k',
        linewidth=.5,
        zorder=5
    )

    def __init__(self, lt_coor, wh_pair, text=None, **kargs):
        super(Box, self).__init__(Box.BOX_DEFAULT_PLOTTING_KARGS, kargs)
        self.lt_coor = lt_coor
        self.wh_pair = wh_pair
        self.text = text

        left, top = self.lt_coor
        width, height = self.wh_pair


        self.x_coor_array = left + np.array([0, 0, 1, 1, 0]) * width
        self.y_coor_array = top + np.array([0, 1, 1, 0, 0]) * height

        self.mid_x_coor = left + width / 2.0
        self.mid_y_coor = top + height / 2.0

        self.text_x_coor = self.mid_x_coor
        self.text_y_coor = self.mid_y_coor

    def get_mid_x_coor(self):
        return self.mid_x_coor

    def draw(self, ax):
        plotting_kargs = self.get_plotting_kargs()
        ax.fill(self.x_coor_array, -self.y_coor_array, **plotting_kargs)

        if self.text:
            ax.text(self.text_x_coor, -self.text_y_coor, self.text,
                    ha='center', va='center', zorder=6)

class Line(DiagramObject):
    LINE_DEFAULT_PLOTTING_KARGS = dict(
        color='k',
        linewidth=.5,
    )

    def __init__(self, start_coor, end_coor, **kargs):
        super(Line, self).__init__(Line.LINE_DEFAULT_PLOTTING_KARGS, kargs)
        self.start_coor  = start_coor
        self.end_coor = end_coor

        self.coor_array = np.vstack((self.start_coor, self.end_coor))

    def draw(self, ax):
        plotting_kargs = self.get_plotting_kargs()
        ax.plot(self.coor_array[:,0], -self.coor_array[:,1], **plotting_kargs)


class Arrow(DiagramObject):

    ARROW_DEFAULT_PLOTTING_KARGS = dict(
        color='k',
        linewidth=.5,
        head_width=6.0,
        head_length=10.0,
        length_includes_head=True,
    )

    def __init__(self, start_coor, delta_pair, text=None, **kargs):
        super(Arrow, self).__init__(Arrow.ARROW_DEFAULT_PLOTTING_KARGS, kargs)
        self.start_coor = start_coor
        self.delta_pair = delta_pair

    def draw(self, ax):
        plotting_kargs = self.get_plotting_kargs()
        ax.arrow(self.start_coor[0], -self.start_coor[1], *self.delta_pair, **plotting_kargs)


if __name__ == '__main__':

    gap_between_components = 200.0
    component_box_width = 120.0
    component_box_height = 30.0

    data_flow_start_y = 50.0
    small_box_width = 10.0
    small_box_height = 30.0

    info_box_width = 120
    info_box_height = 20

    line_height = 500.0

    component_name_list = ['RL Agent', 'MLP Translator', 'Test Agent', 'App Simulator']

    component_box_list = list()

    for idx, component_name in enumerate(component_name_list):
        left_x = gap_between_components*float(idx)
        box = Box(
            (left_x, 0.0),
            (component_box_width, component_box_height),
            text=component_name
        )
        component_box_list.append(box)

        line_x = component_box_list[-1].get_mid_x_coor()
        Line((line_x, component_box_height), (line_x, line_height))

    print(DiagramObject.component_list)

    data_flow_list = list()
    data_flow_list.append((0, 1, 'State'))
    data_flow_list.append((1, 2, 'App Page'))
    data_flow_list.append((2, 3, 'Drive App'))
    data_flow_list.append((3, 2, 'fetch Page Info'))
    data_flow_list.append((2, 1, 'Page & Objects'))
    data_flow_list.append((1, 0, 'State & Actions'))
    data_flow_list.append((0, 1, 'Action'))
    data_flow_list.append((1, 2, 'Action on Object'))
    data_flow_list.append((2, 3, 'Click/Type'))
    data_flow_list.append((3, 2, 'fetch Page Info'))
    data_flow_list.append((2, 1, 'Page & Objects'))
    data_flow_list.append((1, 0, '(Repeat)'))

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
            (from_comp_box_mid_x_coor - small_box_width/2.0, line_y_coor - small_box_height),
            (small_box_width, small_box_height)
        )

        if draw_to_box:
            to_box = Box(
                (to_comp_box_mid_x_coor - small_box_width/2.0, line_y_coor),
                (small_box_width, small_box_height)
            )

        Arrow(
            (from_comp_box_mid_x_coor + float_is_from_less_than_to * small_box_width/2.0, line_y_coor),
            (arrow_length, 0.0)
        )

        Box(
            (mid_x_coor - info_box_width / 2.0, line_y_coor - info_box_height / 2.0),
            (info_box_width, info_box_height),
            text=info_text,
            edgecolor=None
        )

        print(from_comp_num, to_comp_num, info_text)

    fig = DiagramObject.draw_all_components(figsize=(10, 10))
    fig.savefig('test_bot_mlp_workflow.png')


    if '__file__' in dir():
        plt.show()
