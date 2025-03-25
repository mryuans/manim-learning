from manimlib import *


def slope_pos(pos, a):
    x, y = pos
    slope = x + a * y
    start_pos = (x -0.1, y - 0.1 * slope)
    end_pos = (x + 0.1, y + 0.1 * slope)
    return start_pos, end_pos

class Illustration(Scene):
    def construct(self):
        axes = Axes(
            x_range=(-8, 8, 1),
            y_range=(-8, 8, 1),
            height=6,
            width=6,
            axis_config={
                "color": BLUE,
                },
        )
        axes.add_coordinate_labels(font_size=10)

        self.play(ShowCreation(axes))
        self.wait()
        self.play(axes.animate.set_opacity(0.25), run_time=1)
        a = ValueTracker(1)
        
        colors = [BLUE_A, BLUE_B, RED_A, RED_B, GOLD_A, GOLD_B, GREEN_A, GREEN_B, PURPLE_A, PURPLE_B]
        arr_group = VGroup()
        for x in range(-8, 9):
            for y in range(-8, 9):
                pos = (x, y)
                start_pos, end_pos = slope_pos(pos, a.get_value())
                arr = Arrow(axes.c2p(*start_pos), axes.c2p(*end_pos), buff=0)
                arr.scale(0.25 / arr.get_length())
                arr.set_color(GREEN)
                arr_group.add(arr)
        self.play(ShowCreation(arr_group))
        self.wait()
        self.play(arr_group.animate.set_opacity(0.4))
        for color, c in zip(colors, range(-5, 6)):
            graph = axes.get_graph(lambda x: -1 - x + c * math.e**x)
            graph.set_stroke(color, 2)
            self.play(ShowCreation(graph))
        self.play(a.animate.set_value(5))