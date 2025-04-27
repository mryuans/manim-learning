from manimlib import * # type: ignore


def get_dot(
        pos,
        radius=0.05, 
        color=random_bright_color(), 
        glow_factor=1.5,
        light_density=3
    ):
    light = GlowDot(pos, radius=radius * light_density, color=color, glow_factor=glow_factor)
    dot = TrueDot(pos, radius=radius, color=color)
    return Group(light, dot)


class TableAndChangeable(InteractiveScene):
    def construct(self) -> None:
        axes = Axes(
            x_range=(0, 1, 0.1),
            y_range=(0, 1, 0.1),
            height=4,
            width=4,
        )

        axes.shift(RIGHT * 3)
        axes.get_x_axis_label("x proportion")
        axes.get_y_axis_label("y proportion")
        rec = Square(side_length=4)
        rec.set_stroke(GREY, 0.3)
        rec.move_to(axes.get_center())
        rec.shift(UR * 0.05)

        x_p = ValueTracker(0.00)
        y_p = ValueTracker(0.00)

        example = get_example_loop(2)
        example.shift(LEFT * 3)
        pos = example.get_start()
        dot1 = get_dot(pos, color=YELLOW)
        dot2 = get_dot(pos, color=PURPLE)
        dot1.add_updater(lambda m: m.move_to(example.pfp(x_p.get_value())))
        dot2.add_updater(lambda m: m.move_to(example.pfp(y_p.get_value())))

        label1 = DecimalNumber(0, font_size=24)
        label1.set_color(YELLOW)
        label1.add_updater(lambda m: m.set_value(x_p.get_value()))
        label1.set_backstroke(BLACK)
        label1.always.next_to(dot1, UR, buff=-0.1)

        label2 = DecimalNumber(0, font_size=24)
        label2.set_color(PURPLE)
        label2.add_updater(lambda m: m.set_value(y_p.get_value()))
        label2.set_backstroke(BLACK)
        label2.always.next_to(dot2, UL, buff=-0.1)
        
        pos_dot = get_dot(axes.c2p(0, 0))
        pos_dot.add_updater(lambda m: m.move_to(axes.c2p(x_p.get_value(), y_p.get_value())))
        label = Tex(R"(0.00, 0.00)", font_size=24)
        coordins = label.make_number_changeable(0.00, replace_all=True)
        coordins[0].f_always.set_value(x_p.get_value)
        coordins[1].f_always.set_value(y_p.get_value)
        label.always.next_to(pos_dot.get_center(), UR, buff=0.1)
        tip_x = ArrowTip(angle=-90 * DEG)
        tip_x.set_height(0.2)
        tip_x.add_updater(lambda m: m.move_to(axes.c2p(x_p.get_value(), 0), UP))
        tip_x.set_color(YELLOW)
        tip_y = ArrowTip(angle=- PI)
        tip_y.set_height(0.2)
        tip_y.add_updater(lambda m: m.move_to(axes.c2p(0, y_p.get_value()), RIGHT))
        tip_y.set_color(PURPLE)

        x_line = always_redraw(lambda: Line(
            pos_dot.get_center(), axes.c2p(x_p.get_value(), 0)
        ))
        y_line = always_redraw(lambda: Line(
            pos_dot.get_center(), axes.c2p(0, y_p.get_value())
        ))

        self.play(
            ShowCreation(example),
            FadeIn(rec),
            FadeIn(axes),
        )

        self.play(
            FadeIn(dot1),
            FadeIn(dot2),
            FadeIn(pos_dot),
            FadeIn(tip_x),
            FadeIn(tip_y),
            ShowCreation(x_line),
            ShowCreation(y_line)
        )

        self.play(
            tip_x.animate.flip(LEFT, about_edge=DOWN),
            tip_y.animate.flip(UP, about_edge=LEFT),
        )

        self.play(
            FadeIn(label1, DL),
            FadeIn(label2, DL),
            FadeIn(label, DL)
        )

        self.play(
            x_p.animate.set_value(0.5),
            y_p.animate.set_value(0.75),
            run_time=5
        )

        self.play(
            x_p.animate.set_value(0.20),
            y_p.animate.set_value(0.10),
            run_time=5
            
        )

