from turtle import right
from manim_imports_ext import * # type: ignore
from numpy import meshgrid

class Introduction(Scene):
    def construct(self):
        self.camera.frame.save_state()
        title = Text('''
                     The Activated Function 
                     in Deep-learning
                     ''',
                     t2c={
                         "Activated Function": RED,
                         "Deep-learning": BLUE,
                         "in ": PURPLE
                     })
        
        self.play(
            Write(title),
            )
        self.play(FlashAround(title, 1, 3, 4, TEAL))
        self.wait()
        self.play(FadeOut(title))

        putup = Text('''
                     Let's look at two example:
                     ReLU and Sigmoid
                     ''',
                     t2c={
                         "ReLU": YELLOW,
                         "Sigmoid": BLUE
                     })
        self.play(Write(putup))
        self.wait(1)
        self.play(FadeOut(putup))

        axes = Axes()
        def ReLU(x):
            if x <= 0:
                return 0
            else:
                return x
        
        graph1 = axes.get_graph(ReLU, x_range=[-8, 8, 0.1], color=YELLOW)
        label1 = Text("ReLU").next_to(graph1.pfp(0.5)).shift(RIGHT * 2).set_color(YELLOW)
        self.play(
            FadeIn(axes),
            ShowCreation(graph1),
            Write(label1),
        )
        self.wait(1)

        neg_brace = Brace(Line(axes.c2p(-6, 0), ORIGIN), buff=MED_SMALL_BUFF)
        hint1 = neg_brace.get_text(' 0 ', buff=MED_SMALL_BUFF)
        hint2 = Tex(R"\Rightarrow", font_size=72).next_to(graph1.pfp(0.6)).shift(RIGHT)
        hint2_x = Tex('x').next_to(hint2, RIGHT)
        self.play(
            FadeIn(hint1),
            Write(neg_brace),
            Write(hint2),
            Write(hint2_x),
            lag_ratio=0.5,
            )

        graph2 = axes.get_graph(
            lambda x: 1.0 / (1 + np.exp(-x)),
            x_range=[-8, 8, 0.1],
            color=BLUE,
            )
        label2 = Text("Sigmoid").next_to(graph2.pfp(0.5), RIGHT * 3).shift(UP * 1.25).set_color(BLUE)
        hint_line1 = DashedLine(axes.c2p(-8, 1), axes.c2p(8, 1)).set_color(GREEN)
        hint3 = Text(' 1 ').next_to(axes.c2p(0, 1), UL)
        hint_line2 = DashedLine(axes.c2p(-8, 0), axes.c2p(8, 0)).set_color(GREEN)
        hint4 = Text(' 0 ').next_to(ORIGIN, DL)
        formula = Tex(R"f(x)=\frac{1}{1+e^{-1}} ").shift(RIGHT * 3).shift(DOWN * 1)
        rect = SurroundingRectangle(
            formula,
            MED_SMALL_BUFF,
        ).set_stroke(TEAL, 2).set_fill(TEAL, 0.35)

        self.wait()
        self.play(
            FadeOut(hint1),
            FadeOut(hint2),
            FadeOut(neg_brace),
            FadeOut(hint2_x),
            Transform(graph1, graph2),
            TransformMatchingStrings(label1, label2),
            run_time=1.5,
        )

        self.play(
            Write(hint3),
            ShowCreation(hint_line1),
            Write(hint4),
            ShowCreation(hint_line2),
            DrawBorderThenFill(rect),
            Write(formula),
        )


class DifferentialPart(Scene):
    def construct(self):
        title = Text('''
                     Let's find the answer 
                     in their differential function
                     ''',
                     t2c={
                         'differential function':TEAL 
                     }
        )
        axes = Axes()
        graph1 = axes.get_graph(lambda x: 0 if x <= 0 else 1, x_range=[-8, 8, 0.01]).set_color(YELLOW)
        label1 = Text('First order differential of ReLU',t2c={'ReLU': YELLOW}).scale(0.5).next_to(ORIGIN, UL * 3)
        explain = Text('''
                       The difference between 
                       huge and small statstic
                       data is obvious after the
                       backpropregation.
                       ''',
                       t2c={
                           'huge': RED,
                           'small': BLUE,
                           'backpropregation': TEAL
                       }
        ).next_to(label1, DOWN * 5).scale(0.5)

        rect = SurroundingRectangle(
            explain,
            MED_SMALL_BUFF,
        ).set_stroke(TEAL, 2).set_fill(TEAL, 0.35)

        
        graph2 = axes.get_graph(lambda x: np.exp(-x) / (1 + np.exp(-x))**2).set_color(BLUE)
        label2 = Text('First order differential of Sigmoid', t2c={'Sigmoid': BLUE}).scale(0.5).next_to(ORIGIN, UL * 3)
        formula = Tex(R"f'(x)=\frac{e^{-x}}{1+e^{-x^2}}").next_to(ORIGIN, UR * 3)
        explain_2 = Text('''
                         However, obviously, the
                         Sigmoid function doesn't
                         have such property.
                         ''',
                        t2c={
                            'Sigmoid': BLUE
                        }
        ).next_to(formula, DOWN * 5).scale(0.5)
        rect2 = SurroundingRectangle(
            explain_2,
            MED_SMALL_BUFF,
        ).set_stroke(TEAL, 2).set_fill(TEAL, 0.35)
        
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))

        self.play(
            FadeIn(axes),
            ShowCreation(graph1),
            Write(label1),
            )
        self.wait()
        self.play(
            DrawBorderThenFill(rect),
            Write(explain)
        )

        self.wait(1)

        self.play(
            Transform(graph1, graph2),
            Transform(label1, label2),
            Write(formula),
            FadeOut(rect, RIGHT),
            FadeOut(explain, RIGHT),
            run_time=2
        )

        self.play(
            DrawBorderThenFill(rect2),
            Write(explain_2)
        )


class ThreeDExplaining(ThreeDScene):
    def construct(self):
        self.frame.add_updater(lambda m: m.reorient(20 * math.cos(0.5 * self.time), 75)) # type: ignore
        axes = ThreeDAxes()
        graph = axes.get_graph(
            lambda u, v: 1 / (1 + np.exp(-(u + v)))
        )
        mesh = SurfaceMesh(
            graph,
            resolution=(31, 11),
        )
        graph.always_sort_to_camera(self.camera)
        self.add(axes, graph, mesh)
        self.wait(10)
        pass

        