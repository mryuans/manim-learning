from manimlib import * # type: ignore


class MLPneuros(Scene):
    def construct(self) -> None:
        radius = 0.15
        layers1, layers2 = layers = VGroup(
            Dot(radius=radius).get_grid(n, 1, buff=radius/2)
            for n in [8, 16]
        ) 
        layers2.arrange(DOWN, buff=radius)
        layers.arrange(RIGHT, buff=3.0)
        layers.set_stroke(WHITE, 1)
        for neuron in layers1:
            neuron.set_fill(opacity=random.random())
        layers2.set_fill(opacity=0)
        self.add(layers)

        connections = get_network_connections(layers1, layers2)
        self.play(Write(connections))
        
        self.play(
            LaggedStart(*(neuron.animate.set_fill(YELLOW, opacity=1).set_anim_args(rate_func=there_and_back) for neuron in layers1),lag_ratio=0.1),
            LaggedStart(*(
            connect.animate.set_stroke(YELLOW, 5).set_anim_args(rate_func=there_and_back) for connect in connections
        ),lag_ratio=0.1), run_time=8)


class Matrices(Scene):
    def construct(self) -> None:
        matrice = WeightMatrix()
        self.play(Write(matrice))
