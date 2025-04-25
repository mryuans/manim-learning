from manimlib import * # type: ignore


class FatherAndSon(InteractiveScene):
    def construct(self):
        axes = NumberPlane()
        bulb = SVGMobject("light_bulb")
        bulb.set_color(YELLOW)
        dot = GlowDot(bulb.get_center())
        text = Text("Idea").next_to(bulb, DOWN)
        bulb.set_z_index(1)

        self.play(ShowCreation(bulb), Write(text), Write(axes))
        bulb.add(text)
        self.play(
            dot.animate.set_radius(3),
            lag_ratio=1
        )

        self.play(
            Group(bulb, dot).animate.shift(RIGHT * 6).set_anim_args(path_arc= - PI / 3),
            self.frame.animate.set_x(6),
            run_time=4,
            rate_func=there_and_back_with_pause
        )

