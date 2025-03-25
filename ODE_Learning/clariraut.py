from manimlib import * # type: ignore


class Clariaut(Scene):
    def construct(self):
        tab = NumberPlane()
        # tab.center()
        graph = tab.get_graph(lambda x: -x**2/2)
        c_ = np.arange(-4, 4, 0.5)
        def linechange(c):
            new_line = tab.get_graph(lambda x: c*x + c**2/2)
            new_line.set_color(YELLOW)
            return new_line
        
        self.add(tab)
        self.add(graph)
        self.play(LaggedStartMap(
            GrowFromCenter, 
            VGroup(linechange(c) for c in c_),
            lag_ratio=0.9,
            run_time=4
        ))        
        circle = Circle()
