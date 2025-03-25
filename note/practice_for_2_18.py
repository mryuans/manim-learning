from manim_imports_ext import * # type: ignore


class Surface_line(ThreeDScene):
    def construct(self):
        c_tracker = ValueTracker(1)
        get_c = c_tracker.get_value()
        text = Tex(
            'x+y-1·z=1',
            t2c={
                'x': RED,
                'y': BLUE,
                'z': GREEN
            }
            )
        text.to_corner(UL).fix_in_frame()
        text.make_number_changeable("1")
        text.add_updater(lambda m: m[-1].set_value(get_c()))
        self.frame.add_updater(lambda m, dt: m.reorient(30 * np.cos(0.1 * dt), 75)) # type: ignore
        axes = ThreeDAxes(
            x_range=(-6, 6, 1),
            y_range=(-6, 6, 1),
            z_range=(-6, 6, 1),
        )
        # x + y - c * z = 1
        sur = axes.get_graph(
            lambda u, v: u + v - 1, 
            BLUE_E, 
            0.7,
            (-5, 5),
            (-5, 5),
            )
        sur.always_sort_to_camera(self.camera)
        mesh = SurfaceMesh(sur)
        plane = Group(sur, mesh)
        self.play(Write(text))
        self.add(axes, plane)

        def get_graph(c):
            plane = axes.get_graph(
                lambda u, v: (u + v - 1) / c, 
                BLUE_E, 
                0.7,
                (-5, 5),
                (-5, 5),
            )
            plane.always_sort_to_camera(self.camera)
            mesh = SurfaceMesh(plane)
            return Group(plane, mesh)

        for value in [-0.5, -0.8, -0.3, -1.0, -0.3, 0.05, 0.1, -0.3, -1.0, -0.7, -1.0]:
            new_graph = get_graph(value)
            c_tracker.set_value(value)
            self.play(
                Transform(plane, new_graph),
                run_time=3
            )
            self.wait()