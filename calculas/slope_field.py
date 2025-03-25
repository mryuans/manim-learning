from random import randrange
from manimlib import *


class SlopeF(Scene):
    a = 1
    def construct(self) -> None:
        axes = Axes(
            x_range=(-10, 10, 1),
            y_range=(-10, 10, 1),
            width=6,
            height=6,
            ).set_color(BLUE)

        def slope_f(x, y, a):
            slope = x + y * a
            start = (x + 0.1, y - 0.1 * slope)
            end = (x - 0.1, y + 0.1 * slope)
            return (start, end)

        a = 1
        arr_g = VGroup()

        for x in range(-10, 11):
            for y in range(-10, 11):
                point_set = slope_f(x, y, a)
                arr = Arrow(axes.c2p(*point_set[0]), axes.c2p(*point_set[1]), buff=0).set_color(YELLOW)
                arr.scale(0.25 / arr.get_length())
                arr_g.add(arr)

        # def updater(arr_g, dt):
        #     arr_g_ = VGroup()
        #     SlopeF.a += dt
        #     for x in range(-10, 11):
        #         for y in range(-10, 11):
        #             point_set = slope_f(x, y, a)
        #             arr = Arrow(axes.c2p(*point_set[0]), axes.c2p(*point_set[1]), buff=0).set_color(YELLOW)
        #             arr.scale(0.25 / arr.get_length())
        #             arr_g_.add(arr)
        #     arr_g.become(arr_g_)

        # arr_g.add_updater(updater)
        self.play(ShowCreation(axes), ShowCreation(arr_g))
        self.wait(10)
