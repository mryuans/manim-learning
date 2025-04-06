from manimlib import * # type: ignore
from math import sin # type: ignore


class Simplefunc(Scene):
    def construct(self) -> None:
        c = Circle().set_color(color=BLUE, opacity=0.5)
        s = Square().set_color(color=RED, opacity=0.5)
        
        s.next_to(c, DOWN)
        self.play(
            LaggedStart(*(
                DrawBorderThenFill(c),
                DrawBorderThenFill(s)
            ),run_time=1, lag_ratio=0.5)
        )

        self.play(c.animate.scale(2).set_color(color=YELLOW).set_anim_args(rate_func=there_and_back))
        # TODO: figure out what is the difference betwenn "Transform" and "become"


class UpdateSimplifer(Scene):
    def construct(self) -> None:
        c = Circle().set_color(color=BLUE, opacity=0.5)
        s = Square().set_color(color=RED, opacity=0.5)

        s.next_to(c, DOWN)
        self.play(
            LaggedStart(*(
                DrawBorderThenFill(c),
                DrawBorderThenFill(s)
            ),run_time=1, lag_ratio=0.5)
        )

        c.always.shift(0.2 * RIGHT)
        s.always.next_to(c, DOWN)
        self.wait(2)


class DefineFunc(Scene):
    def construct(self) -> None:
        # TODO: figure out the difference betwenn "f_always" and "always"
        c = Circle().set_color(color=BLUE, opacity=0.5)
        s = Square().set_color(color=RED, opacity=0.5)

        s.next_to(c, DOWN)
        self.play(
            LaggedStart(*(
                DrawBorderThenFill(c),
                DrawBorderThenFill(s)
            ),run_time=1, lag_ratio=0.5)
        )


        def func(mob):
           mob.set_width(abs(sin(self.time))) 
        
        c.add_updater(func)
        s.f_always.set_width(c.get_width)
        self.wait(5)

        c.remove_updater((func))
        self.wait()
