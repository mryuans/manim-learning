from manimlib import *


class TexTure(Scene):
    def construct(self) -> None:
        ball = TexturedSurface(
            Sphere(),
            "./images/raster/map.jpg"
        )
        self.add(ball)
