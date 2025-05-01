from manimlib import * # type: ignore


class TransformGroup(InteractiveScene):
    def construct(self) -> None:
        bit = VGroup(*(Integer(i) for i in range(10)))
        sup = Superposition(bit.copy(), offset_multiple=0, glow_stroke_opacity=0)
        sup.generate_target()
        sup.target[2].arrange(DOWN, buff=0.5)
        sup.target[2].shift(RIGHT)

        self.add(sup)
        self.play(
            MoveToTarget(sup, run_time=2)
        )
        self.wait()
        self.play(sup.animate.set_offset_multiple(0.05).set_glow_opacity(0.5))
