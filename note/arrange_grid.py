from manimlib import * # type: ignore


class RosePattern(VMobject):
    def __init__(
        self,
        radius: float = 2,
        k: float = 3,
        theta_range=TAU,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.k = k
        self.radius = radius

        step_size = 0.05
        theta = np.arange(0, theta_range + step_size, step_size)

        points = [
            [
                radius * np.cos(k * t) * np.cos(t),
                radius * np.cos(k * t) * np.sin(t),
                0
            ] for t in theta
        ]

        self.set_points_smoothly(points)


class RosePatternNutshell(Scene):
    def construct(self):
        grps = VGroup()  # as there are going to be groups of Texs and RosePatterns
        texs = VGroup()
        patterns = VGroup()
        num = 7  # intended to be a square
        offset = 2.3  # controls the spacing between the elements

        frame = self.camera.frame

        for n in range(num + 1):
            for d in range(num + 1):
                if n == 0 and d == 0:
                    tex = Tex("k = \\displaystyle\\frac{n}{d}", font_size=25)
                    grps.add(tex)
                    texs.add(tex)
                if n == 0 and d != 0:
                    tex = Tex(f"d = {d}", font_size=25)
                    grps.add(tex)
                    texs.add(tex)
                if n != 0 and d == 0:
                    tex = Tex(f"n = {n}", font_size=25)
                    grps.add(tex)
                    texs.add(tex)
                if n != 0 and d != 0:
                    pattern = RosePattern(
                        k=n / d,
                        radius=frame.get_width() / (2 * offset * (num + 1)),
                        theta_range=TAU * num
                    )
                    grps.add(pattern)
                    patterns.add(pattern)

        colors = [ORANGE, TEAL, BLUE, GREEN, RED, MAROON, PINK]

        grps.arrange_in_grid(fill_rows_first=False)
        patterns.set_color_by_gradient(*colors)
        texs.set_color_by_gradient(*colors)

        self.play(*[Write(tex) for tex in texs])
        self.play(
            *[ShowCreation(pattern) for pattern in patterns],
            run_time=8,
            rate_func=linear
        )
        self.wait()
         
