from manim import *


def mostrarPlano(instance):
    # Lineas del plano
    plane = NumberPlane(x_range=[-6, 6, 1], y_range=[-6, 6, 1],
                        x_length=7, y_length=7,
                        background_line_style={"stroke_color": TEAL,
                                               "stroke_width": 2,
                                               "stroke_opacity": 0.2}).add_coordinates().center()

    instance.play(Create(plane, run_time=2))
    return plane


class DiferentesSenos(Scene):
    def construct(self):

        plane = mostrarPlano(self)

        # Grafico de seno
        sin_graph_1 = plane.plot(lambda x: np.sin(x), color=DARK_BLUE)
        sin_graph_2 = plane.plot(lambda x: np.sin(2 * x), color=DARK_BLUE)
        sin_graph_3 = plane.plot(lambda x: np.sin(3 * x), color=DARK_BLUE)
        sin_graph_4 = plane.plot(lambda x: 2 * np.sin(3 * x), color=DARK_BLUE)

        # Grafico de seno y coseno
        cos_sin_graph = plane.plot(lambda x: 2 * np.sin(3 * x) + np.cos(x), color=GREEN)

        # Texto seno
        sin_label_1 = plane.get_graph_label(sin_graph_1, label="sin(x)", x_val=-5, direction=UP * 4)
        sin_label_2 = plane.get_graph_label(sin_graph_1, label="sin(2x)", x_val=-5, direction=UP * 4)
        sin_label_3 = plane.get_graph_label(sin_graph_1, label="sin(3x)", x_val=-5, direction=UP * 4)
        sin_label_4 = plane.get_graph_label(sin_graph_1, label="2sin(3x)", x_val=-5, direction=UP * 4)
        cos_sin_label = plane.get_graph_label(cos_sin_graph, label="2sin(3x) + cos(x)", x_val=-5, direction=UP * 4)

        # Grafico de coseno
        cos_graph = plane.plot(lambda x: np.cos(2 * x), color=RED)
        # Texto coseno
        cos_label = plane.get_graph_label(cos_graph, label="\\cos(x)", x_val=-5, direction=DOWN * 4)

        # Crea los ejes
        self.play(Create(plane, run_time=2),
                  Create(plane, run_time=2))

        # Creo seno
        self.play(Create(sin_graph_1, run_time=2),
                  Write(sin_label_1, run_time=2))

        self.wait(1)
        self.play(Transform(sin_graph_1, sin_graph_2, run_time=1.5),
                  Transform(sin_label_1, sin_label_2, run_time=1.5))

        self.wait(1)
        self.play(Transform(sin_graph_1, sin_graph_3, run_time=1.5),
                  Transform(sin_label_1, sin_label_3, run_time=1.5))

        self.wait(1)
        self.play(Transform(sin_graph_1, sin_graph_4, run_time=1.5),
                  Transform(sin_label_1, sin_label_4, run_time=1.5))

        self.wait(1)

        # Creo coseno
        self.play(Create(cos_graph, run_time=2),
                  Write(cos_label, run_time=2))

        self.wait(1)

        # Creo senoCoseno
        self.play(Create(cos_sin_graph, run_time=2),
                  Create(cos_sin_label))

        self.wait(1)

        # Elimino seno y coseno por separado
        self.play(Uncreate(cos_graph, run_time=2),
                  Uncreate(sin_graph_1, run_time=2),
                  Uncreate(cos_label, run_time=2),
                  Uncreate(sin_label_1, run_time=2))

        self.wait(3)

        # Borro senoCoseno
        self.play(FadeOut(cos_sin_graph, run_time=1.5),
                  FadeOut(cos_sin_label, run_time=1.5))

        # Borro ejes
        self.play(Uncreate(plane), run_time=2)

        self.wait(0.5)


