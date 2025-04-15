from manimlib import *


class Dot_move(Scene):
    def construct(self) -> None:
        axes = Axes()
        graph = axes.get_graph(np.sin)
        dot = GlowDot()
        x_tracker = ValueTracker(1.5 * PI)
        get_x = x_tracker.get_value
        dot.add_updater(lambda d: d.move_to(axes.i2gp(-get_x(), graph)))
        self.add(axes, dot, graph)
        self.play(
            x_tracker.animate.set_value(0).set_anim_args(run_time=5),
        )


class Combination(Scene):
    def construct(self) -> None:
        axes1, axes2, axes3 = axes = VGroup(*(Axes(
            (-10, 10), 
            (-5, 5),
            width=FRAME_WIDTH - 2,
            height=FRAME_HEIGHT / 3 - 0.1
        ) for _ in range(3)))
        
        axes.arrange(DOWN, buff=1.0)
        self.add(axes)

        f = lambda x: np.exp(x)
        g = lambda x: np.sin(x)

        f_graph = axes1.get_graph(f, color=BLUE)
        g_graph = axes2.get_graph(g, color=YELLOW)
        self.add(f_graph, g_graph)

        sum_graph = axes3.get_graph(lambda x: f(x) + g(x), color=GREEN)
        prod_graph = axes3.get_graph(lambda x: f(x) * g(x), color=GREEN)

        for graph in (sum_graph, prod_graph):
            self.play(
                Transform(f_graph.copy(), graph.copy(), remover=True),
                TransformFromCopy(g_graph, graph)
            )
            self.wait()
            self.play(
                FadeOut(graph)
            )

