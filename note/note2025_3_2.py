from manim_imports_ext import * # type: ignore


"""
 2025/3/2 Topic 1:
 File: In _2023/gauss_int/herschel.py, learning from line 1091 to 1230.
 Topic: Three-D Graph, surface, update-animation and camera knowledge
 (Topic 2 start from line 172)
"""

# Let's start from two base_function class:
class VariableC(InteractiveScene):
    # set c for animation
    c_values = [1.0, 0.5, -1.0, -0.7, -0.5, 0.25, -0.2, -0.4, -0.9, -0.1, 0.5, 0.3, 0.1]

    def construct(self):
        axes = self.get_axes()
        self.add(axes)

        curve = axes.get_graph(lambda x: self.func(x, 1))
        curve.set_stroke(RED, 3)
        self.add(curve)

        label = self.get_label(axes)
        self.add(label)

        c_tracker, c_interval, c_tip, c_label = self.get_c_group()
        get_c = c_tracker.get_value

        # some tiny position changes for the numberline
        c_interval.move_to(axes, UR)
        c_interval.shift(0.5 * DOWN) # type: ignore
        self.add(c_interval, c_tip, c_label)

        axes.bind_graph_to_func(curve, lambda x: self.func(x, get_c())) # let the curve always changes follow the c

        # Animate
        for c in self.c_values:
            self.play(c_tracker.animate.set_value(c), run_time=2) # so you see how to use valuetracker
            self.wait()

    def get_c_group(self):
        c_tracker = ValueTracker(1) 
        # ValueTracker is supported for the animation
        # Usually, we use valuetracker.animate.sett_value() to play animation
        get_c = c_tracker.get_value

        c_interval = NumberLine(
            (-1, 1, 0.25), width=3, tick_size=0.05, big_tick_numbers=[-1, 0, 1],
        ) # big_tick_number for -1, 0, 1, which is literaly but worth your attention.
        c_interval.set_stroke(WHITE, 1) # remember "stroke", "fill" attri. for mobject
        c_interval.add_numbers([-1, 0, 1], num_decimal_places=1, font_size=16) # add numbers to ticks
        c_tip = ArrowTip(angle=-90 * DEGREES)
        c_tip.scale(0.5)
        c_tip.set_fill(RED)
        # let tip move with c all the time.
        c_tip.add_updater(lambda m: m.move_to(c_interval.n2p(get_c()), DOWN)) # type: ignore

        c_label = Tex("c = 1.00", t2c={"c": RED}, font_size=36)
        c_label.make_number_changeable("1.00") # a critical method for Tex type
        c_label[-1].scale(0.8, about_edge=LEFT) # aligned to the origin left side and scale up
        c_label.add_updater(lambda m: m[-1].set_value(get_c())) # type: ignore
        c_label.add_updater(lambda m: m.next_to(c_tip, UP, aligned_edge=LEFT))

        return [c_tracker, c_interval, c_tip, c_label]
    
    def get_axes(self): # write a Axes generate func for further using in later sub_class
        axes = Axes(
            (-1, 5), (0, 4),
            width=6, height=4,
        )
        return axes

    def func(self, x, c): # named for 'bind_graph_to_func'?
        return np.exp(c * x) # use a ndarray type, which is better for manim rendering, but an math.e is also acceptable

    def get_label(self, axes):
        label = Tex("e^{cx}", t2c={"c": RED})
        label.next_to(axes.c2p(0, 2.7), RIGHT)
        return label


# So you see: To update a scene, 
# you could inheriate the method from the former class
# and rewrite them if necessary
class VariableCWithF(VariableC):
    def get_axes(self):
        axes = Axes(
            (-4, 4), (0, 2),
            width=8, height=3,
        )
        axes.add(VectorizedPoint(axes.c2p(0, 3)))
        axes.center()
        return axes

    def func(self, x, c):
        return np.exp(c * x * x)

    def get_label(self, axes):
        label = Tex("e^{cx^2}", t2c={"c": RED})
        label.next_to(axes.c2p(0, 2), LEFT)
        return label

