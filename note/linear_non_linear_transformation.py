from manimlib import * # type: ignore


class LinearOne(Scene):
    def construct(self) -> None:
        matrix = [[1, 0],[0, 1]]
        title = VGroup(
            Text("let's try some linear transformation:"),
            IntegerMatrix(matrix),
        )
        title.arrange(RIGHT)
        
        axes = NumberPlane(
            x_range=(-10, 10),
            y_range=(-5, 5)
        )
        axes_re = axes.copy()
        self.play(Write(title))
        self.play(
            title.animate.to_edge(UP),
            ShowCreation(axes)
        )

        self.play(axes.animate.apply_matrix(matrix), run_time=3)
        self.play(
            FadeOut(axes),
            Write(axes_re),
            run_time=3
        )


class NonLinearOne(Scene):
    def construct(self) -> None:
        title = TexText('''
        What about some non-linear? \\\\
        like: $z \\rightarrow sin(z)$
        ''').to_corner(UR)
        rec = BackgroundRectangle(title, color=BLACK, fill_opacity=0.5, buff=SMALL_BUFF)
        complex_plane = ComplexPlane()
        com = complex_plane.copy().set_opacity(0.3)
        com.add_coordinate_labels(font_size=24)
        complex_plane.prepare_for_nonlinear_transform()

        self.play(
            Write(complex_plane, run_time=3),
            FadeIn(com),
            FadeIn(rec),
            Write(title),
        )
        self.wait()
        self.play(
            complex_plane.animate.apply_complex_function(lambda z: np.sin(z)),
            run_time=6
        )
        

class TextTransformation(Scene):
    def construct(self) -> None:
        grid = Tex(r"\pi").get_grid(10, 10, height=4)
        
        self.play(Write(grid))
        self.play(grid.animate.shift(LEFT).set_anim_args(rate_func=there_and_back))
        self.play(grid.animate.set_submobject_colors_by_gradient(BLUE, PINK))
        self.play(grid.animate.set_height(TAU - MED_SMALL_BUFF))
        self.play(grid.animate.apply_complex_function(np.exp), run_time=5)
        self.play(
            grid.animate.apply_function(
                lambda p: [
                    p[0] + 0.5 * np.sin(p[1]),
                    p[1] + 0.5 * np.cos(p[0]),
                    p[2]
                ]
            ),
            run_time=5
        )
        self.wait()
