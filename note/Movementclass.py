from manimlib import * # type: ignore


def lorenz_system(t, state, sigma=10, rho=28, beta=8 / 3):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]


def ode_solution_points(function, state0, time, dt=0.01):
    solution = solve_ivp(
        function,
        t_span=(0, time),
        y0=state0,
        t_eval=np.arange(0, time, dt)
    )
    return solution.y.T

class Move(Scene):
    def construct(self):
        path = ode_solution_points(lorenz_system, [10,10,10], 30)
        circle = Circle()
        dot = GlowDot(path[0], glow_factor=1)

        graph = VMobject().set_points_smoothly(path)
        graph.scale(0.3)
        graph.center()

        self.add(dot)
        self.play(MoveAlongPath(dot, circle, run_time=5, rate_func=linear_with_scale(0.7)))