class FuncionDienteDeSierra(Scene):
    def construct(self):
        plane = mostrarPlano(self)

        self.wait(1)

        formula = Tex(r"f(x) = x si x $\epsilon$ (0,1) $\linebreak$"
                      r"f(x) = f(x+1)", font_size=42)
        formula.shift(UP * 3, LEFT * 3)
        self.play(Create(formula), run_time=2)

        self.wait(1)

        self.mostrarLineGraph(plane)

        self.wait(1)

        valorMedio = self.mostrarValorMedio(plane)

        self.wait(1)

        self.mostrarArea(plane, valorMedio)

        self.wait(3)

    def mostrarLineGraph(self, plane):
        line_graph = plane.plot_line_graph(
            x_values=[0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],
            y_values=[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            line_color=GOLD_E,
            vertex_dot_style=dict(stroke_width=3, fill_color=PURPLE),
            stroke_width=4, add_vertex_dots=False
        )

        self.play(Create(line_graph, run_time=2))

    def mostrarValorMedio(self, plane):
        valorMedio = plane.plot(lambda x: 0.5, color=DARK_BLUE)
        self.play(Create(valorMedio, run_time=2))
        return valorMedio

    def mostrarArea(self, plane, valorMedio):
        animations = []

        for i in range(0, 6):
            funcionCreciente = plane.plot(lambda x: x - i, color=DARK_BLUE)
            area = plane.get_area(funcionCreciente, bounded_graph=valorMedio, x_range=(i, i + 1), opacity=0.4)
            animations.append(Create(area, run_time=2))

        self.play(animations[0], animations[1], animations[2], animations[3], animations[4])


class FuncionCuadratica(Scene):
    xMin = -6
    xMax = 6

    def construct(self):

        plano2D = mostrarPlano(self)

        self.wait(1)

        formula = Tex(r"f(x) = x$^2$ si x $\epsilon$ (0,1) $\linebreak$"
                      r"f(x) = f(x+1)", font_size=42)
        formula.shift(UP * 3, LEFT * 3)
        self.play(Create(formula), run_time=2)

        self.wait(2)

        self.mostrarEquisCuadrado(plano2D)

        self.wait(2)

        valorMedio = self.mostrarValorMedio(plano2D)

        self.wait(2)

        self.mostrarArea(plano2D, valorMedio)

        self.wait(3)

    def mostrarEquisCuadrado(self, plane):
        animations = []

        for i in range(self.xMin, self.xMax):
            equisCuadrado = plane.plot(lambda x: (x - i) * (x - i), color=DARK_BLUE, x_range=(i, i + 1))
            animations.append(Create(equisCuadrado, run_time=2))

        self.play(animations[6])
        self.wait(1)
        self.play(animations[0], animations[1], animations[2], animations[3], animations[4], animations[5])
        self.wait(0.5)
        self.play(animations[7], animations[8], animations[9], animations[10], animations[11])

    def mostrarValorMedio(self, plane):
        valorMedio = plane.plot(lambda x: 0.3, color=ORANGE)
        self.play(Create(valorMedio, run_time=2))
        return valorMedio

    def mostrarArea(self, plane, valorMedio):
        animations = []

        for i in range(self.xMin, self.xMax):
            equisCuadrado = plane.plot(lambda x: (x - i) * (x - i), color=DARK_BLUE, x_range=(i, i + 1))
            area = plane.get_area(valorMedio, bounded_graph=equisCuadrado,
                                  x_range=(i, i + 1),
                                  opacity=0.4)
            animations.append(Create(area, run_time=3))

        self.play(animations[0], animations[1], animations[2], animations[3], animations[4], animations[5])


class EscalonUnitario(Scene):
    def construct(self):
        plane = mostrarPlano(self)

        # noinspection PyTypeChecker
        line_graph = plane.plot_line_graph(
            x_values=[0, 6],
            y_values=[1, 1],
            line_color=GOLD_E,
            vertex_dot_style=dict(stroke_width=3, fill_color=PURPLE),
            stroke_width=4, add_vertex_dots=False)

        self.wait(1)

        self.play(Create(line_graph, run_time=2))

        self.wait(3)
