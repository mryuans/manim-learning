from manimlib import *


class TimeVarying(Scene):
    def construct(self):
        axes = NumberPlane()
        def func(p, t):
            x, y = p.T[:2]
            dx = -x + np.cos(t) + x * y
            dy = y + np.sin(t) * x
            scale = 0 + np.sin(0.5 * t)
            vec = np.column_stack([dx, dy])
            return vec * scale

        field = TimeVaryingVectorField(
            func, 
            axes,
            density=2,
            magnitude_range=(0, 5),
            stroke_width=3
        )
        self.add(field)
        self.wait(10)
