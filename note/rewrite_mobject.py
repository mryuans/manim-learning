from manimlib import * # type: ignore


def get_rose_pattern(k, colors=[BLUE, WHITE, BLUE]):
    return RosePattern(k=k).set_color_by_gradient(*colors)


class RosePattern(VMobject):
    def __init__(
        self,
        radius: float = 2,
        k: float = 3,
        theta_range=TAU,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.k = k
        self.radius = radius

        step_size = 0.05
        theta = np.arange(0, theta_range + step_size, step_size)

        points = [
            [
                radius * np.cos(k * t) * np.cos(t),
                radius * np.cos(k * t) * np.sin(t),
                0
            ] for t in theta
        ]

        self.set_points_smoothly(points)
       

class Showing_1(Scene):
    def construct(self) -> None:
        
        rose = RosePattern(k=10)
        
        self.play(ShowCreation(rose), run_time=5)
        self.wait()


class ShowingWithUpdater(Scene):
    def construct(self) -> None:
        rose = get_rose_pattern(k=0)
        rose.k = 0
        
        self.play(ShowCreation(rose))

        def update_func(mob: RosePattern, dt):
            mob.k += dt
            new_pat = get_rose_pattern(k=mob.k)
            mob.become(new_pat)

        rose.add_updater(update_func)
        self.wait(5)



class ShowingWithUpdater_And_ValueTracker(Scene):
    def construct(self) -> None:
        track_k = ValueTracker(0)
        rose = get_rose_pattern(k=track_k.get_value())

        self.play(ShowCreation(rose))

        self.play(
            UpdateFromFunc(
                rose, lambda pat: pat.become(
                    get_rose_pattern(k=track_k.get_value())
            )),
            track_k.animate.set_value(10),
            run_time=5
        )
