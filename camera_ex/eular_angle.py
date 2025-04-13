from manimlib import * # type: ignore


class EularAngle(ThreeDScene):
    def construct(self) -> None:
        axes_rotating = ThreeDAxes().set_stroke(width=6)
        
        self.add(axes_rotating)
        self.play(axes_rotating.animate.set_color(RED))
        
        self.play(self.frame.animate.reorient(60, 45).set_anim_args(rate_func=there_and_back), run_time=3)
        self.play(self.frame.animate.reorient(-60, 45).set_anim_args(rate_func=there_and_back), run_time=3)
    

