from manimlib import * # type: ignore


class Density(Scene):
    def construct(self):
        axes = Axes()
        graph_1 = axes.get_graph(lambda x: np.sin(9*x))
        graph = ParametricCurve(
            lambda t: np.cos(9*t),
            t_range=(0, 10, 0.01),
            epsilon=1e-8,
        )

        self.play(ShowCreation(graph))