from manimlib import * # type: ignore

 

class Pendulum_animation(Scene):
    L = 2.5
    m = 1
    g = 9.8
    theta = 90 * DEGREES
    omega = np.sqrt(g / L)
    def construct(self):
        label = Tex(R"\theta=100").to_corner(UL)
        parameter = Text(
            '''
            L = 2.5 
            g = 9.8 
            m = 1
            '''
        ).next_to(label, DOWN)
        label.make_number_changeable("100")
        l = self.L
        m = self.m
        init_degrees = self.theta
        
        init_pos = np.array([
            l * np.sin(init_degrees),
            -l * np.cos(init_degrees),
            0
        ])
        handle = Dot(ORIGIN).set_color(YELLOW)
        dot = Dot(init_pos, radius=0.25).set_color(MAROON)

        line = always_redraw(
            lambda: Line(np.array([0, 0, 0]), dot.get_center()).set_stroke(WHITE, 1)
        )
        trace = TracingTail(dot, time_traced=1).set_stroke(BLUE, 1)

        self.add(handle, dot, line, label, parameter, trace)
        value = ValueTracker(self.theta)

        def updater(pendulum, dt):
            t = self.time
            theta = self.theta * np.cos(self.omega * t)  # 小角度解析解
            value.set_value(theta)
            new_end = self.L * np.array([
                np.sin(theta), 
                -np.cos(theta), 
                0
            ])
            pendulum.move_to(new_end)
            label[-1].set_value(value.get_value() * 60)

        dot.add_updater(updater)
        self.wait(10)

