from manimlib import * # type: ignore


class VectorFieldRetry(Scene):
    def construct(self) -> None:
        magnitude_range=(0, 4)
        time_width=0.3
        axes = NumberPlane(
            x_range=(-TAU, 5 * PI, PI),
            y_range=(-4.5, 4.5, 2),
            width=FRAME_WIDTH,
            height=FRAME_HEIGHT
        )
        def vector_func(state: np.ndarray) -> np.ndarray:
            state = np.array(state).T
            x, y = state[:2]
            dx = y
            dy = np.sin(x)
            vect = np.column_stack([dx, dy])
            return vect

        vec = VectorField(
            vector_func, 
            axes,
            magnitude_range=magnitude_range,
            density=4
        )
        stream_lines = StreamLines(
            func=vector_func,
            coordinate_system=axes,
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


class Test(Scene):
    def construct(self) -> None:
        def func(p):
            return p / 3

        def func_2(p):
            return rotate_vector(v223(p / 3), PI / 3)
        # field1 = VectorField(func)
        # field2 = VectorField(func_2)
        # lines = StreamLines(func)
        # lines_2 = StreamLines(func_2)
        # animation = AnimatedStreamLines(lines)
        # animation_2 = AnimatedStreamLines(lines_2)
        # self.add(animation, field1)
        # self.wait(2)
        # self.play(
        #     ReplacementTransform(animation, animation_2),
        #     Transform(field1, field2)
        # )

        def get_vector_field_and_stream_lines(
            func, coordinate_system,
            magnitude_range=(0.5, 4),
            vector_opacity=0.75,
            vector_thickness=0.03,
            color_by_magnitude=False,
            line_color=GREY_A,
            line_width=3,
            line_opacity=0.75,
            density=1.0,  # Changed from sample_freq to density
            n_samples_per_line=10,
            arc_len=3,
            time_width=0.3,
        ):
            vector_field = VectorField(
                func, coordinate_system,
                magnitude_range=magnitude_range,
                stroke_opacity=vector_opacity,  # Changed from vector_config
                stroke_width=vector_thickness,  # Changed from vector_config
            )
            stream_lines = StreamLines(
                func, coordinate_system,
                density=density,  # Changed from step_multiple to density
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
                    "time_width": time_width,
                },
            )

            return vector_field, animated_lines
        
        field1, stream_lines1 = get_vector_field_and_stream_lines(func, NumberPlane())
        field2, stream_lines2 = get_vector_field_and_stream_lines(func_2, NumberPlane())
        self.add(field1, stream_lines1)
        self.wait(2)
        self.play(
            ReplacementTransform(stream_lines1, stream_lines2),
            Transform(field1, field2)
        )
        self.wait(2)
