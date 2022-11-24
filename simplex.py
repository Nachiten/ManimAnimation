from manim import *


# self.wait(1)
#
# # Highlight a cell
# cellRed = table.get_cell((4, 3), color="#ff0000")
# self.play(Create(cellRed), run_time=1)
#
# self.wait(1)
#
# # Highlight a cell
# cellBlue = table.get_cell((1, 4), color="#0000ff")
# self.play(Create(cellBlue), run_time=1)
#
# self.wait(1)
#
# yellowRectangle = SurroundingRectangle(table.get_columns()[4], color=YELLOW)
# # Rectangle surrounding a cell
# self.play(Create(yellowRectangle))

class SimplexTest(Scene):
    tableScale = 0.35

    def construct(self):
        # Create table
        table = Table(
            [["", "", "Cj", "4", "2,5", "3", "1,5", "", "", ""],
             ["Ck", "Xk", "B", "A1", "A2", "A3", "A4", "A5", "A6", "A7"],
             ["0", "X7", "1700", "3/2", "0", "1", "0", "0,5", "0", "1"],
             ["0", "X6", "0", "-3,5", "0", "-6", "-1", "-1,5", "1", "0"],
             ["2,5", "X2", "1000", "2,5", "1", "2", "1", "0,5", "0", "0"],
             ["Z", "=", "2500", "2,25", "0", "2", "1", "1,25", "0", "0"]],
            include_outer_lines=True)
        # Reduce table size
        table.scale(self.tableScale)

        # Animate table creation
        self.play(table.create(), run_time=3)
        self.wait(1)

        # redRectangle = Rectangle(height=1.5, width=0.5, color=BLUE)
        # redRectangle.move_to(table.get_cell((4, 7)))
        #
        # self.play(Create(redRectangle))
        # self.wait(1)

        # Set value of 4,6 (2,25) to 1238
        cell46 = table.get_entries((4, 6))
        cosa = cell46.become(Text("1238").scale(self.tableScale).move_to(cell46).set_color(cell46.get_color()))
        # table.add_highlighted_cell((4, 6), color=YELLOW)

        self.play(Create(cosa), run_time=0.3)
        # self.play(table.update())

        table.add_highlighted_cell((4, 6), color=YELLOW)

        # Update table visual
        self.play(table.update())

        self.wait(2)

        # Make group with everything
        # group = VGroup(table, yellowRectangle, redRectangle, cellRed, cellBlue)
        # group = VGroup(table, redRectangle)
        # # Animate removing group
        # self.play(FadeOut(group), run_time=1)


class Dyntable(Scene):
    def construct(self):
        table = Table(
            [["This", "is a"],
             ["simple", "Table."]]
        )

        self.add(table)
        self.wait(2)

        field = table.get_entries((2, 1)).animate.set_color(RED)

        self.wait(2)
        # field.become(Text("changed").move_to(field).set_color(field.get_color()))
        self.play(
            ReplacementTransform(
                field,
                Text("changed").move_to(field).set_color(field.get_color())
            )
        )
        self.wait(2)
