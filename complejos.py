from manim import *


class CoordinateSystem(Scene):
    def construct(self):
        # Lineas del plano
        plane = ComplexPlane(x_range=[-6, 6, 1], y_range=[-6, 6, 1],
                             x_length=7, y_length=7,
                             background_line_style={"stroke_color": TEAL,
                                                    "stroke_width": 2,
                                                    "stroke_opacity": 0.2}).add_coordinates()

        self.play(Create(plane, run_time=2))

        self.wait(1)

        d1 = Dot(plane.n2p(2 + 1j), color=YELLOW)
        d2 = Dot(plane.n2p(-3 - 2j), color=YELLOW)
        label2 = MathTex("-3-2i").next_to(d2, UR, 0.1)

        self.play(Create(d1, run_time=2),
                  Create(d2, run_time=2),
                  Create(label2, run_time=2))

        h_line = always_redraw(lambda: plane.get_horizontal_line(d1.get_left()))
        v_line = always_redraw(lambda: plane.get_vertical_line(d1.get_bottom()))

        self.play(Create(h_line, run_time=2),
                  Create(v_line, run_time=2))

        def dot_position(mobject):
            mobject.set_value(d1.get_x())
            mobject.next_to(d1)

        label1 = MathTex()
        label1.add_updater(dot_position)

        self.play(Create(label1))

        self.wait(2)

        self.wait(3)
