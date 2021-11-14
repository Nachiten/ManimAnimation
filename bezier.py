from manim import *


class BezierCurves(Scene):
    plane = NumberPlane(x_range=[-6, 6, 1], y_range=[-6, 6, 1],
                        x_length=7, y_length=7,
                        background_line_style={"stroke_color": TEAL,
                                               "stroke_width": 2,
                                               "stroke_opacity": 0.2}).add_coordinates().center()

    p1 = plane.c2p(-3, 1)
    p2 = plane.c2p(3.0, -1.0)

    dotp1 = Dot(point=p1).set_color(BLUE)
    dotp2 = Dot(point=p2).set_color(RED)

    p1Control = plane.c2p(-2.0, 2.0)
    p2Control = plane.c2p(2.0, -2.0)

    dotp1Control = Dot(point=p1Control).set_color(LIGHT_GRAY)
    dotp2Control = Dot(point=p2Control).set_color(LIGHT_GRAY)

    line1 = Line(dotp1.get_center(), p1Control).set_color(ORANGE)
    line2 = Line(dotp2.get_center(), p2Control).set_color(ORANGE)

    bezierCurve = CubicBezier(start_anchor=dotp1.get_center(), start_handle=p1Control,
                              end_anchor=dotp2.get_center(), end_handle=p2Control)

    def construct(self):
        self.play(Create(self.plane))

        # Muestro los dos puntos
        self.play(Create(self.dotp1),
                  Create(self.dotp2))

        self.wait()

        # Muestro los dos controles y los conecto
        self.play(Create(self.dotp1Control),
                  Create(self.dotp2Control))
        self.play(Create(self.line1),
                  Create(self.line2))

        self.wait()

        # Muestro la bezier final
        self.play(Create(self.bezierCurve))

        self.wait()

        self.moverPuntosDeControlA(self.plane.c2p(-1, 3), self.plane.c2p(1, 3))

        self.wait()

        self.moverPuntosDeControlA(self.plane.c2p(-3, 0), self.plane.c2p(-1, 1))

        self.wait()

        self.moverPuntosDeControlA(self.plane.c2p(-2, -6), self.plane.c2p(-4, -6))

        self.wait(3)

    def moverPuntosDeControlA(self, control1, control2):
        p1Control = control1
        dotp1Controlb = Dot(point=p1Control).set_color(LIGHT_GRAY)
        line1b = Line(self.p1, p1Control).set_color(ORANGE)

        p2Control = control2
        dotp2Controlb = Dot(point=p2Control).set_color(LIGHT_GRAY)
        line2b = Line(self.p2, p2Control).set_color(ORANGE)

        bezierCurveb = CubicBezier(start_anchor=self.p1, start_handle=p1Control,
                                   end_anchor=self.p2, end_handle=p2Control)

        self.play(Transform(self.bezierCurve, bezierCurveb),
                  Transform(self.line1, line1b),
                  Transform(self.line2, line2b),
                  Transform(self.dotp1Control, dotp1Controlb),
                  Transform(self.dotp2Control, dotp2Controlb))
