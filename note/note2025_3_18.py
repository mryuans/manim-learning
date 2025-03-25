from manim_imports_ext import * # type: ignore
from pyautogui import resolution # type: ignore


"""
 Topic: camera, Tex, ThreeDSurface
"""

class Camera_set(ThreeDScene):
    def construct(self):
        mob = Sphere(radius=3).set_color_by_gradient(BLUE, GREEN)
        mesh = SurfaceMesh(mob, resolution=(31, 31))
        self.add(mob, mesh)
        
        # self.frame will control the frame of the whole anim
        self.frame.reorient(43, 76, 1, IN, 10)

        # there is two method to spin the camera
        self.play(
            self.frame.animate.reorient(430, 436, 361),
            run_time=15,
            rate_func=there_and_back
        )

        # worth mentioning: the updater is always connected with the time system
        # like self.time self.wait
        self.frame.add_updater(lambda m, dt: m.increment_theta(dt * 3 * DEGREES)) # type: ignore
        self.wait(5)

# still under writing
class Tex_set(ThreeDScene):
    def construct(self):
        text1 = Tex(
            R"""
            \begin{aligned} 
            \frac{\mathrm{d} z}{\mathrm{~d} t} & =x y-\beta z
            \end{aligned}
            """,
            t2c={
                'x': RED,
                'y': GREEN,
                'd': BLUE,
            },
            font_size=40
        )
        self.play(Write(text1))


# draw the surface pic
class Surface_note(ThreeDScene):
    def construct(self):
        self.frame.reorient(60, 60, 60)
        def gear_torus(u, v):
            R = 3.0  # 主半径
            r = 1.0  # 副半径（基圆半径）
            a = 0.3  # 齿深
            n = 10   # 齿数
            
            modulated_r = r + a * np.sin(n * v)
            x = (R + modulated_r * np.cos(u)) * np.cos(v)
            y = (R + modulated_r * np.cos(u)) * np.sin(v)
            z = modulated_r * np.sin(u)
            return np.array([x, y, z])
        
        def param_func(u, v):
            R = 3.0  # 主半径
            a = 1.0  # 双纽线振幅
            x = (R + a * np.cos(u)) * np.cos(v)
            y = (R + a * np.cos(u)) * np.sin(v)
            z = a * np.sin(u) * np.cos(u)
            return np.array([x, y, z])
        
        surface_1 = ParametricSurface(
            gear_torus,
            u_range=(0, np.pi*2),
            v_range=(0, np.pi*2),
            resolution=(200, 200),
        ).set_color(GOLD_C, 0.5)

        mesh_1 = SurfaceMesh(
            surface_1,
            resolution=(31, 31)
        )

        surface_2 = ParametricSurface(
            param_func,
            u_range=(0, np.pi*2),
            v_range=(0, np.pi*2),
            resolution=(200, 200),
            
        ).set_color(BLUE, 0.5)

        mesh_2 = SurfaceMesh(
            surface_2,
            resolution=(31, 31)
        )

        self.add(surface_1, mesh_1)
        self.wait(2)
        self.play(
            Transform(surface_1, surface_2),
            Transform(mesh_1, mesh_2), 
            run_time=10, 
            rate_func=there_and_back
            )

