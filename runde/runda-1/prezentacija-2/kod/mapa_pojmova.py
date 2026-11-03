from manim import *
from manim_slides import Slide


class MapaPojmova(Slide):
    """Animated concept map for the encoder/decoder architecture."""

    BG = "#F8F9FB"
    INK = "#1F293B"
    BLUE = "#2878F0"
    ORANGE = "#F24B0B"
    MUTED = "#91A3BC"
    PALE = "#E2E8F0"
    RED = "#D90808"

    def make_box(self, label, center, color, *, dark=False, dashed=False, width=2.65):
        box = RoundedRectangle(
            width=width,
            height=0.66,
            corner_radius=0.07,
            stroke_color=color,
            stroke_width=1.3,
            fill_color=self.INK if dark else (self.PALE if color == self.PALE else self.BG),
            fill_opacity=1,
        ).move_to(center)
        if dashed:
            box = DashedVMobject(box, num_dashes=42)
        text_color = self.BG if dark else self.INK
        label_mob = Text(label, font_size=16, color=text_color)
        label_mob.move_to(center)
        if label_mob.width > width - 0.18:
            label_mob.scale((width - 0.18) / label_mob.width)
        return VGroup(box, label_mob)

    def make_arrow(self, start, end, label=None, label_point=None, *, buff=0):
        arrow = Arrow(
            start,
            end,
            buff=buff,
            color=self.MUTED,
            stroke_width=1.5,
            max_tip_length_to_length_ratio=0.12,
            tip_length=0.12,
        )
        if label is None:
            return VGroup(arrow)
        note = Text(label, font_size=11, color=self.RED)
        note.move_to(label_point)
        return VGroup(arrow, note)

    def construct(self):
        self.camera.background_color = ManimColor(self.BG)

        title = Text(
            "Reprezentacija sadržaja i latentni prostor",
            font="DejaVu Serif",
            font_size=29,
            color=self.INK,
        )
        if title.width > 8.9:
            title.scale(8.9 / title.width)
        title.move_to([-2.42, 3.48, 0])
        author = Text("Autor: Dejan Lisica", font_size=12, color="#64748B")
        author.move_to([title.get_left()[0] + author.width / 2, 3.03, 0])
        note = Text("Isprekidan okvir: uzorkovana vrednost", font_size=11, color=self.RED)
        note.move_to([4.42, 3.42, 0])

        col_left = Text("SPOLJAŠNJI OBLIK", font_size=15, weight=BOLD, color=self.BLUE)
        col_mid = Text("ARHITEKTURA", font_size=15, weight=BOLD, color="#C91E1E")
        col_right = Text("UNUTRAŠNJI OBLIK", font_size=15, weight=BOLD, color=self.ORANGE)
        col_left.move_to([-4.55, 2.53, 0])
        col_mid.move_to([0, 2.53, 0])
        col_right.move_to([4.55, 2.53, 0])

        ys = [1.48, -0.17, -1.82, -3.47]
        xs = [-4.55, 0, 4.55]

        left_labels = [
            "Reprezentacija medija",
            "Tokenizacija",
            "Token",
            "Ugrađivanje (Embedding)",
        ]
        center_labels = ["Enkoder", "Rekonstrukcija", "Dekoder", "Hipoteza mnogostrukosti"]
        right_labels = ["Apriorna raspodela", "Gausov šum", "Latentni prostor", "Latentna promenljiva"]

        left_nodes = VGroup(*[
            self.make_box(text, [xs[0], y, 0], self.BLUE, width=2.65)
            for text, y in zip(left_labels, ys)
        ])
        center_nodes = VGroup(
            self.make_box(center_labels[0], [xs[1], ys[0], 0], self.INK, dark=True),
            self.make_box(center_labels[1], [xs[1], ys[1], 0], self.PALE),
            self.make_box(center_labels[2], [xs[1], ys[2], 0], self.INK, dark=True),
            self.make_box(center_labels[3], [xs[1], ys[3], 0], self.PALE, width=2.65),
        )
        right_nodes = VGroup(
            self.make_box(right_labels[0], [xs[2], ys[0], 0], self.ORANGE),
            self.make_box(right_labels[1], [xs[2], ys[1], 0], self.MUTED, dashed=True),
            self.make_box(right_labels[2], [xs[2], ys[2], 0], self.INK, dark=True),
            self.make_box(right_labels[3], [xs[2], ys[3], 0], self.ORANGE),
        )

        arrows = VGroup(
            # Input representation and tokenization pipeline.
            self.make_arrow([-3.19, 1.48, 0], [-1.37, 1.48, 0], "predaje se u", [-2.28, 1.72, 0]),
            self.make_arrow([-4.55, 1.11, 0], [-4.55, 0.22, 0], "tekst prolazi kroz", [-5.22, 0.66, 0]),
            self.make_arrow([-4.55, -0.54, 0], [-4.55, -1.45, 0], "daje niz", [-5.08, -0.98, 0]),
            self.make_arrow([-4.55, -2.19, 0], [-4.55, -3.10, 0], "predstavlja se kao", [-5.13, -2.67, 0]),
            # Encoder, reconstruction and decoder steps.
            self.make_arrow([0, 1.10, 0], [0, 0.21, 0], "1. korak", [-0.04, 0.66, 0]),
            self.make_arrow([0, -1.45, 0], [0, -0.54, 0], "2. korak", [0.42, -0.99, 0]),
            self.make_arrow([-0.88, -1.48, 0], [-3.24, 0.99, 0], "vraća nazad u", [-2.49, -0.20, 0]),
            # Latent-space connections and sampling path.
            self.make_arrow([0.88, 1.20, 0], [3.22, -1.48, 0], "sažima u", [2.14, -0.02, 0]),
            self.make_arrow([3.22, -1.82, 0], [1.37, -1.82, 0], "ulazi u", [2.28, -1.57, 0]),
            self.make_arrow([4.55, 1.11, 0], [4.55, 0.22, 0], "uzorkuje se kao", [4.55, 0.66, 0]),
            self.make_arrow([4.55, -0.54, 0], [4.55, -1.45, 0], "inicijalizuje", [4.55, -0.99, 0]),
            self.make_arrow([4.55, -2.19, 0], [4.55, -3.10, 0], "čine ga", [4.55, -2.67, 0]),
            self.make_arrow([1.34, -3.30, 0], [3.24, -2.15, 0], "opravdava dimenziju", [2.27, -2.75, 0]),
        )

        self.play(
            Write(title, run_time=1.5),
            Write(author, run_time=1.5),
            Write(note, run_time=1.5),
            run_time=1.5,
        )
        self.play(
            LaggedStart(
                Write(col_left, run_time=1.0),
                Write(col_mid, run_time=1.0),
                Write(col_right, run_time=1.0),
                lag_ratio=0.2,
            ),
            run_time=1.5,
        )
        self.play(
            LaggedStart(
                *[AnimationGroup(Create(node[0], run_time=1.0), Write(node[1], run_time=1.0), run_time=1.0) for node in left_nodes],
                *[AnimationGroup(Create(node[0], run_time=1.0), Write(node[1], run_time=1.0), run_time=1.0) for node in center_nodes],
                *[AnimationGroup(Create(node[0], run_time=1.0), Write(node[1], run_time=1.0), run_time=1.0) for node in right_nodes],
                lag_ratio=0.08,
            ),
            run_time=2.8,
        )
        self.play(LaggedStart(*[GrowArrow(item[0], run_time=1.0) for item in arrows], lag_ratio=0.05), run_time=2.2)
        self.play(LaggedStart(*[Write(item[1], run_time=1.0) for item in arrows], lag_ratio=0.05), run_time=1.8)
        self.wait(0.5)
