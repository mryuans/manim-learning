from manimlib import *


class TexTure(Scene):
    def construct(self) -> None:
        ball = TexturedSurface(
            Sphere(),
            "map.jpg"
        )
        self.add(ball)
        self.embed()
