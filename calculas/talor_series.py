from manimlib import * # type: ignore


def talorfunc_generator(f, n: int):
	g = lambda x: f(x) + x ** n / math.factorial(n)
	return g


class Talor(Scene):
	def construct(self):
		axes = Axes(
			x_range=(-8, 8, 1),
			y_range=(-2, 8, 1),
			height=6,
			width=10,
			axis_config=dict(include_tip=True),
		)
		label_x = axes.get_x_axis_label("x")
		label_y = axes.get_y_axis_label("y")
		group = VGroup(axes, label_x, label_y)

		orders_input = 21
		orders_count = Text("order")
		orders = ValueTracker(1)
		text_group = VGroup(orders_count, text:= Text(f'{orders.get_value():.0f}').next_to(orders_count, LEFT)).to_corner(UR)

		ex = axes.get_graph(lambda x: math.e ** x)
		name = Tex("f(x)=e^x").next_to(text_group, DL, buff=1.5)
		ex.set_stroke(BLUE, 5)
		colors = color_gradient([BLUE_E, GOLD_A, RED_A][::-1], orders_input)

		self.play(Write(text_group))
		self.play(ShowCreation(group))
		self.play(ShowCreation(ex), Write(name))

		f = lambda x: x + 1
		graph_x = axes.get_graph(f)
		graph_x.set_color(RED)
		self.play(ShowCreation(graph_x))

		for n, color in zip(range(2, orders_input + 1), colors):
			orders.set_value(n)
			y = Text(f'{orders.get_value():.0f}').next_to(orders_count, LEFT)
			g = talorfunc_generator(f, n)
			graph_y = axes.get_graph(g)
			graph_y.set_color(color)
			self.play(ReplacementTransform(graph_x, graph_y), 
				TransformMatchingTex(text, y, run_time=2))
			text = y
			f = g
			graph_x = graph_y

		self.wait(5)
