from manim import *

labelColor = BLUE
dotColor = YELLOW
lineColor = WHITE


class NumerosComplejosBinomica(Scene):
    def construct(self):
        #def dot_position(mobject, dot):
        #    mobject.set_value(plane.p2n(d1.get_center())).set_color(labelColor)
        #    mobject.next_to(dot, UP)

        """

        plane = ComplexPlane(x_range=[-6, 6, 1], y_range=[-6, 6, 1],
                             x_length=7, y_length=7,
                             background_line_style={"stroke_color": TEAL,
                                                    "stroke_width": 2,
                                                    "stroke_opacity": 0.2}).add_coordinates()
        self.play(Create(plane, run_time=2))

        self.wait(1)

        d1 = Dot(plane.n2p(2 + 1j), color=dotColor)
        label = DecimalNumber(plane.p2n(d1.get_center()), num_decimal_places=2).set_color(labelColor)
        label.add_updater(lambda mobject: dot_position(mobject, d1))
        self.play(Create(d1),
                  Write(label))

        h_line = always_redraw(lambda: plane.get_horizontal_line(d1.get_left()).set_color(lineColor))
        v_line = always_redraw(lambda: plane.get_vertical_line(d1.get_bottom()).set_color(lineColor))
        self.play(Create(h_line),
                  Create(v_line))

        self.wait(1)

        d2 = Dot(plane.n2p(-4 + -3j), color=YELLOW)
        self.play(Transform(d1, d2), run_time=2)

        self.wait(1)

        d2 = Dot(plane.n2p(-3 + 5j), color=YELLOW)
        self.play(Transform(d1, d2), run_time=2)

        self.wait(1)

        d2 = Dot(plane.n2p(2.5 + -0.33j), color=YELLOW)
        self.play(Transform(d1, d2), run_time=2)

        self.wait(3)

        self.play(Uncreate(h_line),
                  Uncreate(v_line))

        self.play(Uncreate(d1),
                  Uncreate(label))

        self.play(Uncreate(plane))

        """

        self.wait(1)

        plane = PolarPlane(size=6, background_line_style={
                                                  "stroke_color": TEAL,
                                                  "stroke_width": 2,
                                                  "stroke_opacity": 0.2}).add_coordinates()

        self.play(Create(plane, run_time=2))

        self.wait(1)

        #d1 = Dot((2, np.pi), color=dotColor)
        #label = DecimalNumber(plane.p2n(d1.get_center()), num_decimal_places=2).set_color(labelColor)
        #label.add_updater(lambda mobject: dot_position(mobject, d1))
        #self.play(Create(d1))
        #          Write(label))

        #h_line = always_redraw(lambda: plane.get_horizontal_line(d1.get_left()).set_color(lineColor))
        #v_line = always_redraw(lambda: plane.get_vertical_line(d1.get_bottom()).set_color(lineColor))
        #self.play(Create(h_line),
        #          Create(v_line))

        #self.wait(1)
