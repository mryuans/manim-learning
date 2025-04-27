from manimlib import * # type: ignore


class UpdaterMobGroup(InteractiveScene):
    def construct(self) -> None:
        arrayValue = ValueTracker(np.linspace(0, 1, 4))
        dots = Group(
            Group(TrueDot(radius=0.05).make_3d(), GlowDot(radius=0.30))
            .set_color(random_bright_color()) for _ in range(4)
        )

        # example = get_example_loop(2)
        example = Circle(radius=2)
        loop_func = example.pfp

        def updater(dots):
            for dot, value in zip(dots, arrayValue.get_value()):
                dot.move_to(loop_func(value))

        dots.add_updater(updater)
        
        def get_polygon(dots):
            ploy = Polygon(RIGHT, LEFT)
            ploy.add_updater(lambda m: m.set_points_as_corners(
                [*[dot.get_center() for dot in dots], dots[0].get_center()]
            ))
            ploy.set_stroke(YELLOW)
            return ploy

        plolygon = get_polygon(dots)         
        new_square_params = [
            [0.519, 0.308, 0.277, 0.177],
            [0.444, 0.105, 0.877, 0.650],
            [0.037, 0.739, 0.468, 0.372],
        ]

        self.add(example, dots)
        self.play(ShowCreation(plolygon))
        self.play(
            *[arrayValue.animate.set_value(params) for params in new_square_params],
            run_time=14,
        )
        self.play(
            UpdateFromFunc(arrayValue, lambda v: v.set_value(np.random.random(4))),
        )


