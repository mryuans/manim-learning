from manimlib import *


class Screen(Scene):
    def construct(self) -> None:
        framewidth = (FRAME_WIDTH - 2) / 2.
        frameheight = (FRAME_HEIGHT - 3) / 1.2

        title = Title("Screen")
        background = FullScreenRectangle()
        background.set_fill(MAROON)
        screen1, screen2 = frames = Rectangle(
            framewidth,
            frameheight
        ).replicate(2)
        frames.set_fill(BLACK, 1)
        frames.set_stroke(WHITE, 2)
        frames.arrange(RIGHT, buff=1)

        # Write in this way is also acceptable
        # screen1, screen2 = screens = VGroup(
                # Rectangle().set_fill(BLACK) for _ in [1, 2])
        matrice1 = WeightMatrix()
        matrice1.match_height(screen1)
        matrice1.match_width(screen2)
        matrice1.scale(0.8)
        matrice1.move_to(screen1.get_center())

        layers1, layers2 = VGroup(
            Dot(radius=frameheight / 60).set_fill(WHITE, 1).get_grid(n, 1, buff=(frameheight - 1) / 20) for n in [6, 10]
        )
        layers2.arrange(DOWN, buff=SMALL_BUFF)
        layers2.next_to(screen2.get_right(), LEFT * 2)
        layers1.next_to(screen2.get_left(), RIGHT * 2)
        layers1.set_stroke(WHITE, 0.05)
        lines = get_network_connections(layers1, layers2)

        self.add(background)
        self.add(frames)
        self.play(
            LaggedStartMap(Write, VGroup(title, matrice1), lag_ratio=0.1, run_time=3),
            FadeIn(layers1),
            FadeIn(layers2),
            Write(lines)
            )
        for _ in range(5):
            self.play(
                RandomizeMatrixEntries(matrice1),
                Write(lines.copy()),
                LaggedStart(*(neurons.animate.set_fill(opacity=random.random()) for neurons in layers1))
            )
