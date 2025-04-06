from manimlib import * # type: ignore


class PointsTheory(Scene):
    def construct(self) -> None:
        points = [
            [1, 1, 0],
            [1, 0 ,0],
            [0, 0, 0],
            [1, 1, 0]
        ]
        dots = VGroup(*[Dot(point).set_color(YELLOW) for point in points])
        mob = VMobject().set_points_as_corners(points).set_color(BLUE)
        self.play(
            ShowCreation(mob),
            ShowCreation(dots),
        )
        self.play(
            LaggedStart(*(
                dot.animate.scale(1.4).set_color(RED).set_anim_args(rate_func=there_and_back) 
                for dot in dots
            ),
            run_time=1,
            lag_ratio=0.5
        ))

        self.play(mob.animate.make_smooth())
