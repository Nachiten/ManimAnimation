from manim import *


class Dyntable(Scene):
    def construct(self):
        table = Table(
            [["250", "300"],
             ["135", "20"]]
        )

        self.play(Create(table), run_time=1.5)
        self.wait(2)

        field = table.get_entries((2, 1))
        self.play(field.animate.set_color(RED), run_time=0.5)
        self.wait(2)

        self.play(
            ReplacementTransform(
                field,
                Text("238").move_to(field).set_color(field.get_color())
            ), run_time=0.5
        )
        self.wait(2)
