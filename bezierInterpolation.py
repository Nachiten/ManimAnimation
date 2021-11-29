from manim import *

os.system("")

'''
# Case 2
xMin, xMax = -50, 50
yMin, yMax = -20, 25
xLength, yLength = 7, 7

# Case 2
plane = Axes(x_range=[xMin, xMax, 5], y_range=[yMin, yMax, 5],
             x_length=xLength, y_length=yLength).add_coordinates(font_size=22).move_to(LEFT * 2)
'''

# Case 1:
xMin, xMax = -6, 6
yMin, yMax = -5, 40
xLength, yLength = 7, 7

# Case 1
plane = Axes(x_range=[xMin, xMax, 1], y_range=[yMin, yMax, 5],
             x_length=xLength, y_length=yLength).add_coordinates(font_size=22).move_to(LEFT * 2)


dot1 = Dot(point=plane.c2p(-2, 23)).set_color(RED)
dot2 = Dot(point=plane.c2p(0, 3)).set_color(RED)
dot3 = Dot(point=plane.c2p(1, 2)).set_color(RED)
dot4 = Dot(point=plane.c2p(3, 18)).set_color(RED)
dot5 = Dot(point=plane.c2p(4, 35)).set_color(RED)


# --- NORMAL INTERPOLATION ---

class PolinomialInterpolationCase1(Scene):
    def construct(self):
        movimientoDerecha = 4

        # Tabla de puntos
        puntos = Tex("Puntos:").move_to(RIGHT * movimientoDerecha + UP * 3.7).scale(0.8)
        pointsTable = Table([["Xi", "-2", "0", "1", "3", "4"],
                             ["Yi", "23", "3", "2", "18", "35"]]).move_to(RIGHT * movimientoDerecha + UP * 2.9) \
            .scale(0.4)

        # Formula
        formula = Tex(r"Funcion interpolante:$\linebreak$"
                      r"$3x^{2} - 4x + 3$", font_size=42).move_to(RIGHT * movimientoDerecha + UP * 1.8).scale(0.8)

        nombreMetodo = Tex("Interpolación Polinomica:").move_to(LEFT * 5 + UP * 3.7).scale(0.65)

        dotsGroup = VGroup(dot1, dot2, dot3, dot4, dot5)

        interpFunc = plane.plot(lambda x: 3 * (x ** 2) - 4 * x + 3, color=DARK_BLUE)

        self.add(plane, pointsTable, dotsGroup, formula, interpFunc, puntos, nombreMetodo)


# --- BEZIER INTERPOLATION ---

def get_bezier_coef(thePoints):
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
def draw_bezier_cubic(instance, a, b, c, d):
    realA = plane.c2p(a[0], a[1])
    realB = plane.c2p(b[0], b[1])
    realC = plane.c2p(c[0], c[1])
    realD = plane.c2p(d[0], d[1])

    bezierCurveToPlot = CubicBezier(start_anchor=realA, start_handle=realB, end_handle=realC, end_anchor=realD,
                                    color=DARK_BLUE)

    dotp1Control = Dot(point=realB).set_color(LIGHT_GRAY).scale(0.75)
    dotp2Control = Dot(point=realC).set_color(LIGHT_GRAY).scale(0.75)

    line1 = Line(realA, realB).set_color(ORANGE).set_stroke(width=2, opacity=0.5)
    line3 = Line(realC, realD).set_color(ORANGE).set_stroke(width=2, opacity=0.5)

    linesGroup = VGroup(line1, line3)

    instance.add(bezierCurveToPlot, dotp1Control, dotp2Control, linesGroup)


# return one cubic curve for each consecutive points
def draw_bezier_cubics(instance, thePoints):
    A, B = get_bezier_coef(thePoints)

    # Draw each cubic
    for i in range(len(thePoints) - 1):
        draw_bezier_cubic(instance, thePoints[i], A[i], B[i], thePoints[i + 1])


