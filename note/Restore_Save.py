from manimlib import *


class SaveAndRestore(InteractiveScene):
    def construct(self):
        axes = Axes(
            (-int(8 * PI), int(8 * PI)), 
            (-0.5, 1.0, 0.5),
            width=FRAME_WIDTH * PI + 1,
            height=4
            )
        sin_graph = axes.get_graph(np.sin)
        dx = 0.01
        rec = axes.get_riemann_rectangles(
            sin_graph,
            dx=dx,
            negative_color=RED_E,
            fill_opacity=1,
        )
        self.play(LaggedStart(
            FadeIn(axes),
            ShowCreation(sin_graph),
            Write(rec),
            lag_ratio=0.1,
            run_time=3
        ))

        next_area = rec.copy().stretch_about_point(1 / PI, 0, axes.get_origin())
        next_graph = sin_graph.copy().stretch_about_point(1 / PI, 0, axes.get_origin())

        sin_graph.save_state()
        rec.save_state()
        self.play(
            Transform(sin_graph, next_graph),
            Transform(rec, next_area)
        )
        self.wait()
        self.play(
            Restore(sin_graph),
            Restore(rec)
        )
# The Restore() and mob.animate.restore() is both accepted
