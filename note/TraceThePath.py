from manimlib import * # type: igonre


class SinCurve(InteractiveScene):
    def construct(self):
        pos = ValueTracker()
        axes = Axes(
            (0, TAU, PI / 2), 
            (-1.2, 1.2, 0.3),
            height=FRAME_HEIGHT / 3,
            width=FRAME_WIDTH / 2.5
        )
        axes.shift(RIGHT * 2)
        
        get_v = pos.get_value
        dot = Dot()
        dot.add_updater(
            lambda m: m.move_to([
                np.sin(get_v()) - 3,
                np.cos(get_v()),
                0
            ])
        )
        path = TracedPath(
            dot.get_center
        )
        path_axes = TracedPath(
            lambda: axes.c2p(
                get_v(),
                np.cos(get_v())
            ),
            stroke_color=YELLOW,
            stroke_width=4
        )
        self.add(dot, path, axes, path_axes)
        self.play(pos.animate.set_value(PI * 2), run_time=4)