# Let's start:
class TalkAboutSignOfConstant3D(VariableCWithF):
    def construct(self):
        # Setup
        # you could think the "frame" as the structure of a camera
        frame = self.frame # give the "self.frame" a shorter name
        # let frame spining along the time:
        # add_updater need a func:
        # mob.add_update(func(mob, dt) -> new_mob) sometimes you needn't a return value
        # use cos() to move the frame back and forth
        # self time will be counted from the scene started (I think so...)
        frame.add_updater(lambda m: m.reorient(20 * math.cos(0.1 * self.time), 75)) # type: ignore

        # you may like adding some param. by using set method for coordinate system
        axes = ThreeDAxes((-4, 4), (-4, 4), (0, 1), depth=2)
        axes.set_width(10)
        axes.set_depth(2, stretch=True)
        axes.center()
        self.add(axes)

        label = Tex("f(r) = e^{cr^2}", t2c={"c": RED}, font_size=72) # t2c, t2s, t2w: {"target string": params}
        label.next_to(ORIGIN, LEFT) # use origin to locate 
        label.to_edge(UP)
        label.fix_in_frame() # disabled the label from moving along the camera

        c_tracker, c_interval, c_tip, c_label = self.get_c_group()
        get_c = c_tracker.get_value
        c_interval.next_to(label, RIGHT, LARGE_BUFF) # so next time you may use 'LARGE_BUFF', not buff=...
        c_interval.shift(0.5 * DOWN) # type: ignore
        c_tracker.set_value(-1) # initial value

        c_group = VGroup(c_interval, c_tip, c_label)
        c_group.fix_in_frame()

        # Graph for ThreeD
        def get_graph(c):
            surface = axes.get_graph(lambda x, y: np.exp(c * (x**2 + y**2))) 
            surface.always_sort_to_camera(self.camera)
            surface.set_color(BLUE_E, 0.5)
            mesh = SurfaceMesh(surface, (31, 31)) # useful func for ThreeDSurface !
            mesh.set_stroke(WHITE, 0.5, 0.5)
            mesh.shift(0.001 * OUT) # type: ignore
            x_slice = ParametricCurve(
                lambda t: axes.c2p(t, 0, np.exp(c * t**2)),
                t_range=(-4, 4, 0.1)
            )
            x_slice.set_stroke(RED, 2)
            x_slice.set_flat_stroke(False)
            return Group(mesh, surface, x_slice)

        graph = get_graph(-1)

        self.add(graph)
        self.add(c_group)
        self.add(label)

        # Animations
        for value in [-0.5, -0.8, -0.3, -1.0, -0.3, 0.05, 0.1, -0.3, -1.0, -0.7, -1.0]:
            new_graph = get_graph(value)
            self.play(
                c_tracker.animate.set_value(value),
                Transform(graph, new_graph),
                run_time=5
            )
            self.wait()


"""
2025/3/2 Topic 2:
File: In _2023/gauss_int/herschel.py, learning from line 500 to 1088
Topic: Tex and some useful text animation func.
"""

