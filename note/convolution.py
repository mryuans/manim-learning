from manimlib import * # type: ignore


class ConvolutionGraph(Scene):
    def construct(self) -> None:
        height = (FRAME_HEIGHT - 2) / 3
        width = FRAME_WIDTH - 2
        axes3, axes2, axes1 = axes = Axes(
            height=height,
            width=width,
        ).get_grid(3, 1)
        
        func = lambda x: np.exp(-(x ** 2))
        graph1 = axes1.get_graph(np.sin)
        graph1.set_stroke(BLUE)
        graph2 = axes2.get_graph(func)
        graph2.set_stroke(RED)

        x_samples = np.arange(*axes1.x_range[:2], 0.05)
        convo_prod = np.convolve(np.sin(x_samples), func(x_samples), mode="same") * 0.05
        graph3 = VMobject().set_points_smoothly(axes3.c2p(x_samples, convo_prod)).set_stroke(GREEN)

        self.add(axes)
        self.play(
            ShowCreation(graph1),
            ShowCreation(graph2)
        )
        self.wait()

        self.play(
            TransformFromCopy(graph1, graph3),
            TransformFromCopy(graph2, graph3)
        )
        
        x = ValueTracker(axes1.x_range[0])
        x_get = x.get_value
        dot1 =  GlowDot()
        dot2 =  GlowDot()
        dot3 =  GlowDot()

        dot1.add_updater(lambda d: d.move_to(axes1.i2gp(x_get(), graph1)))
        dot2.add_updater(lambda d: d.move_to(axes2.i2gp(x_get(), graph2)))
        self.add(dot1, dot2, dot3)
        self.play(x.animate.set_value(axes1.x_range[1]).set_anim_args(rate_func=linear, run_time=7))
        