class BezierInterpolationCase1(Scene):

    def construct(self):
        movimientoDerecha = 4

        # Tabla de puntos
        puntos = Tex("Puntos:").move_to(RIGHT * movimientoDerecha + UP * 3.7).scale(0.8)
        pointsTable = Table([["Xi", "-2", "0", "1", "3", "4"],
                             ["Yi", "23", "3", "2", "18", "35"]]).move_to(RIGHT * movimientoDerecha + UP * 2.9) \
            .scale(0.4)

        # Nombre del metodo
        nombreMetodo = Tex("Interpolación con Bézier:").move_to(LEFT * 5 + UP * 3.7).scale(0.65)

        dotsGroup = VGroup(dot1, dot2, dot3, dot4, dot5)

        # The 5 numbers that I want to fit with bezier curves
        points = np.array([[-2, 23], [0, 3], [1, 2], [3, 18], [4, 35]])

        # Calculate and draw the bezier curves between the different points
        draw_bezier_cubics(self, points)

        self.add(plane, dotsGroup, puntos, pointsTable, nombreMetodo)


class BezierInterpolationCase2(Scene):

    def construct(self):
        movimientoDerecha = 4

        # Tabla de puntos
        puntos = Tex("Puntos:").move_to(RIGHT * movimientoDerecha + UP * 3.7).scale(0.8)
        pointsTable = Table([["Xi", "-45", "-37", "-22", "-13", "-6", "0"],
                             ["Yi", "5", "13", "7", "-10", "18", "-5"]]).move_to(RIGHT * movimientoDerecha + UP * 2.9) \
            .scale(0.3)

        # Nombre del metodo
        nombreMetodo = Tex("Interpolación con Bézier:").move_to(LEFT * 5 + UP * 3.7).scale(0.65)

        # The 5 numbers that I want to fit with bezier curves
        points = np.array([[-45, 5], [-37, 13], [-22, 7], [-13, -10], [-6, 18], [0, -5]])

        # [6, 5], [15, -7], [22, 14], [30, -4]])

        # Muestro todos los puntos
        for point in points:
            coords = plane.c2p(point[0], point[1])
            unDot = Dot(point=coords).set_color(RED).scale(0.9)
            self.add(unDot)

        # Calculate and draw the bezier curves between the different points
        draw_bezier_cubics(self, points)

        self.add(plane, puntos, pointsTable, nombreMetodo)


dots = [[-45, 5], [-37, 13], [-22, 7], [-13, -10], [-6, 18], [0, -5]]


class PolinomialInterpolationCase2(Scene):
    def construct(self):
        movimientoDerecha = 4

        # Tabla de puntos
        puntos = Tex("Puntos:").move_to(RIGHT * movimientoDerecha + UP * 3.7).scale(0.8)
        pointsTable = Table([["Xi", "-45", "-37", "-22", "-13", "-6", "0"],
                             ["Yi", "5", "13", "7", "-10", "18", "-5"]]).move_to(RIGHT * movimientoDerecha + UP * 2.9) \
            .scale(0.3)

        # Formula
        formula = Tex(r"Función interpolante:$\linebreak"
                      r"-\frac{1858169 x^5}{43459004160} "
                      r"-\frac{319580881 x^4}{65188506240} "
                      r"-\frac{25351954687 x^3}{130377012480} \linebreak"
                      r"-\frac{100269393173 x^2}{32594253120} "
                      r"-\frac{35406799913 x}{2172950208} "
                      r"-5$", font_size=42)\
            .move_to(RIGHT * movimientoDerecha + UP * 1.8).scale(0.7)

        nombreMetodo = Tex("Interpolación Polinomica:").move_to(LEFT * 5 + UP * 3.7).scale(0.65)

        for dot in dots:
            unDot = Dot(point=plane.c2p(dot[0], dot[1])).set_color(RED).scale(0.9)
            self.add(unDot)

        interpFunc = plane.plot(lambda x: -(1858169 * (x ** 5)) / 43459004160
                                          - (319580881 * (x ** 4)) / 65188506240
                                          - (25351954687 * (x ** 3)) / 130377012480
                                          - (100269393173 * (x ** 2)) / 32594253120
                                          - (35406799913 * x) / 2172950208 - 5, color=DARK_BLUE)

        self.add(plane, pointsTable, formula, interpFunc, puntos, nombreMetodo)
