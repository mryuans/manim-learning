from manim_imports_ext import * # type:ignore


class BarsThings(InteractiveScene):
    def construct(self) -> None:
        h_line = Line(LEFT, RIGHT)
        h_line.set_width(5)
        h_line.shift(DOWN * 2 + RIGHT * 3)
        
        digits = np.random.uniform(0, 1, 6)
        digits = np.random.shuffle(digits)

        prob_bar_group = VGroup()
        for _ in range(3):
            prob_bar = VGroup()
            digits = np.random.uniform(0, 1, 6)
            # np.random.shuffle(digits)
            for digit in digits:
                bar = Rectangle(width=5 / 6.3, height=3 * digit)
                bar.set_fill(interpolate_color(BLUE_D, GREEN, digit * 1.5), 1)
                bar.set_stroke(width=0.1)
                prob_bar.add(bar)
            prob_bar.arrange(RIGHT, buff=0)
            prob_bar.match_x(h_line)
            for mob in prob_bar:
                mob.align_to(h_line, DOWN)
            prob_bar_group.add(prob_bar)
        self.add(h_line)


        img = ImageMobject('image')
        img.shift(LEFT * 2)
        lines = VGroup(
            *(Line(img, prob) for prob in prob_bar)
        )
        for line in lines:
            line.insert_n_curves(20)
            color = random_bright_color(hue_range=(0.3, 0.4))
            line.set_stroke(color, [2, 4, 4, 2], opacity=1)
        self.play(GrowFromCenter(img))

        self.play(
            LaggedStartMap(GrowFromEdge, prob_bar_group[0], edge=DOWN, lag_ratio=0.2),
            LaggedStartMap(VShowPassingFlash, lines, lag_ratio=0.2),
        )

        for prob in prob_bar_group[1:]:
            self.play(
                Transform(prob_bar_group[0], prob),
                LaggedStartMap(VShowPassingFlash, lines),
            )
            

