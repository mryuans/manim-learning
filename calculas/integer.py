from manimlib import * # type: ignore
from scipy.integrate import quad


class Integer(InteractiveScene):
    def construct(self) -> None:
        axes = Axes(
            x_range=(-8, 8, 1),
            y_range=(-1, 7, 1),
            height=7.5,
            width=14,
            axis_config=dict(include_tip=True)
        )
        f = lambda x: 6 * math.e ** (-0.25 * x ** 2)
        actual_integer = Text(f"actual integer: {quad(f, -8, 8)[0]:.3f}").scale(0.5).to_corner(UR)
        calculas_proximation = DecimalNumber(
        	0,
        	num_decimal_places=3,
        	).next_to(actual_integer, DOWN)

        self.play(Write(actual_integer), Write(calculas_proximation))

        graph = axes.get_graph(f, color=YELLOW)
        self.play(ShowCreation(axes, run_time=2), ShowCreation(graph, run_time=2))
        
        dx_list = [0.5, 0.3, 0.1, 0.05, 0.01]
        rectangles = VGroup(
            *[
                axes.get_riemann_rectangles(
                    graph=graph,
                    stroke_width=0.1,
                    stroke_color=BLUE,
                    dx=dx,
                ) for dx in dx_list
            ]
        )
        first_area = rectangles[0]
        self.play(ShowCreation(first_area, run_time=1.5))
        # summ = first_area.get

        for i in range(1, len(dx_list)):
            new_area = rectangles[i]
            self.play(ReplacementTransform(first_area, new_area), run_time=1.5)
            self.wait()
            first_area = new_area
