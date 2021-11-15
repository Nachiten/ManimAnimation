from manim import *

xMin, xMax = -5, 15
yMin, yMax = -5, 15
xLength, yLength = 8, 8

values = [0, 2, 4, 6, 8, 10, 12, 14]

# lines = NumberPlane(x_range=[xMin, xMax, 1], y_range=[yMin, yMax, 1],
#                    x_length=xLength, y_length=yLength,
#                    background_line_style={"stroke_color": TEAL,
#                                           "stroke_width": 2,
#                                           "stroke_opacity": 0.2}).center()

plane = Axes(x_range=[xMin, xMax, 1], y_range=[yMin, yMax, 1],
             x_length=xLength, y_length=yLength).add_coordinates(values, values).center()

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


class BezierCurves(Scene):
    def construct(self):
        self.play(Create(plane))

        # Muestro los dos puntos
        self.play(Create(dotp1),
                  Create(dotp2))

        self.wait()

        # Muestro los dos controles y los conecto
        self.play(Create(dotp1Control),
                  Create(dotp2Control))
        self.play(Create(line1),
                  Create(line2))

        self.wait()

        # Muestro la bezier final
        self.play(Create(bezierCurve))

        self.wait()

        self.moverPuntosDeControlA(plane.c2p(-1, 3), plane.c2p(1, 3))

        self.wait()

        self.moverPuntosDeControlA(plane.c2p(-3, 0), plane.c2p(-1, 1))

        self.wait()

        self.moverPuntosDeControlA(plane.c2p(-2, -2), plane.c2p(-1, -3))

        self.wait(3)

    def moverPuntosDeControlA(self, control1, control2):
        global p1Control
        global p2Control

        p1Control = control1
        dotp1Controlb = Dot(point=p1Control).set_color(LIGHT_GRAY)
        line1b = Line(p1, p1Control).set_color(ORANGE)

        p2Control = control2
        dotp2Controlb = Dot(point=p2Control).set_color(LIGHT_GRAY)
        line2b = Line(p2, p2Control).set_color(ORANGE)

        bezierCurveb = CubicBezier(start_anchor=p1, start_handle=p1Control,
                                   end_anchor=p2, end_handle=p2Control)

        groupAnterior = VGroup(bezierCurve, line1, line2, dotp1Control, dotp2Control)
        groupNuevo = VGroup(bezierCurveb, line1b, line2b, dotp1Controlb, dotp2Controlb)

        self.play(Transform(groupAnterior, groupNuevo))


class Interpolation(Scene):
    def construct(self):
        self.play(Create(plane))

        self.wait(1)

        pointsTable = Table([["Xi", "0", "1", "3"],
                             ["Yi", "3", "2", "12"]]).scale(0.4).move_to(RIGHT * 3 + UP * 3)
        self.play(Create(pointsTable), run_time=2)

        self.wait(1)

        dot1 = Dot(point=plane.c2p(0, 3)).set_color(RED)
        dot2 = Dot(point=plane.c2p(1, 2)).set_color(RED)
        dot3 = Dot(point=plane.c2p(3, 12)).set_color(RED)

        dotsGroup = VGroup(dot1, dot2, dot3)

        self.play(Create(dotsGroup), run_time=2)

        self.wait(1)

        formula = Tex(r"Funcion interpolante:$\linebreak$"
                      r"$2x^{2} - 3x + 3$", font_size=42).move_to(RIGHT * 3 + UP * 2)
        self.play(Create(formula), run_time=2)

        self.wait(1)

        interpFunc = plane.plot(lambda x: 2 * (x ** 2) - 3 * x + 3, color=DARK_BLUE)
        self.play(Create(interpFunc), run_time=4)

        self.wait(3)
