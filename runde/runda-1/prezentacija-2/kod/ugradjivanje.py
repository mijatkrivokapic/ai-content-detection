"""Embedding vectors and a translated vector analogy."""

from manim import *
import numpy as np

from manim_slides import ThreeDSlide


class Ugradjivanje(ThreeDSlide):
    BG = "#F8F9FB"
    INK = "#1F293B"
    MUTED = "#64748B"
    BLUE = "#2878F0"
    ORANGE = "#F24B0B"

    def construct(self):
        self.camera.background_color = ManimColor(self.BG)
        self.set_camera_orientation(phi=68 * DEGREES, theta=-48 * DEGREES)

        category = Text("SPOLJAŠNJI OBLIK", font_size=13, weight=BOLD, color=self.BLUE)
        category.move_to([-5.1, 3.42, 0])
        title = Text("Ugrađivanje (Embedding)", font="DejaVu Serif", font_size=39, color=self.INK)
        if title.width > 11.8:
            title.scale(11.8 / title.width)
        title.move_to([0, 2.64, 0])
        divider = Line([-5.9, 2.17, 0], [5.9, 2.17, 0], color="#D7DFEA", stroke_width=1.3)

        equation = Text(
            "(Muškarac − Žena) ≈ (Kralj − Kraljica)",
            font_size=25,
            color=self.INK,
        ).move_to([0, -2.48, 0])
        body = Text(
            "Ugrađivanje čuva odnose među pojmovima kao vektorske pomake.",
            font_size=19,
            color=self.INK,
        ).move_to([0, -3.34, 0])
        footer_line = Line([-5.9, -3.62, 0], [5.9, -3.62, 0], color="#D7DFEA", stroke_width=1)
        footer = Text(
            "Dejan Lisica  ·  Reprezentacija sadržaja i latentni prostor",
            font_size=11,
            color=self.MUTED,
        ).move_to([0, -3.82, 0])

        self.add_fixed_in_frame_mobjects(category, title, divider)

        word = Text("Mačka", font_size=48, color=self.INK).move_to([0, 0.55, 0])
        explanation = Text(
            "Posle tokenizacije, ID tokena se preslikava u naučeni niz brojeva.",
            font_size=20,
            color=self.INK,
        ).move_to([0, -1.15, 0])
        vector_label = Text("embedding vektor", font_size=18, color=self.BLUE)
        vector_label.next_to(word, DOWN, buff=0.34)
        vector_form = Text(
            "[0.24, −0.71, 0.18, 0.95, …]",
            font_size=29,
            color=self.BLUE,
        ).move_to(word)

        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            z_range=[-2, 2, 1],
            x_length=7.6,
            y_length=4.8,
            z_length=2.5,
            axis_config={
                "color": "#94A3B8",
                "stroke_width": 1.5,
                "include_ticks": False,
            },
            tips=True,
        ).shift(DOWN * 0.05)

        # The coordinates are illustrative embeddings in a 3D space.
        coords = {
            "Žena": (-3, -1, 2),
            "Muškarac": (-1, 1, 1),
            "Kraljica": (1, -1, 3),
            "Kralj": (3, 1, 2),
        }
        points = {name: axes.c2p(*xyz) for name, xyz in coords.items()}
        origin = axes.c2p(0, 0, 0)
        colors = {
            "Žena": self.BLUE,
            "Muškarac": self.BLUE,
            "Kraljica": self.ORANGE,
            "Kralj": self.ORANGE,
        }
        labels = {
            name: Text(name, font_size=17, color=colors[name]).move_to(
                point + 0.3 * (point - origin) / np.linalg.norm(point - origin)
            )
            for name, point in points.items()
        }

        # Part one: a token is mapped to a learned vector of numbers.
        self.add_fixed_in_frame_mobjects(word)
        self.play(Write(word, run_time=1.1), run_time=1.1)
        self.add_fixed_in_frame_mobjects(explanation)
        self.play(Write(explanation, run_time=1.5), run_time=1.5)
        self.wait(0.15)
        self.next_slide()

        word.align_data(vector_form.copy())
        self.add_fixed_in_frame_mobjects(word)
        self.play(
            Transform(word, vector_form, run_time=1.8),
            run_time=1.8,
        )
        self.add_fixed_in_frame_mobjects(vector_label)
        self.play(Write(vector_label, run_time=1.0), run_time=1.0)
        self.wait(0.15)
        self.next_slide()

        # Part two starts on the presenter's next key press.
        self.play(
            FadeOut(word), FadeOut(vector_label), FadeOut(explanation),
            run_time=0.8,
        )
        self.play(Create(axes, run_time=1.6), run_time=1.6)
        self.wait(0.15)
        self.next_slide()

        # Draw the four embedding vectors one at a time and leave them visible.
        embedding_vectors = {
            name: Vector(
                points[name] - origin,
                buff=0,
                color=colors[name],
                stroke_width=3.2,
                tip_length=0.32,
            )
            for name in ("Žena", "Muškarac", "Kraljica", "Kralj")
        }
        for name in ("Žena", "Muškarac", "Kraljica", "Kralj"):
            self.add_fixed_orientation_mobjects(labels[name])
            self.play(
                Write(labels[name], run_time=1.2),
                Write(embedding_vectors[name], run_time=1.2),
                run_time=1.2,
            )
            self.wait(0.15)
            self.next_slide()

        self.begin_ambient_camera_rotation(rate=0.1, about="theta")
        self.next_slide(loop=True)
        self.wait(15)
        self.stop_ambient_camera_rotation(about="theta")
        self.wait(0.15)
        self.next_slide()

        relation_vector = Vector(
            points["Muškarac"] - points["Žena"],
            buff=0,
            color=self.BLUE,
            stroke_width=4.8,
            tip_length=0.34,
        ).shift(points["Žena"])
        self.play(Write(relation_vector, run_time=1.3), run_time=1.3)
        self.wait(0.15)
        self.next_slide()

        # Keep a faint copy at the starting pair while translating the vector.
        source_ghost = relation_vector.copy().set_opacity(0.28)
        self.add(source_ghost)
        translation = points["Kraljica"] - points["Žena"]
        self.play(
            relation_vector.animate.shift(translation).set_color(self.ORANGE),
            run_time=1.6,
        )
        self.add_fixed_in_frame_mobjects(equation, body, footer_line, footer)
        self.play(
            Write(equation, run_time=1.6),
            Write(body, run_time=1.6),
            Create(footer_line, run_time=1.6),
            Write(footer, run_time=1.6),
            run_time=1.6,
        )
        self.wait(0.6)
