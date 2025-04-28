from manimlib import * # type: ignore


class MakeNumberChange(InteractiveScene):
    def construct(self):
        axes = NumberLine(
            (-1, 1, 0.1),
            width=FRAME_WIDTH - 3,
            tick_size=0.05,
            decimal_number_config=dict(
                num_decimal_places=1,
                font_size=24
            )
        )
        axes.add_numbers()

        dot = GlowDot()
        dot.add_updater(lambda m: m.move_to(axes.n2p(np.sin(self.time))))

        label = Tex(R"Postion:-0.01")
        label.next_to(axes, DOWN)
        coord = label.make_number_changeable(-0.01)
        # coord.add_updater(lambda d: d.set_value(axes.p2n(dot.get_center())))
        coord.add_updater(lambda d: d.set_value(np.sin(self.time)))

        self.add(axes, label, dot)
        self.wait(3)
