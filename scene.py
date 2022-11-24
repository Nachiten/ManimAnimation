from manim import *


class TableExample(Scene):
    def construct(self):
        table = Table(
            [["", "", "Cj", "4", "2,5", "3", "1,5", "", "", ""],
             ["Ck", "Xk", "B", "A1", "A2", "A3", "A4", "A5", "A6", "A7"],
             ["0", "X7", "1700", "3/2", "0", "1", "0", "0,5", "0", "1"],
             ["0", "X6", "0", "-3,5", "0", "-6", "-1", "-1,5", "1", "0"],
             ["2,5", "X2", "1000", "2,5", "1", "2", "1", "0,5", "0", "0"],
             ["Z", "=", "2500", "2,25", "0", "2", "1", "1,25", "0", "0"]],
            include_outer_lines=True)
        # Reduce table size
        table.scale(0.35)

        # Animate table creation
        self.play(table.create(), run_time=3)

        self.wait(2)

        # Highlight a cell
        cell = table.get_cell((4, 3), color="#ff0000")
        self.play(Create(cell), run_time=1)

        self.wait(1)

        # Highlight a cell
        cell = table.get_cell((1, 4), color="#0000ff")
        self.play(Create(cell), run_time=1)

        self.wait(2)

        rectangle = SurroundingRectangle(table.get_columns()[4])
        # Rectangle surronunding a cell
        self.play(Create(rectangle))

        self.wait(2)