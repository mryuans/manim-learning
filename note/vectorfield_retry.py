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
            dx = -y
            dy = x
            vect = np.column_stack([dx, dy])
            return vect

        def ODE_system(state: np.ndarray) -> np.ndarray:
            x, y = state
            dxdt = -y
            dydt = x
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



class TransformScenn(Scene):
    def construct(self) -> None:
        def func_1(p: np.ndarray) -> np.ndarray:
            return p / 3
        
        def func_2(p: np.ndarray) -> np.ndarray:
            return p ** 2

        def func_rotate(p: np.ndarray) -> np.ndarray:
            return rotate_vector(Vect2ToVect3(p / 3), PI / 3)

        vec1 = VectorField(func_1).save_state()
        vec2 = VectorField(func_2)
        vec_rotate = VectorField(func_rotate)

        self.play(VFadeIn(vec1))
        self.play(
            Transform(vec1, vec2)
        )
        self.wait()
        self.play(
            Transform(vec1, vec_rotate)
        )

        self.play(vec1.animate.restore())
 
