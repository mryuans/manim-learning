from manimlib import * # type: ignore


class LissajousCurve(ParametricCurve):
    def __init__(
        self,
        a: float = 1,
        b: float = 1,
        A: float= 1,
        B: float = 1,
        delta: float = PI/2,
        theta_range: float = 2 * PI,
        step_size: float = 0.1,
        **kwargs,
    ):
        self.a = a
        self.b = b
        self.A = A
        self.B = B
        self.theta_range = theta_range
        self.delta = delta
        self.step_size = step_size

        super().__init__(
            t_func=lambda t: [
                A * np.sin(a * t + delta),
                B * np.sin(b * t),
                0
            ],
            t_range=(0, theta_range + step_size, step_size),
            **kwargs
        )

class Show(Scene):
    def construct(self) -> None:
        colors = [ORANGE, TEAL, BLUE, GREEN, RED, MAROON, PINK]
        example = LissajousCurve(
            a=2,
            b=3,
        ).set_stroke(width=3.5)
        example.set_color_by_gradient(BLUE, GREEN, BLUE)
        self.play(ShowCreation(example), run_time=3)
        self.play(FadeOut(example))

        pattern = VGroup()
        pattern.add(example)

        infinite = LissajousCurve(a=1, b=2, delta=PI/2).set_stroke(width=3.5)
        pattern.add(infinite)

        circle = LissajousCurve(a=1, b=1, delta=PI/2).set_stroke(width=3.5)
        pattern.add(circle)

        star = LissajousCurve(a=3, b=4, delta=PI/2).set_stroke(width=3.5)
        pattern.add(star)

        pattern.set_color_by_gradient(*colors)
        pattern.arrange_in_grid(fill_rows_first=False)
        self.play(ShowCreation(pattern), run_time=3)

