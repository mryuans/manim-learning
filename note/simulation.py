from manimlib import * # type: ignore


class Simulation(Scene):
    def construct(self) -> None:
        axes = NumberPlane()
        def div_func(p: np.ndarray) -> np.ndarray:
            return p / 3
        field_dir = VectorField(div_func, axes)
        self.play(FadeIn(field_dir))

        def curl_func(p):
            return rotate_vector(p / 3, PI / 2)
        field_curl = VectorField(curl_func, axes)
        self.play(
            ReplacementTransform(field_dir, field_curl), run_time=1
        )
