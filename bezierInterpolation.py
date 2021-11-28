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

dot1 = Dot(point=plane.c2p(-2, 23)).set_color(RED)
dot2 = Dot(point=plane.c2p(0, 3)).set_color(RED)
dot3 = Dot(point=plane.c2p(1, 2)).set_color(RED)
dot4 = Dot(point=plane.c2p(3, 18)).set_color(RED)
dot5 = Dot(point=plane.c2p(4, 35)).set_color(RED)


# --- NORMAL INTERPOLATION ---

class PolinomialInterpolation(Scene):
    def construct(self):
        pointsTable = Table([["Xi", "-2", "0", "1", "3", "4"],
                             ["Yi", "23", "3", "2", "18", "35"]]).scale(0.4).move_to(UP * 3 + RIGHT * 3)

        dotsGroup = VGroup(dot1, dot2, dot3, dot4, dot5)

        formula = Tex(r"Funcion interpolante:$\linebreak$"
                      r"$3x^{2} - 4x + 3$", font_size=42).move_to(RIGHT * 3 + UP * 2).scale(0.8)

        interpFunc = plane.plot(lambda x: 3 * (x ** 2) - 4 * x + 3, color=DARK_BLUE)

        self.add(plane, pointsTable, dotsGroup, formula, interpFunc)


# --- BEZIER INTERPOLATION ---

class BezierInterpolation(Scene):

    # find the a & b points
    def get_bezier_coef(self, thePoints):
        # since the formulas work given that we have n+1 points
        # then n must be this:
        n = len(thePoints) - 1

        # build coefficents matrix
        C = 4 * np.identity(n)
        np.fill_diagonal(C[1:], 1)
        np.fill_diagonal(C[:, 1:], 1)
        C[0, 0] = 2
        C[n - 1, n - 1] = 7
        C[n - 1, n - 2] = 2

        # build points vector
        P = [2 * (2 * thePoints[i] + thePoints[i + 1]) for i in range(n)]
        P[0] = thePoints[0] + 2 * thePoints[1]
        P[n - 1] = 8 * thePoints[n - 1] + thePoints[n]

        # solve system, find a & b
        A = np.linalg.solve(C, P)
        B = [0] * n
        for i in range(n - 1):
            B[i] = 2 * thePoints[i + 1] - A[i + 1]
        B[n - 1] = (A[n - 1] + thePoints[n]) / 2

        return A, B

    # Draw on the screen a specific bezier curve
    def draw_bezier_cubic(self, a, b, c, d):
        realA = plane.c2p(a[0], a[1])
        realB = plane.c2p(b[0], b[1])
        realC = plane.c2p(c[0], c[1])
        realD = plane.c2p(d[0], d[1])

        print(realA)
        print(realB)
        print(realC)
        print(realD)

        bezierCurveToPlot = CubicBezier(start_anchor=realA, start_handle=realB, end_handle=realC, end_anchor=realD,
                                        color=DARK_BLUE)

        self.add(bezierCurveToPlot)

    # return one cubic curve for each consecutive points
    def draw_bezier_cubics(self, thePoints):
        A, B = self.get_bezier_coef(thePoints)

        # Draw each cubic
        for i in range(len(thePoints) - 1):
            self.draw_bezier_cubic(thePoints[i], A[i], B[i], thePoints[i + 1])

    def construct(self):
        dotsGroup = VGroup(dot1, dot2, dot3, dot4, dot5)

        # The 5 numbers that I want to fit with bezier curves
        points = np.array([[-2, 23], [0, 3], [1, 2], [3, 18], [4, 35]])

        # Calculate and draw the bezier curves between the different points
        self.draw_bezier_cubics(points)

        self.add(plane, dotsGroup)