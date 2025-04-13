from manimlib import *


class Testself(Scene):
    def construct(self) -> None:
        axes = Axes()
        circle = Circle().set_fill(color=BLUE, opacity=0.5)
        circle.shift(LEFT * 3)
        self.add(axes, circle)
        
        self.focus()


class OpeningManimExample(Scene):
    def construct(self):
        intro_words = Text("""
            The original motivation for manim was to
            better illustrate mathematical functions
            as transformations.
        """)
        intro_words.to_edge(UP)

        self.play(Write(intro_words))
        self.wait(2)

        # Linear transform
        grid = NumberPlane((-10, 10), (-5, 5))
        matrix = [[1, 1], [0, 1]]
        linear_transform_words = VGroup(
            Text("This is what the matrix"),
            IntegerMatrix(matrix).set_backstroke(BLACK),
            Text("looks like")
        )
        linear_transform_words.arrange(RIGHT)
        linear_transform_words.to_edge(UP)
        linear_transform_words.set_stroke(BLACK, 10)

        self.play(
            ShowCreation(grid),
            FadeTransform(intro_words, linear_transform_words)
        )
        self.wait()
        self.play(grid.animate.apply_matrix(matrix), run_time=3)
        self.wait()

        # Complex map
        c_grid = ComplexPlane()
        moving_c_grid = c_grid.copy()
        moving_c_grid.prepare_for_nonlinear_transform()
        c_grid.set_stroke(BLUE_E, 1)
        c_grid.add_coordinate_labels(font_size=24)
        complex_map_words = TexText("""
            Or thinking of the plane as $\\mathds{C}$,\\\\
            this is the map $z \\rightarrow z^2$
        """)
        complex_map_words.to_corner(UR)
        complex_map_words.set_stroke(BLACK, 5).set_backstroke(BLACK)

        self.play(
            FadeOut(grid),
            Write(c_grid, run_time=3),
            FadeIn(moving_c_grid),
            FadeTransform(linear_transform_words, complex_map_words),
        )
        self.wait()
        self.play(
            moving_c_grid.animate.apply_complex_function(lambda z: z**2),
            run_time=6,
        )
        self.wait(2)



class IllustrationUseVennDiagram(Scene):
    def construct(self):
        title = Title("Divergence \\& Curl")
        title.to_edge(UP, buff=MED_SMALL_BUFF)

        useful_for = TexText("Useful for")
        useful_for.next_to(title, DOWN)
        useful_for.set_color(BLUE)

        fluid_flow = TexText("Fluid \\\\ flow")
        fluid_flow.next_to(ORIGIN, UL)
        ff_circle = Circle(color=YELLOW)
        ff_circle.surround(fluid_flow, stretch=True)
        fluid_flow.match_color(ff_circle)

        big_circle = Circle(
            fill_color=BLUE,
            fill_opacity=0.2,
            stroke_color=BLUE,
        )
        big_circle.stretch_to_fit_width(9)
        big_circle.stretch_to_fit_height(6)
        big_circle.next_to(useful_for, DOWN, SMALL_BUFF)

        illustrated_by = TexText("Illustrated by")
        illustrated_by.next_to(
            big_circle.point_from_proportion(3. / 8), UL
        )
        illustrated_by.match_color(ff_circle)
        illustrated_by_arrow = Arrow(
            illustrated_by.get_bottom(),
            ff_circle.get_left(),
            path_arc=90 * DEGREES,
            color=YELLOW,
        )
        illustrated_by_arrow.pointwise_become_partial(
            illustrated_by_arrow, 0, 0.95
        )

        examples = VGroup(
            TexText("Electricity"),
            TexText("Magnetism"),
            TexText("Phase flow"),
            TexText("Stokes' theorem"),
        )
        points = [
            2 * RIGHT + 0.5 * UP,
            2 * RIGHT + 0.5 * DOWN,
            2 * DOWN,
            2 * LEFT + DOWN,
        ]
        for example, point in zip(examples, points):
            example.move_to(point)

        self.play(Write(title), run_time=1)
        self.play(
            Write(illustrated_by),
            GrowArrow(illustrated_by_arrow),
            run_time=1,
        )
        self.play(
            ShowCreation(ff_circle),
            FadeIn(fluid_flow),
        )
        self.wait()
        self.play(
            Write(useful_for),
            DrawBorderThenFill(big_circle),
            Animation(fluid_flow),
            Animation(ff_circle),
        )
        self.play(LaggedStartMap(
            FadeIn, examples,
            run_time=3,
        ))
        self.wait()


class Try(Scene):
    def construct(self) -> None:
        title = Title(
            "Python vs. C",
        )
        rec = Rectangle(width=3, height=5).next_to(title, DOWN).shift(LEFT * 3).set_stroke(color=TEAL, opacity=1)
        rec.set_fill(color=TEAL, opacity=0.3)
        python = TexText("Python \\\\ A Bug for C").next_to(rec.get_top(), DOWN)

        self.play(Write(title))
        self.play(
            DrawBorderThenFill(rec),
            Write(python)
        )
