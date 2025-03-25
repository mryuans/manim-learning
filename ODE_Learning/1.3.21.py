from manimlib import *
from time import sleep


def get_slope_pos(center_pos: tuple[int, int]) -> tuple[int, int]:
    x, y = center_pos
    slope = x + y
    end_pos = (x + 0.1, y + slope * 0.1)
    start_pos = (x - 0.1, y - slope * 0.1)
    return start_pos, end_pos


def function(x: int):
    return -1 * x - 1 + math.e ** x


class SlopeMap(Scene):
    def construct(self):
        text = Text("Slope Map")
        text.set_color(BLUE_A)
        answer = Text(f"1.3 test 21: y(-4) = {function(-4)}")
        answer.set_color(BLUE_A)
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-5, 5],
            axis_config={
                "color": BLUE,
            },
            height=10,
            width=10,
        )

        axes.add_coordinate_labels(
            font_size=20,
            num_decimal_places=1,
        )

        self.play(Write(text))
        self.play(FadeOut(text))
        self.play(Write(axes))

        for x in range(-5, 6):
            for y in range(-5, 6):
                center_pos = (x, y)
                (_x, _y), (x_, y_) = get_slope_pos(center_pos)
                arr = Arrow(axes.c2p(_x, _y), axes.c2p(x_, y_), buff=0)
                arr.scale(0.5 / arr.get_length())
                arr.set_color(GREEN)
                self.play(Write(arr), run_time=0.01)

        graph = FunctionGraph(function, x_range=[-5, 5, 0.1])
        graph.set_color(RED)
        self.play(Write(graph))
        self.wait()
        self.play(Write(answer.scale(0.5).next_to(axes, DOWN)))
        self.wait()
