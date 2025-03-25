from manimlib import *
from manimlib.utils import color


class Introduction(Scene):
    def construct(self) -> None:
        intro = Text(
            """
            So, I'd like to tell you something
            about ODE
            """,
            t2c={"O": ORANGE, "D": BLUE, "E": RED})
        ordinary = Text("O").set_color(ORANGE)
        diferential = Text("D").set_color(BLUE)
        equations = Text("E").set_color(RED)
        group = VGroup(ordinary, diferential, equations).arrange(RIGHT)

        self.play(Write(intro))
        self.play(TransformMatchingParts(intro, group))
        self.play(
            group.animate.arrange(DOWN, buff=1).scale(1.3) 
            )
        self.play(group.animate.to_edge(LEFT, buff=1))
        
        diferential_text = Text(": Differential").set_color(BLUE).next_to(diferential, buff=1).scale(1.3)        
        ordinary_text = Text(": Ordinary").set_color(ORANGE).next_to(ordinary, buff=1).scale(1.3)        
        equations_text = Text(": Equations").set_color(RED).next_to(equations, buff=1).scale(1.3)        
        group_text = VGroup(diferential_text, ordinary_text, equations_text)
        self.play(Write(group_text))

class Tangent(Scene):
    a = 0
    def construct(self):
        f = lambda x: x**2
        axes = Axes(
            x_range=(-2, 2, 1),
            y_range=(-5, 5, 1),
            width=4,
            height=10,
            )

        x = axes.get_graph(f, color=BLUE)
        line = TangentLine(x, 0)
        def updater(mob, dt):
            Tangent.a += dt / 5
            line_new = TangentLine(x, Tangent.a)
            line.become(line_new)

        self.play(ShowCreation(axes), Write(x), ShowCreation(line))
        line.add_updater(updater)
        self.wait(10)

        