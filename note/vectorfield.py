from manimlib import * # type: ignore
from numpy import ndarray


class VectorFieldExample(Scene):
    def construct(self) -> None:
        axes = NumberPlane()
        def func(p: ndarray) -> ndarray:
            p = np.array(p)
            x, y = p.T
            a, b = -4, -15
            c, d = -1, 0
            dx = a * x + b * y + 2
            dy = c * x ** 2 + 4
            vec = np.column_stack([dx, dy])
            return vec
        
        def ode(state):  # <- this is the func I wrote 
            x, y = state
            dxdt = -4 * x - 15 * y + 2
            dydt = -1 * x ** 2 + 4 
            return [dxdt, dydt]

        stream_lines = StreamLines(
            func=ode,
            coordinate_system=axes,
            density=1,
            stroke_width=2.0,
            color_by_magnitude=True,
            magnitude_range=(0, 2.0),
            color_map="3b1b_colormap",
            solution_time=4.0,
            dt=0.05,
            noise_factor=0.1,
        )
        animated_lines = AnimatedStreamLines(
            stream_lines,
            lag_range=3.0,
            rate_multiple=1.5,
            line_anim_config={
                "time_width": 1.5,
                "rate_func": linear,
            }
        )


        field = VectorField(func, axes)
        self.add(field, animated_lines)
        self.wait(10)
