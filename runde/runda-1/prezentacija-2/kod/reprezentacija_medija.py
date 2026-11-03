import numpy as np
from manim import *

from .pojam_base import ConceptSlide


class ReprezentacijaMedija(ConceptSlide):
    TITLE = "Reprezentacija medija"
    CATEGORY = "Spoljašnji oblik"
    BODY = "Slika daje matricu piksela, zvuk spektrogram, a tekst niz tokena."
    ACCENT = ConceptSlide.BLUE
    KEEP_VISUAL_POSITION = True

    def build_visual(self):
        # Slika: mala ilustracija ulaza i matrica vrednosti piksela.
        image_frame = RoundedRectangle(
            width=0.92, height=0.72, corner_radius=0.06,
            stroke_color=self.BLUE, stroke_width=2,
            fill_color="#E8F1FF", fill_opacity=1,
        ).move_to([-4.85, 1.08, 0])
        sun = Circle(radius=0.10, stroke_width=0, fill_color="#F5A623", fill_opacity=1)
        sun.move_to([-4.58, 1.28, 0])
        mountain_back = Polygon(
            [-5.24, 0.78, 0], [-4.92, 1.13, 0], [-4.69, 0.88, 0],
            [-4.48, 1.09, 0], [-4.43, 0.78, 0],
            stroke_width=0, fill_color="#78A7F5", fill_opacity=1,
        )
        image_label = Text("slika", font_size=16, color=self.INK).move_to([-3.85, 1.08, 0])
        image_arrow = self.arrow([-3.35, 1.08, 0], [-0.35, 1.08, 0])
        matrix_title = Text("matrica piksela", font_size=17, color=self.INK).move_to([2.05, 1.68, 0])
        values = [
            ["0.1", "0.2", "0.8", "0.9"],
            ["0.2", "0.7", "0.8", "0.3"],
            ["0.0", "0.4", "0.2", "0.1"],
        ]
        shades = ["#E7EEF8", "#C6D7EE", "#83A9D8", "#4D78B4"]
        pixel_grid = VGroup()
        for row, row_values in enumerate(values):
            for col, value in enumerate(row_values):
                cell = Square(
                    side_length=0.27,
                    stroke_color="#FFFFFF",
                    stroke_width=1,
                    fill_color=shades[(row * 2 + col) % len(shades)],
                    fill_opacity=1,
                ).move_to([1.62 + col * 0.30, 1.48 - row * 0.29, 0])
                number = Text(value, font_size=8, color=self.INK).move_to(cell)
                pixel_grid.add(VGroup(cell, number))

        # Zvuk počinje kao talasni oblik, koji se direktno menja u spektrogram.
        axes = Axes(
            x_range=[0, 2, 1], y_range=[-1, 1, 1],
            x_length=2.65, y_length=0.62,
            axis_config={"color": self.MUTED, "stroke_width": 1.2, "include_ticks": False},
            tips=False,
        ).move_to([-4.00, 0, 0])
        signal = axes.plot(
            lambda t: 0.72 * np.sin(2 * PI * 1.15 * t) * (0.72 + 0.28 * np.sin(2 * PI * 0.18 * t)),
            x_range=[0, 2], color=self.ORANGE, stroke_width=3,
        )
        signal_label = Text("talasni oblik", font_size=14, color=self.INK).move_to([-4.00, 0.42, 0])
        spectrum_label = Text("spektrogram · frekvencija × vreme", font_size=13, color=self.INK)
        spectrum_label.move_to([3.50, 0.42, 0])
        # Run the conversion arrow through the full gap between input and output.
        signal_to_spectrum = self.arrow([-2.55, 0, 0], [2.20, 0, 0])
        spectrum_values = [
            [0, 0, 1, 3, 5, 3, 1, 0],
            [0, 1, 2, 4, 5, 2, 1, 0],
            [0, 1, 3, 6, 3, 2, 1, 0],
            [0, 0, 2, 4, 4, 2, 0, 0],
            [1, 2, 3, 3, 2, 2, 1, 0],
            [0, 1, 1, 2, 3, 2, 1, 0],
        ]
        spectrum_colors = ["#172554", "#1D4ED8", "#2563EB", "#7C3AED", "#C026D3", "#F97316", "#FDE047"]
        spectrogram = VGroup()
        for row, row_values in enumerate(spectrum_values):
            for col, value in enumerate(row_values):
                cell = Rectangle(
                    width=0.27,
                    height=0.08,
                    stroke_width=0.3,
                    stroke_color=self.BG,
                    fill_color=spectrum_colors[value],
                    fill_opacity=1,
                ).move_to([2.45 + col * 0.30, 0.14 - row * 0.09, 0])
                spectrogram.add(cell)

        # Tekst: primer se razlaže u niz tokena.
        text_card = RoundedRectangle(
            width=2.55, height=0.62, corner_radius=0.06,
            stroke_color=self.BLUE, stroke_width=1.5,
            fill_color=self.BG, fill_opacity=1,
        ).move_to([-4.75, -1.26, 0])
        text_example = Text("Mačka sedi na klupi.", font_size=16, color=self.INK).move_to(text_card)
        text_label = Text("tekst", font_size=16, color=self.INK).move_to([-3.03, -1.26, 0])
        text_arrow = self.arrow([-2.43, -1.26, 0], [-0.66, -1.26, 0])
        array_label = Text("niz tokena", font_size=15, color=self.INK).move_to([2.55, -0.61, 0])
        array_tokens = VGroup(
            self.box('"Mačka"', [0.25, -1.26, 0], width=1.10, color=self.BLUE),
            self.box('"sedi"', [1.55, -1.26, 0], width=0.95, color=self.BLUE),
            self.box('"na"', [2.68, -1.26, 0], width=0.72, color=self.BLUE),
            self.box('"klupi"', [3.82, -1.26, 0], width=0.95, color=self.BLUE),
            self.box('"."', [4.82, -1.26, 0], width=0.55, color=self.BLUE),
        )
        array_brackets = VGroup(
            Text("[", font_size=38, color=self.BLUE).move_to([-0.48, -1.26, 0]),
            Text("]", font_size=38, color=self.BLUE).move_to([5.28, -1.26, 0]),
        )

        separators = VGroup(
            Line([-5.65, 0.68, 0], [5.65, 0.68, 0], color="#E5EAF1", stroke_width=1),
            Line([-5.65, -0.82, 0], [5.65, -0.82, 0], color="#E5EAF1", stroke_width=1),
        )
        static_parts = VGroup(
            separators,
            image_label, image_arrow, matrix_title,
            axes, signal_label, signal_to_spectrum,
            text_card, text_label, text_arrow, array_label,
        )
        input_parts = VGroup(
            VGroup(image_frame, sun, mountain_back),
            text_example,
        )
        array = VGroup(array_tokens, array_brackets)
        self.media_parts = {
            "static": static_parts,
            "inputs": input_parts,
            "image": input_parts[0],
            "pixels": pixel_grid,
            "signal": signal,
            "axes": axes,
            "signal_label": signal_label,
            "spectrum_label": spectrum_label,
            "spectrogram": spectrogram,
            "text": text_example,
            "array": array,
        }
        return VGroup(static_parts, input_parts, pixel_grid, signal, spectrogram, spectrum_label, array)

    def animate_visual(self, visual):
        parts = self.media_parts
        self.play(
            self.reveal_mobj(parts["static"]),
            Create(parts["image"], run_time=1.0),
            Write(parts["text"], run_time=1.0),
            Create(parts["signal"], run_time=1.0),
            run_time=1.8,
        )
        self.play(
            TransformFromCopy(parts["image"], parts["pixels"].copy()),
            run_time=1.6,
        )
        self.play(
            TransformFromCopy(parts["signal"], parts["spectrogram"].copy()),
            Write(parts["spectrum_label"], run_time=1.6),
            run_time=1.6,
        )
        self.play(
            TransformFromCopy(parts["text"], parts["array"].copy()),
            run_time=1.6,
        )