class TwoProperties(InteractiveScene):
    def construct(self):
        # Name properties
        properties = VGroup(
            VGroup(
                Text("Property 1"),
                # Unknown usage of TexTest
                TexText(
                R"""
                The probability (density) depends \\
                only on the distance from the origin
                """, alignment="", font_size=36, color=GREY_A),
            ),
            VGroup(
                Text("Property 2"),
                TexText(R"""
                    The $x$ and $y$ coordinates are \\
                    independent from each other.
                """, alignment="", font_size=36, color=GREY_A),
            ),
        )
        for prop in properties:
            prop.arrange(DOWN, aligned_edge=LEFT)
        properties.arrange(DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT)
        properties.to_corner(UL)

        # Notice this func: SurroundingRectangle()
        prop_boxes = VGroup(*(
            SurroundingRectangle(prop[1]).set_fill(GREY_E, 1).set_stroke(RED, 1, 0.5)
            for prop in properties
        ))

        for prop, box in zip(properties, prop_boxes):
            # lag_ratio defines the delay of the animation for
            # a bunch of mob, or animationgroup
            # 1: 100% delay
            # 0: smountanously occurred
            self.play(FadeIn(prop[0], lag_ratio=0.1), FadeIn(box))

        # Formula
        implies = Tex(R"\Downarrow", font_size=72)
        implies.next_to(properties, DOWN, MED_LARGE_BUFF)

        # a way to set t2c to many Tex (Tex only support t2c)
        kw = dict(
            t2c={"x": BLUE, "y": YELLOW, R"\sigma": RED, "{r}": RED}
        )
        form1, form2, form3 = forms = VGroup(
            Tex(R"f_2(x, y) = e^{-(x^2 + y^2)}", **kw),  # type: ignore
            Tex(R"f_2(x, y) = e^{-(x^2 + y^2) / 2 \sigma^2}", **kw),  # type: ignore
            Tex(R"f_2(x, y) = {1 \over 4 \sigma^2 \pi} e^{-(x^2 + y^2) / 2 \sigma^2}", **kw),  # type: ignore
        )
        forms.next_to(implies, DOWN, MED_SMALL_BUFF)

        form1.save_state() # Save the now state for later "restore()"
        self.play(
            Write(implies),
            FadeIn(form1, DOWN)
        )
        self.wait()
        self.play(TransformMatchingTex(form1, form2, run_time=1, lag_ratio=0.05))  # type: ignore
        self.wait(2)
        self.play(TransformMatchingTex(form2, form3, run_time=1, lag_ratio=0.05))  # type: ignore
        self.wait(2)
        form1.restore()
        self.play(TransformMatchingTex(form3, form1, run_time=2, lag_ratio=0.05))  # type: ignore
        self.wait(2)

        # Property 1
        lhs = form1["f_2(x, y)"][0]

        self.add(properties[0][1], prop_boxes[0])
        self.play(
            prop_boxes[0].animate.stretch(0, 0, about_edge=RIGHT).set_opacity(0),
            FadeOut(implies),
            FadeOut(form1["= e^{-(x^2 + y^2)}"]),
        )
        self.remove(prop_boxes[0])
        self.add(lhs)
        self.wait()
        phrase = properties[0][1]["only on the distance"]
        self.play(
            FlashUnder(phrase, color=TEAL, buff=0),
            phrase.animate.set_color(TEAL),
        )
        self.wait(2)

        # Function of radius
        lhs.generate_target()
        lhs.target.to_edge(LEFT) # type: ignore
        radial_rhs = Tex(R"= f({r})", **kw)  # type: ignore
        full_radial_rhs = Tex(R"= f(\sqrt{x^2 + y^2})", **kw)  # type: ignore
        radial_rhs.next_to(lhs.target, RIGHT, SMALL_BUFF)  # type: ignore
        full_radial_rhs.next_to(radial_rhs, RIGHT, MED_SMALL_BUFF)
        # a little bit complex position locate expression
        full_radial_rhs.shift((radial_rhs["="].get_y() - full_radial_rhs["="].get_y()) * UP)  # type: ignore

        lhs_rect = SurroundingRectangle(lhs) # create YELLOW boundary for emphsis
        f_rect = SurroundingRectangle(radial_rhs["f"], buff=0.05) # particularly for "f"
        f_rect.set_stroke(BLUE, 2)
        f_words = Text("Some single-variable function", font_size=36)
        f_words.next_to(f_rect, UP, SMALL_BUFF, aligned_edge=LEFT)
        f_words.match_color(f_rect)

        self.play(ShowCreation(lhs_rect))
        self.wait()

        self.play(lhs_rect.animate.replace(lhs[1], stretch=True).set_stroke(width=1).scale(1.1))
        self.play(FadeOut(lhs_rect))
        self.wait()
        self.play(
            MoveToTarget(lhs),
            Write(radial_rhs),
        )
        self.play(
            ShowCreation(f_rect),
            FadeIn(f_words, lag_ratio=0.1)
        )
        self.wait(2)
        self.play(FadeOut(f_words), FadeOut(f_rect))
        self.play(TransformMatchingTex(radial_rhs.copy(), full_radial_rhs))
        self.wait(2)

        # Property 2
        self.add(properties[1][1], prop_boxes[1])
        self.play(
            prop_boxes[1].animate.stretch(0, 0, about_edge=RIGHT).set_opacity(0),
        )
        self.remove(prop_boxes[0])
        self.wait()

        phrase = properties[1][1]["independent"]
        self.play(
            FlashUnder(phrase, color=TEAL, buff=0),
            phrase.animate.set_color(TEAL)
        )
        self.wait()

        # Factored expression
        lhs.generate_target()
        lhs.target.next_to(properties, DOWN, buff=0.7, aligned_edge=LEFT) # type: ignore
        radial_rhss = VGroup(radial_rhs, full_radial_rhs)

        factored_rhs = Tex(R"= g(x) h(y)", **kw) # type: ignore
        simpler_rhs = Tex(R"= g(x) g(y)", **kw) # type: ignore
        for rhs in factored_rhs, simpler_rhs:
            rhs.next_to(lhs.target, RIGHT) # type: ignore

        g_box = SurroundingRectangle(factored_rhs["g(x)"], buff=0.05).set_stroke(BLUE, 2)
        h_box = SurroundingRectangle(factored_rhs["h(y)"], buff=0.05).set_stroke(YELLOW, 2)
        g_words = TexText("Distribution of $x$", font_size=30).next_to(g_box, DOWN, 0.2)
        h_words = TexText("Distribution of $y$", font_size=30).next_to(h_box, DOWN, 0.2)

        self.play(
            MoveToTarget(lhs),
            radial_rhss.animate.to_edge(LEFT).shift(0.5 * DOWN).set_opacity(0.35), # type: ignore
        )
        self.play(
            TransformMatchingShapes(lhs.copy(), factored_rhs)
        )
        self.wait()
        self.play(
            # use ShowCreation() to animate box
            ShowCreation(g_box),
            FadeIn(g_words)
        )
        self.wait()
        self.play(
            # use ReplacementTransform() to show text and box transform
            ReplacementTransform(g_box, h_box),
            ReplacementTransform(g_words, h_words),
        )
        self.wait()
        self.play(FadeOut(h_box), FadeOut(h_words))
        self.wait()
        self.play(
            # use UP param to show words change
            FadeOut(factored_rhs["h(y)"], 0.5 * UP), # type: ignore
            FadeIn(simpler_rhs["g(y)"], 0.5 * UP), # type: ignore
        )
        self.wait()
        self.remove(factored_rhs)
        self.add(simpler_rhs)

        # Show proportionality
        arrow = Arrow(simpler_rhs, radial_rhs)
        self.play(
            # use this func to show arrow from none to exist
            GrowArrow(arrow),
            radial_rhs.animate.set_opacity(1),
            FadeOut(full_radial_rhs),
        )
        self.wait()
        radial_rhs.generate_target()
        radial_rhs.target.next_to(lhs, RIGHT) # type: ignore
        self.play(
            MoveToTarget(radial_rhs),
            simpler_rhs.animate.next_to(radial_rhs.target, RIGHT),
            Uncreate(arrow), # AntiShowCreation()
        )
        self.wait()

        xs = VGroup(lhs[3], simpler_rhs["x"][0][0]) # type: ignore
        ys = VGroup(lhs[5], simpler_rhs["y"][0][0]) # type: ignore
        rs = Tex("{r}", **kw).replicate(2) # type: ignore
        zeros = Tex("0", **kw).replicate(2) # type: ignore
        zeros.set_color(YELLOW)
        for x, r in zip(xs, rs):
            r.move_to(x, DOWN)
        for x, y, zero in zip(xs, ys, zeros):
            zero.move_to(y)
            zero.align_to(x, DOWN)

        const_rect = SurroundingRectangle(simpler_rhs["g(y)"], buff=0.05)
        const_rect.set_stroke(YELLOW, 1)
        const_words = Text("Some constant", font_size=36)
        const_words.match_color(const_rect)
        const_words.next_to(const_rect, DOWN)

        self.play(
            LaggedStartMap(FadeOut, VGroup(*xs, *ys), shift=0.5 * UP), # type: ignore
            LaggedStartMap(FadeIn, VGroup(*rs, *zeros), shift=0.5 * UP), # type: ignore
        )
        self.wait()
        self.play(
            ShowCreation(const_rect),
            FadeIn(const_words)
        )
        self.wait()

        # Assume this constant is 1
        assumption = TexText("Assume this is 1", font_size=36)
        assumption.move_to(const_words)
        assumption.match_color(const_words)

        f_eq_g = Tex("f = g", **kw) # type: ignore
        f_eq_g.next_to(radial_rhs, DOWN, LARGE_BUFF)

        f_rhs = Tex(R"= f(x)f(y)", **kw) # type: ignore
        f_rhs.move_to(simpler_rhs, LEFT)
        gs = simpler_rhs["g"]
        fs = f_rhs["f"]

        self.play(
            FadeIn(assumption, 0.5 * DOWN), # type: ignore
            FadeOut(const_words, 0.5 * DOWN), # type: ignore
        )
        self.wait()

        self.play(
            TransformFromCopy(
                VGroup(radial_rhs[1], *simpler_rhs[:2]),
                f_eq_g
            )
        )
        self.wait()

        self.play(
            LaggedStartMap(FadeIn, VGroup(*xs, *ys), shift=0.5 * DOWN), # type: ignore
            LaggedStartMap(FadeOut, VGroup(*rs, *zeros), shift=0.5 * DOWN), # type: ignore
            FadeOut(const_rect),
            FadeOut(assumption),
        )
        self.wait()
        self.play(
            TransformMatchingShapes(f_eq_g[0].copy(), fs),
            ReplacementTransform(simpler_rhs, f_rhs),
        )
        self.wait()

        # Highlight key equation
        key_equation = VGroup(*radial_rhs[1:], *f_rhs)

        self.play(
            key_equation.animate.set_x(0.25 * FRAME_WIDTH).to_edge(UP),
            FadeOut(f_eq_g),
            FadeOut(lhs),
            FadeOut(radial_rhs[0]),
        )
        # another critical class to emphsize
        """
        Create a surroundingrectangle flashing once
        """
        # similiarly you could use FlashUnder()
        self.play(FlashAround(key_equation, time_width=1, run_time=2))

        full_radial_rhs.set_opacity(1)
        full_radial_rhs.move_to(key_equation).shift(LEFT)

        self.play(
            GrowFromCenter(full_radial_rhs, lag_ratio=0.02),
            radial_rhs[1:].animate.next_to(full_radial_rhs, LEFT, aligned_edge=DOWN),
            key_equation[4:].animate.next_to(full_radial_rhs, RIGHT),
        )
        self.wait()

        # Name as a functional equation
        func_eq_name = Text("Functional\nequation")
        func_eq_name.to_corner(UL)
        func_eq_name.match_y(key_equation)
        # Arrow() could use mob or vec3 but get_left() is better for location
        arrow = Arrow(func_eq_name, radial_rhs[1].get_left(), buff=0.25)
        func_eq_name.to_edge(UP)

        self.play(LaggedStartMap(FadeOut, properties, shift=LEFT, lag_ratio=0.2))
        self.play(
            Write(func_eq_name),
            GrowArrow(arrow)
        )
        self.wait()

        # Example
        example_box = Rectangle(4, 3)
        # next time use TEAL for expression is pretty nice.
        example_box.set_stroke(TEAL, 2)
        example_box.set_fill(TEAL, 0.35)
        example_box.to_corner(DL, buff=0)
        example_word = Text("For example", font_size=30)
        example_word.next_to(example_box.get_top(), DOWN, SMALL_BUFF)
        example_f = Tex(R"f({r}) = e^{-{r}^2}", **kw) # type: ignore
        example_f.scale(0.75)
        example_f.next_to(example_word, DOWN, MED_LARGE_BUFF)

        self.play(
            FadeIn(example_box),
            FadeIn(example_word, 0.5 * DOWN) # type: ignore
        )
        self.play(
            TransformFromCopy(key_equation[:4], example_f[:4]),
            GrowFromPoint(example_f[4:], key_equation.get_left()),
        )
        self.wait()

        # Define h
        let = Text("Let")
        h_def = Tex(R"h({x}) = f(\sqrt{{x}})", **kw) # type: ignore
        h_def.next_to(key_equation, DOWN, LARGE_BUFF)
        let.next_to(h_def, LEFT, MED_LARGE_BUFF)
        h_def2 = Tex(R"h({x}^2) = f({x})", **kw) # type: ignore
        h_def2.next_to(h_def["h"], DOWN, MED_LARGE_BUFF, aligned_edge=LEFT)

        h_eq = Tex(R"h(x^2 + y^2) = h(x^2) h(y^2)", **kw) # type: ignore
        h_eq.to_corner(UR)
        h_eq.to_edge(RIGHT, buff=1.25)

        example_h = Tex(R"h({r}) = e^{-{r}}", **kw) # type: ignore
        example_h.scale(0.75)
        example_h.next_to(example_f, DOWN, MED_LARGE_BUFF)

        self.play(FadeIn(h_def, DOWN), Write(let))
        self.wait()
        self.play(TransformMatchingTex(
            h_def.copy(), h_def2,
            key_map={R"\sqrt": "^2"},
            run_time=1
        ))
        self.wait()
        self.play(
            TransformFromCopy(h_def, example_h)
        )
        self.wait(2)

        self.play(
            VGroup(key_equation, full_radial_rhs).animate.scale(0.8).to_edge(LEFT),
            VGroup(let, h_def, h_def2).animate.scale(0.8).to_edge(LEFT),
            FadeOut(func_eq_name, LEFT),
            Uncreate(arrow),
        )
        self.play(
            TransformMatchingShapes(
                VGroup(*full_radial_rhs[1:], *f_rhs).copy(),
                h_eq
            )
        )
        self.wait()

        # Exponential property
        sum_box = SurroundingRectangle(h_eq["x^2 + y^2"])
        prod_box = SurroundingRectangle(h_eq["h(x^2) h(y^2)"])
        sum_words = Text("Adding inputs", font_size=30)
        sum_words.next_to(sum_box, DOWN)
        prod_words = Text("Multiplying outputs", font_size=30)
        prod_words.next_to(prod_box, DOWN)

        VGroup(sum_box, prod_box).set_stroke(TEAL, 2)
        VGroup(sum_words, prod_words).set_color(TEAL)

        self.play(
            ShowCreation(sum_box),
            FadeIn(sum_words, lag_ratio=0.1),
        )
        self.wait()
        self.play(
            ReplacementTransform(sum_box, prod_box),
            FadeTransform(sum_words, prod_words),
        )
        self.wait()
        self.play(FadeOut(prod_box), FadeOut(prod_words))
        self.wait()

        # Multi-input property
        implies = Tex(R"\Downarrow", font_size=72)
        implies.next_to(h_eq, DOWN)
        full_h_eq = Tex(R"h(x_1 + x_2 + \cdots + x_n) = h(x_1)h(x_2) \cdots h(x_n)")
        for s, color in zip(["1", "2", "n"], color_gradient([BLUE, YELLOW], 3)):
            full_h_eq[f"x_{s}"].set_color(color)
        full_h_eq.scale(0.75)
        full_h_eq.next_to(implies, DOWN)

        self.play(
            Write(implies),
            FadeIn(full_h_eq, DOWN),
        )
        self.wait()

        # Whole numbers
        implies2 = implies.copy()
        implies2.next_to(full_h_eq, DOWN, buff=MED_LARGE_BUFF)

        five_eq = Tex(R"h(5) &= h(1 + 1 + 1 + 1 + 1) \\ &= h(1)h(1)h(1)h(1)h(1) = h(1)^5")
        five_eq.next_to(implies2, DOWN)
        five_eq.to_edge(RIGHT)

        n_eq = Tex(R"h(n) = h(1 + \cdots + 1) = h(1) \cdots h(1) = h(1)^n")
        n_eq.scale(0.75)
        n_eq.next_to(implies2, DOWN, MED_LARGE_BUFF)
        # useful latex warpper func for sum
        """
        Create huge () for sum
        """
        sum_brace = Brace(n_eq[R"1 + \cdots + 1"], UP, SMALL_BUFF)
        sum_tex = sum_brace.get_tex(R"n \text{ times}", buff=SMALL_BUFF).scale(0.5, about_edge=DOWN)
        prod_brace = Brace(n_eq[R"h(1) \cdots h(1)"], UP, SMALL_BUFF)
        prod_tex = prod_brace.get_tex(R"n \text{ times}", buff=SMALL_BUFF).scale(0.5, about_edge=DOWN)

        for tex in n_eq, sum_tex, prod_tex:
            tex["n"].set_color(BLUE)

        self.play(Write(five_eq["h(5)"]))
        self.wait()
        self.play(
            TransformFromCopy(five_eq["h("][0], five_eq["h("][1]),
            TransformFromCopy(five_eq[")"][0], five_eq[")"][1]),
            Write(five_eq["="][0]), # type: ignore
        )
        self.play(ShowIncreasingSubsets(five_eq["1 + 1 + 1 + 1 + 1"][0]))
        self.wait()
        self.play(
            FadeTransform(
                five_eq["= h(1 + 1 + 1 + 1 + 1)"].copy(),
                five_eq["= h(1)h(1)h(1)h(1)h(1)"],
            )
        )
        self.wait()
        self.play(Write(five_eq["= h(1)^5"]))
        self.wait()

        self.play(FadeOut(five_eq), FadeIn(n_eq), FadeIn(implies2))
        self.play(LaggedStart(
            GrowFromCenter(sum_brace),
            FadeIn(sum_tex, 0.25 * DOWN), # type: ignore
            GrowFromCenter(prod_brace),
            FadeIn(prod_tex, 0.25 * DOWN), # type: ignore
        ))
        self.wait()

        # Exponential equation
        exp_eq1 = Tex(R"h(n) = h(1)^n")
        exp_eq2 = Tex(R"h(n) = b^n")
        for eq in exp_eq1, exp_eq2:
            eq["n"].set_color(BLUE)
        exp_eq1.next_to(n_eq, DOWN, MED_LARGE_BUFF)
        exp_eq2.move_to(exp_eq1, LEFT)
        h1_rect = SurroundingRectangle(exp_eq1["h(1)"], buff=0.05)
        h1_rect.set_stroke(YELLOW, 1)
        h1_words = Text("Some number", font_size=30)
        h1_words.match_color(h1_rect)
        h1_words.next_to(h1_rect, DOWN, SMALL_BUFF)

        self.play(
            TransformFromCopy(n_eq["h(n)"], exp_eq1["h(n)"]),
            TransformFromCopy(n_eq["= h(1)^n"], exp_eq1["= h(1)^n"]),
        )
        self.wait()
        self.play(ShowCreation(h1_rect), FadeIn(h1_words))
        self.wait()
        self.play(
            TransformMatchingTex(exp_eq1, exp_eq2),
            FadeOut(h1_rect, scale=0.5),
            FadeOut(h1_words, scale=0.5),
        )
        self.wait()

        # Show exercises
        self.play(
            exp_eq2.animate.next_to(implies2, DOWN),
            FadeOut(VGroup(n_eq, sum_brace, sum_tex, prod_brace, prod_tex), UP),
        )
        rational_eq = Tex(R"h(p / q) = b^{\,p / q}")
        rational_eq["p / q"].set_color(RED)
        rational_eq.move_to(exp_eq2)

        exercise = TexText(R"Exercise: Show this is also true for rational inputs, $p / q$")
        exercise["p / q"].set_color(RED)
        hint = TexText(R"Hint, think about $h\left(\frac{p}{q} + \cdots + \frac{p}{q} \right)$")

        exercise.next_to(rational_eq, DOWN, LARGE_BUFF)
        exercise.to_edge(RIGHT)
        hint.scale(0.7)
        hint.set_fill(GREY_A)
        hint.next_to(exercise, DOWN)

        self.play(
            Write(exercise),
            FadeOut(VGroup(example_box, example_word, example_f, example_h), shift=DL),
        )
        self.wait()
        pq_target = rational_eq["p / q"].copy()
        self.play(
            TransformMatchingTex(exp_eq2, rational_eq),
            TransformMatchingShapes(exercise["p / q"].copy(), pq_target),
        )
        self.remove(pq_target)
        self.wait()
        self.play(FadeIn(hint, DOWN))
        self.wait(2)
        self.play(LaggedStart(
            FadeOut(exercise, 0.5 * DOWN), # type: ignore
            FadeOut(hint, 0.5 * DOWN), # type: ignore
            lag_ratio=0.25,
        ))

        # Continuity
        assumption = TexText(R"Assuming $f$ (and hence also $h$) \\ is continuous...", font_size=36)
        assumption.next_to(rational_eq, LEFT, buff=2.0, aligned_edge=UP)
        assumption.shift(0.5 * DOWN) # type: ignore

        hx_eq = Tex("h(x) = b^x", **kw) # type: ignore
        hx_eq.move_to(rational_eq)
        range1 = TexText(R"For all $x \in \mathds{R}$", **kw) # type: ignore
        range2 = TexText(R"For all $x \in \mathds{R}^+$", **kw) # type: ignore
        for ran in range1, range2:
            ran.scale(0.75)
            ran.next_to(hx_eq, DOWN, MED_LARGE_BUFF)

        arrow = Arrow(assumption, hx_eq)

        self.play(FadeIn(assumption, lag_ratio=0.1))
        self.wait()
        self.play(
            GrowArrow(arrow),
            TransformMatchingTex(rational_eq, hx_eq)
        )
        self.play(FadeIn(range1, DOWN))
        self.wait()
        self.play(FadeTransform(range1, range2))
        self.wait()

        # Swap out for e
        hx_eq2 = Tex(R"h(x) = e^{{c} x}", **kw) # type: ignore
        hx_eq2.move_to(hx_eq)
        hx_eq2["c"].set_color(RED)

        b_rect = SurroundingRectangle(hx_eq["b"], buff=0.05)
        b_rect.set_stroke(PINK, 2)
        b_words = Text("Some constant", font_size=30)
        b_words.next_to(b_rect, DOWN, SMALL_BUFF, LEFT)
        b_words.match_color(b_rect)

        self.play(
            FadeOut(assumption, LEFT),
            Uncreate(arrow),
            FadeOut(range2, LEFT),
            ShowCreation(b_rect),
            Write(b_words, run_time=1)
        )
        self.wait()
        c = hx_eq2["{c}"][0][0]
        c_copy = c.copy()
        c.set_opacity(0)
        self.play(
            ReplacementTransform(b_rect, c_copy),
            TransformMatchingTex(hx_eq, hx_eq2, key_map={"b": "e"}),
            FadeOut(b_words, 0.2 * DOWN), # type: ignore
        )
        self.remove(c_copy)
        c.set_opacity(1)
        self.add(hx_eq2)
        self.wait()

        # Write final form for f
        implies3 = implies2.copy()
        implies3.rotate(-90 * DEGREES)
        implies3.next_to(hx_eq2, LEFT)
        f_form = Tex(R"f(x) = e^{cx^2}", **kw) # type: ignore
        f_form["c"].set_color(RED)
        f_form.next_to(implies3, LEFT)
        f_form.align_to(hx_eq2, DOWN)

        self.play(
            Write(implies3),
            TransformMatchingTex(hx_eq2.copy(), f_form, run_time=1)
        )
        self.wait()
        f_form.generate_target()
        f_form.target.scale(1.5, about_edge=RIGHT) # type: ignore
        rect = SurroundingRectangle(f_form.target) # type: ignore
        rect.set_stroke(YELLOW, 2)
        self.play(
            MoveToTarget(f_form),
            FlashAround(f_form.target, time_width=1, run_time=2, stroke_width=5), # type: ignore
            ShowCreation(rect, run_time=2),
        )
        self.wait()

