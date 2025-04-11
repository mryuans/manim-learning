from manimlib import * # type: ignore


class Lessorshot(Scene):
    def construct(self) -> None:
        title = Tex(
        R'''
        Lissajous\ Curve \\
        x=3sin(2t+\pi/4) \\
        y=3sin(3t)
        ''',
            t2c={
                "x": BLUE,
                "y": RED,
                "t": YELLOW
                }
        ).scale(0.5).to_corner(UR)
        origin = Text(
            "O",
            t2s={
                "O":ITALIC
            }
        ).next_to(ORIGIN, DL)
        axes = Axes()
        dotx = Dot(axes.c2p(0, 1)).set_color(BLUE)
        doty = Dot(ORIGIN).set_color(RED)
        dot_lessor = Dot(axes.c2p(0, 1)).set_color(YELLOW)
        graph = ParametricCurve(
            lambda t: np.array([
                3 * np.sin(2 * t + PI / 4),
                3 * np.sin(3 * t),
                0
            ]),
            t_range=(0, TAU, 0.01)
        )
        def update(dot):
            dot.move_to(axes.c2p(
                3 * np.sin(2 * self.time / 2 + PI / 4),
                3 * np.sin(3 * self.time / 2)
            ))
        
        def updatex(dot):
            dot.move_to(axes.c2p(
                3 * np.sin(2 * self.time / 2 + PI / 4),
                0
            ))

        def updatey(dot):
            dot.move_to(axes.c2p(
                0,
                3 * np.sin(3 * self.time / 2)
            ))

        dot_lessor.add_updater(update)
        dotx.add_updater(updatex)
        doty.add_updater(updatey)
        linex = always_redraw(lambda: DashedLine(dotx.get_center(), dot_lessor.get_center()))
        liney = always_redraw(lambda: DashedLine(doty.get_center(), dot_lessor.get_center()))
        self.add(dot_lessor, doty, dotx, linex, liney, axes, graph, origin)
        self.play(Write(title))
        self.wait(10)

         
