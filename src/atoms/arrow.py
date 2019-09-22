from atoms.geo_object_2d import GeoObject2D


class Arrow(GeoObject2D):

    ARROW_DEFAULT_PLOTTING_KARGS = dict(
        color="k", linewidth=0.5, head_width=6.0, head_length=10.0, length_includes_head=True
    )

    def __init__(self, start_coor, delta_pair, text=None, **kargs):
        super(Arrow, self).__init__(Arrow.ARROW_DEFAULT_PLOTTING_KARGS, kargs)
        self.start_coor = start_coor
        self.delta_pair = delta_pair

    def draw(self, ax):
        plotting_kargs = self.get_plotting_kargs()
        ax.arrow(self.start_coor[0], -self.start_coor[1], *self.delta_pair, **plotting_kargs)
