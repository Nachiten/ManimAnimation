from manim import *

os.system("")

xMin, xMax = -15, 15
yMin, yMax = -15, 60
xLength, yLength = 7, 7

plane = Axes(x_range=[xMin, xMax, 5], y_range=[yMin, yMax, 5],
             x_length=xLength, y_length=yLength).add_coordinates().move_to(LEFT * 2)

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


dot1 = Dot(point=plane.c2p(-2, 23)).set_color(RED)
dot2 = Dot(point=plane.c2p(0, 3)).set_color(RED)
dot3 = Dot(point=plane.c2p(1, 2)).set_color(RED)
dot4 = Dot(point=plane.c2p(3, 18)).set_color(RED)
dot5 = Dot(point=plane.c2p(4, 35)).set_color(RED)


class CalculoPolInter(Scene):
    def construct(self):
        pointsTable = Table([["Xi", "-2", "0", "1", "3", "4"],
                             ["Yi", "23", "3", "2", "18", "35"]]).scale(0.4).move_to(UP * 3)
        self.play(Create(pointsTable), run_time=2)

        self.wait(1)

        texto1 = Tex("Vamos a calcular el polinomio interpolante:").scale(0.5).move_to(UP * 2)
        self.play(Create(texto1))

        self.wait(2)

        pointsTableVertical = Table([["Xi", "Yi"],
                                     ["-2", "23"],
                                     ["0", "3"],
                                     ["1", "2"],
                                     ["3", "18"],
                                     ["4", "35"]]).move_to(LEFT * 3).scale(0.4)

        self.play(texto1.animate.move_to(UP * 3.5),
                  Transform(pointsTable, pointsTableVertical), run_time=2)

        self.wait(1)

        # orden1 = Table([["Orden 1"], ["-10"], ["-1"], ["8"], ["17"]]).move_to(LEFT * 1.5 + UP * 0.025)
        orden1 = Table([["Orden 1"], ["(3 - 23) / (0 - (-2))"], ["-"], ["-"], ["-"]]).move_to(LEFT * 1.5 + UP * 0.025)
        orden1.remove(*orden1.get_horizontal_lines()).scale(0.4)
        self.play(Create(orden1))

        self.wait(1)

        pointsTableVertical.add(pointsTableVertical.get_cell((3, 2), color=RED).scale(0.4))
        pointsTableVertical.add(pointsTableVertical.get_cell((2, 2), color=GREEN).scale(0.4))
        pointsTableVertical.add(pointsTableVertical.get_cell((3, 1), color=BLUE).scale(0.4))
        pointsTableVertical.add(pointsTableVertical.get_cell((2, 1), color=YELLOW).scale(0.4))

        self.play(Transform(pointsTable, pointsTableVertical), run_time=2)

        self.wait(1)

        self.wait(3)
