from manimlib import *

    
class Illustration(Scene):
    def construct(self):
        text = Text("Illustration")
        title = Text("1.3 test 27 (a)")
        axes = Axes(
            x_range=(-8, 8),
            y_range=(-8, 8),
            height=6,
            width=6,
            axis_config={
                "color": BLUE,
                },
        )

        self.play(Write(text))
        self.play(FadeOut(text))
        self.play(Write(axes))
        for c in range(1, 11):
            graph = axes.get_graph(lambda x: 0 if x <= c else (x-c)**2)
            graph.set_color(RED)
            self.play(Write(graph))
            self.wait()
        self.play(Write(title.next_to(axes, DOWN)))
        self.wait()
