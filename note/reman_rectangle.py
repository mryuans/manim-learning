from manimlib import * # type: ignore 


class Rectangle(Scene):
    def construct(self) -> None:
        f = lambda x: 4 * np.exp(- x ** 2)
        axes = Axes()
        graph = axes.get_graph(f)
        rect = axes.get_riemann_rectangles(graph, dx=0.2)
        rect.set_opacity(opacity=0.7)
        rect.set_stroke(WHITE, 1)

        self.play(
            FadeIn(axes),
            ShowCreation(graph)
        )
        self.play(ShowCreation(rect), run_time=3)

        self.play(LaggedStart(*(
            rect_.animate.set_color(YELLOW).shift(UP * SMALL_BUFF).set_anim_args(rate_func=there_and_back) for rect_ in rect),
            lag_ratio=0.3,
            run_time=5
        ))

        dx = [0.1, 0.075, 0.05, 0.03, 0.02, 0.01, 0.005]
        for dx_ in dx:
            new_rect = axes.get_riemann_rectangles(graph, dx=dx_)
            new_rect.set_stroke(WHITE, 1)
            new_rect.set_fill(opacity=0.7)
            self.play(Transform(rect, new_rect))
