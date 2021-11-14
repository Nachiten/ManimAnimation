from manim import *

labelColor = BLUE
dotColor = YELLOW
lineColor = ORANGE

class NumerosComplejosBinomica(Scene):
    def construct(self):
        def dot_position(mobject, dot):
            mobject.set_value(dot.get_center()).set_color(labelColor)
            mobject.next_to(dot, UP)

        # Lineas del plano
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
                  Write(label), run_time=1)

        h_line = always_redraw(lambda: plane.get_horizontal_line(d1.get_left()).set_color(lineColor))
        v_line = always_redraw(lambda: plane.get_vertical_line(d1.get_bottom()).set_color(lineColor))
        self.play(Create(h_line),
                  Create(v_line))

        self.wait(1)

        d2 = Dot(plane.n2p(-1 + -2j), color=YELLOW)
        self.play(Transform(d1, d2), run_time=2)

        self.wait(1)

        d2 = Dot(plane.n2p(-1 + 2j), color=YELLOW)
        self.play(Transform(d1, d2), run_time=2)

        self.wait(1)

        d2 = Dot(plane.n2p(3 + -1j), color=YELLOW)
        self.play(Transform(d1, d2), run_time=2)

        self.wait(3)
