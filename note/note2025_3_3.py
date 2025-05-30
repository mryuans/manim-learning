from manimlib import * # type: ignore


"""
 File: In _2023/gauss_int/integral.py, learning from line 15 to 205.
 Topic: Riemann_rectangle, flash, animation_args
 (Topic 2 start from line )
"""

class BellCurveArea(InteractiveScene):
    def construct(self):
        # Setup
        # so next time use NumberPlane() which is a sub-class Axes()
        axes = NumberPlane(
            (-4, 4), (0, 1.5, 0.5),
            width=14, height=5,
            background_line_style=dict(
                stroke_color=GREY_C,
                stroke_width=2,
                stroke_opacity=0.5
            )
        )
        axes.x_axis.add_numbers(font_size=24)
        axes.y_axis.add_numbers(num_decimal_places=1, excluding=[0]) # excluding is essential
        axes.to_edge(DOWN)
        graph = axes.get_graph(lambda x: np.exp(-x**2))
        graph.set_stroke(BLUE, 3)

        t2c = {"x": BLUE}
        graph_label = Tex("e^{-x^2}", font_size=72, t2c=t2c)
        # use pfp() to locate the label you want to use
        graph_label.next_to(graph.pfp(0.6), UR)

        self.add(axes)
        self.play(ShowCreation(graph))
        self.play(Write(graph_label))
        self.wait()

        # Show integral
        integral = Tex(R"\int_{-\infty}^\infty e^{-x^2} dx", t2c=t2c)
        integral.to_edge(UP)
    
        self.play(graph.animate.set_fill(BLUE, 0.5))
        self.wait()
        self.play(
            # use parts of Tex animated from same time
            Write(integral[R"\int_{-\infty}^\infty"]),
            # this is like TransformFromCopy()
            FadeTransform(graph_label.copy(), integral["e^{-x^2}"])
        )
        self.play(TransformFromCopy(integral["x"][0], integral["dx"]))
        self.wait()

        # Show rectangles
        colors = (BLUE_E, BLUE_D, TEAL_D, TEAL_E)
        rects = axes.get_riemann_rectangles(graph, dx=0.2, colors=colors)
        rects.set_stroke(WHITE, 1)
        rects.set_fill(opacity=0.75)
        rect = rects[len(rects) // 2 - 2].copy()
        rect.set_opacity(1)
        graph_label.set_backstroke(width=5)

        brace = Brace(rect, UP, SMALL_BUFF)
        brace.set_backstroke(width=3)
        dx_label = brace.get_tex("dx", buff=SMALL_BUFF)
        dx_label["x"].set_color(BLUE)

        axes.generate_target()
        axes.target.y_axis.numbers.set_opacity(0) # type: ignore

        self.play(
            FadeIn(rects, lag_ratio=0.1, run_time=3),
            # set_anim_args() for more dedicated animation
            # all the animation in manim is based on animation class
            # and you can set_anim_args() for them
            # rate_func: the way the animation run
            # lag_ratio: delay for a bunch of animation
            # time_span(a, b): run the animation from time a to time b 
            # path_arc: move in a arc path, according to your angles
            # path_func: self-defines a move path
            graph.animate.set_fill(opacity=0).set_anim_args(time_span=(1, 2)), # let fill_area disappear
            graph_label.animate.shift(SMALL_BUFF * UR).set_anim_args(time_span=(1, 2)), # type: ignore
        )
        self.wait()
        self.play(
            rects.animate.set_opacity(0.1),
            MoveToTarget(axes),
            FadeIn(rect),
        )
        self.wait()
        self.play(graph_label.animate.set_height(0.5).next_to(rect, LEFT, SMALL_BUFF))
        self.play(FlashAround(integral["e^{-x^2}"], time_width=1, run_time=1.5))
        self.wait()
        self.play(
            GrowFromCenter(brace),
            FadeIn(dx_label, 0.5 * UP), # type: ignore
        )
        self.play(FlashAround(integral["dx"], time_width=1, run_time=1.5))
        self.wait()

        # Show addition
        rects.set_fill(opacity=0.8)
        rects.set_stroke(WHITE, 1)
        self.play(
            LaggedStart(
                graph_label.animate.set_height(0.7).next_to(graph.pfp(0.4), UL),
                FadeOut(rect),
                *(r.animate.set_opacity(0.75) for r in rects),
                lag_ratio=0.7,
            )
        )
        self.play(rects.animate.set_opacity(0.75))
        self.wait()
        self.play(
            LaggedStart(*(
                r.animate.shift(0.25 * UP).set_color(YELLOW).set_anim_args(rate_func=there_and_back) # type: ignore
                for r in rects
            ), run_time=5, lag_ratio=0.1),
            LaggedStart(
                FlashAround(integral[2:4], time_width=1),
                FlashAround(integral[1], time_width=1),
                lag_ratio=0.25,
                run_time=5,
            )
        )
        self.wait()

        # Thinner rectangles
        for dx in [0.1, 0.075, 0.05, 0.03, 0.02, 0.01, 0.005]:
            new_rects = axes.get_riemann_rectangles(graph, dx=dx, colors=colors)
            new_rects.set_stroke(WHITE, 1)
            new_rects.set_fill(opacity=0.7)
            self.play(
                Transform(rects, new_rects),
                # about_edge could use any element 
                # compared with aligned_edge which prefers other mobs 
                brace.animate.set_width(dx * axes.x_axis.get_unit_size(), about_edge=LEFT),
                # use this to quickly express the always() meaning
                MaintainPositionRelativeTo(dx_label, brace),
            )
        self.add(graph)
        self.play(
            FadeOut(brace), FadeOut(dx_label),
            ShowCreation(graph),
        )

        # Indefinite integral
        frame = self.frame
        equals = Tex("=")
        equals.move_to(integral)
        equals.shift(0.5 * UP) # type: ignore
        answer_box = SurroundingRectangle(integral["e^{-x^2} dx"])
        answer_box.next_to(equals, RIGHT)
        answer_box.set_stroke(TEAL, 2)
        answer_box.set_fill(GREY_E, 1)
        q_marks = Tex("???")
        q_marks.set_height(0.6 * answer_box.get_height())
        q_marks.move_to(answer_box)
        answer_box.add(q_marks)

        self.play(
            frame.animate.set_height(9, about_edge=DOWN),
            integral.animate.next_to(equals, LEFT),
            FadeIn(equals),
            Write(answer_box),
        )

        integral.save_state()
        integral.generate_target()
        integral.target[1:4].stretch(0, 0, about_edge=RIGHT).set_opacity(0) # type: ignore
        integral.target[0].move_to(integral[:4], RIGHT) # type: ignore
        self.play(MoveToTarget(integral))

        # Arrows
        int_box = SurroundingRectangle(integral["e^{-x^2} dx"])
        int_box.set_stroke(BLUE, 2)
        arc = -0.5 * PI
        low_arrow = Arrow(answer_box.get_bottom(), int_box.get_bottom(), path_arc=arc)
        top_arrow = Arrow(int_box.get_top(), answer_box.get_top(), path_arc=arc)

        low_words = Text("Derivative", font_size=30)
        low_words.next_to(low_arrow, DOWN, MED_SMALL_BUFF)
        top_words = Text("Antiderivative", font_size=30)
        top_words.next_to(top_arrow, UP, MED_SMALL_BUFF)

        self.play(
            GrowArrow(low_arrow),
            FadeIn(low_words, 0.5 * LEFT), # type: ignore
            FadeTransform(answer_box.copy(), int_box, path_arc=arc)
        )
        self.wait()
        self.play(
            GrowArrow(top_arrow),
            FadeIn(top_words, 0.5 * RIGHT), # type: ignore
        )
        self.wait()

        # Impossible
        impossible = Text("Impossible!", font_size=72, color=RED)
        impossible.next_to(answer_box, RIGHT)

        functions = VGroup(
            Tex(R"a_n x^n + \cdots a_1 x + a_0", t2c=t2c),
            Tex(R"\sin(x), \cos(x), \tan(x)", t2c=t2c),
            Tex(R"b^x", t2c=t2c),
            Tex(R"\vdots")
        )
        functions.arrange(DOWN, MED_LARGE_BUFF, aligned_edge=LEFT) # type: ignore
        functions.set_height(2.5)
        functions.next_to(impossible, RIGHT, buff=LARGE_BUFF)

        self.play(FadeIn(impossible, scale=0.5, rate_func=rush_into))
        self.wait()
        self.play(
            LaggedStartMap(FadeIn, functions, shift=DOWN, lag_ratio=0.5),
            frame.animate.shift(4 * RIGHT), # type: ignore
            run_time=3
        )
        self.wait()