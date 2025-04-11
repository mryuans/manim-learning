from manimlib import * # type: ignore


class paramSur(ThreeDScene):
    def construct(self) -> None:
        axes = ThreeDAxes()
        def surfacefunc(u, v):
            z = (5 / 9 * u ** 2 + 5 / 9 * v ** 2) ** 0.5 + 1
            if z > 0:
                return np.array([u, v, z])
            else:
                return np.array([u, v, -z])


        surface = ParametricSurface(
            surfacefunc,
            u_range=(-6, 6),
            v_range=(-6, 6)
        ).set_color(BLUE)
        mesh = SurfaceMesh(
            surface,
        )
        self.add(axes, surface, mesh)
        self.play(self.frame.animate.reorient(TAU), run_time=6)
