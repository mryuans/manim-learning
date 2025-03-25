from manimlib import *
from pyautogui import resolution


class TexAndPlane(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.frame.reorient(43, 76, 1, IN, 10)

        sphere = Sphere(radius=3).set_color(BLUE)

        pos = sphere.get_center()
        mesh = SurfaceMesh(sphere, (31, 31))


        self.play(
            ShowCreation(mesh),
            ShowCreation(sphere),
            ShowCreation(axes)
            )
        
        self.play(self.frame.animate.reorient(430, 76, 1, IN, 10), run_time=10, rate_func=there_and_back)
        self.play(self.frame.animate.reorient(*pos), run_time=5, rate_func=there_and_back)