from manimlib import * # type: ignore


class VectorFieldRetry(Scene):
    def construct(self) -> None:
        magnitude_range=(0.5, 4)
        color_by_magnitude=False
        line_color=GREY_A
        line_width=3
        line_opacity=0.75
        n_samples_per_line=10
        arc_len=3
        time_width=0.3
        axes = NumberPlane(
            x_range=(-10, 10, 1),
            y_range=(-10, 10, 1),
            width=7,
            height=7
        )
        def vector_func(state: np.ndarray) -> np.ndarray:
            state = np.array(state).T
            x, y = state[:2]
            dx = x
            dy = y
            vect = np.column_stack([dx, dy])
            return vect

        def ODE_system(state: np.ndarray) -> np.ndarray:
            x, y = state
            dxdt = x
            dydt = y
            return np.array([dxdt, dydt])

        vec = VectorField(
            vector_func, 
            axes,
            density=1
        )
        stream_lines = StreamLines(
            func=ODE_system,
            coordinate_system=axes,
            n_samples_per_line=n_samples_per_line,
            arc_len=arc_len,
            magnitude_range=magnitude_range,
            color_by_magnitude=color_by_magnitude,
            stroke_color=line_color,
            stroke_width=line_width,
            stroke_opacity=line_opacity,        
        )
        animated_lines = AnimatedStreamLines(
            stream_lines,
            line_anim_config={
                "time_width": time_width
            }
        )
        self.add(vec, animated_lines)
        self.wait(10)

