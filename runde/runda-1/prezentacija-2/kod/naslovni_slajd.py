from manim import *
from manim_slides import Slide


class NaslovniSlajd(Slide):
    """Opening title slide for the concept-map presentation."""

    def construct(self):
        self.camera.background_color = ManimColor("#F8F9FB")

        accent = VGroup(
            Line([-4.5, -0.55, 0], [4.5, -0.55, 0], color="#D7DFEA", stroke_width=1.5),
            Line([-4.5, -0.55, 0], [-2.7, -0.55, 0], color="#2878F0", stroke_width=4),
        )
        title = Text(
            "Reprezentacija sadržaja\ni latentni prostor",
            font="DejaVu Serif",
            font_size=48,
            line_spacing=0.9,
            color="#1F293B",
        )
        title.move_to([0, 0.72, 0])

        author = Text("Dejan Lisica", font_size=24, color="#53657D")
        author.move_to([0, -1.12, 0])

        dots = VGroup(
            *[
                Dot(point, radius=0.07, color=color)
                for point, color in zip(
                    [[-0.28, -2.08, 0], [0, -2.08, 0], [0.28, -2.08, 0]],
                    ["#2878F0", "#91A3BC", "#F24B0B"],
                )
            ]
        )

        self.play(Write(title, run_time=2.0), run_time=2.0)
        self.play(Create(accent, run_time=1.4), Write(author, run_time=1.4), run_time=1.4)
        self.play(LaggedStart(*[Create(d, run_time=1.0) for d in dots], lag_ratio=0.25), run_time=1.0)
        self.wait(0.5)


