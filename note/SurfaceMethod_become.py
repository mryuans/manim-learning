from manimlib import * # type: ignore


class SurfaceMethod(InteractiveScene):
    def construct(self) -> None:
        frame = self.frame
        frame.set_height(3)
        light = self.camera.light_source

        axes = ThreeDAxes((-2, 2), (-2, 2), (0, 2))
        axes_mesh = NumberPlane((-2, 2), (-2, 2))
        
        circle = Circle(radius=1)
        sphere = Sphere(radius=1)

        sphere.set_opacity(0.5)
        sphere.set_shading(0.5, 0.5, 0.5)
        sphere.set_clip_plane(OUT, 1e-10)
        sphere.always_sort_to_camera(self.camera)

        pre_sphere = sphere.copy()
        pre_sphere.stretch(0, 2)
        pre_sphere.set_opacity(0)
        # prevent the situation where two 3D mob 
        # which will cause a wrong rendering
        pre_sphere.shift(1e-2 * IN) 

        sphere.save_state()
        sphere.become(pre_sphere)

        clip_pos = ValueTracker(1e-10)
        clip = Square3D(4)
        clip.set_opacity(0.25)
        clip.set_color(GREY)
        clip.replace(axes_mesh)
        clip.add_updater(lambda m: m.set_z(- clip_pos.get_value()))


        self.play(
            Write(axes_mesh),
            FadeIn(axes),
            ShowCreation(circle),
            FadeIn(sphere),
            FadeIn(clip),
            run_time=3
        )

        self.play(frame.animate.reorient(-34, 59, 0).set_anim_args(rate_func=smooth, run_time=2))
        self.play(Restore(sphere), run_time=4)
        self.play(frame.animate.reorient(40, 59, 0).set_anim_args(rate_func=smooth, run_time=3))
        
        sphere.add_updater(lambda m: m.set_clip_plane(OUT, clip_pos.get_value()))

        self.play(clip_pos.animate.set_value(-0.5), run_time=3)
        self.play(clip_pos.animate.set_value(1e-10), run_time=2)

        def get_strip(x0, x1, theta):
            strip = ParametricSurface(
                lambda u, v: [
                    np.cos(u),
                    np.sin(u) * np.cos(v),
                    np.sin(u) * np.sin(v),
                ],
                u_range=(math.acos(x0), math.acos(x1)),
                v_range=(0, TAU),
                shading=(0.5, 0.5, 0.5)
            )
            strip.set_color(BLUE)
            strip.always_sort_to_camera(self.camera)
            strip.set_clip_plane(OUT, 1e-10)
            strip.scale(1.001, about_point=ORIGIN)
            strip.rotate(theta, about_point=ORIGIN)
            return strip
        
        strip = get_strip(-0.2, 0, 0)
        self.play(ShowCreation(strip))
        self.play(frame.animate.reorient(-2, 94, 0, (0.31, 0.11, 0.63), 2.35), run_time=3)
        
        x0_tracker = ValueTracker(-0.2)
        strip.add_updater(lambda m: m.become(
            get_strip(
                x0_tracker.get_value(),
                x0_tracker.get_value() + 0.2,
                0
            )
        ))

        brace = Brace(strip, UP)
        brace.add(brace.get_tex(R"d", font_size=24, buff=0.05))
        brace.rotate(PI / 2, RIGHT)
        brace.add_updater(lambda m: m.next_to(strip, OUT, buff=0))
        self.play(GrowFromCenter(brace))
        self.play(x0_tracker.animate.set_value(-0.99), run_time=3)
        self.play(x0_tracker.animate.set_value(0.5), run_time=3)




