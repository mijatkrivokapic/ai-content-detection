"""Shared layout and visual helpers for individual concept slides."""

from manim import *
from manim_slides import Slide


class ConceptSlide(Slide):
    BG = "#F8F9FB"
    INK = "#1F293B"
    MUTED = "#64748B"
    BLUE = "#2878F0"
    ORANGE = "#F24B0B"
    PALE = "#E2E8F0"

    TITLE = "Pojam"
    CATEGORY = "POJMOVI"
    BODY = ""
    VISUAL = "representation"
    ACCENT = BLUE
    KEEP_VISUAL_POSITION = False

    def box(self, label, center, width=2.25, color=None, fill=None):
        color = color or self.ACCENT
        fill = fill or self.BG
        shape = RoundedRectangle(
            width=width,
            height=0.72,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=1.8,
            fill_color=fill,
            fill_opacity=1,
        ).move_to(center)
        text = Text(label, font_size=20, color=self.INK)
        if text.width > width - 0.22:
            text.scale((width - 0.22) / text.width)
        text.move_to(center)
        return VGroup(shape, text)

    def arrow(self, start, end):
        return Arrow(start, end, buff=0.08, color=self.MUTED, stroke_width=2, tip_length=0.16)

    def build_visual(self):
        kind = self.VISUAL
        if kind == "representation":
            cards = VGroup(
                self.box("Tekst", [-3.5, 0.25, 0], color=self.BLUE),
                self.box("Slika", [-3.5, -0.75, 0], color=self.BLUE),
                self.box("Zvuk", [-3.5, -1.75, 0], color=self.BLUE),
                self.box("ulaz modela", [3.25, -0.25, 0], width=2.6, color=self.INK, fill=self.PALE),
            )
            lines = VGroup(
                self.arrow([-2.3, 0.25, 0], [1.9, -0.05, 0]),
                self.arrow([-2.3, -0.75, 0], [1.9, -0.25, 0]),
                self.arrow([-2.3, -1.75, 0], [1.9, -0.45, 0]),
            )
            return VGroup(lines, cards)

        if kind == "tokenization":
            source = Text('"Mačka sedi."', font_size=32, color=self.INK).move_to([0, 1.0, 0])
            tokens = VGroup(
                self.box("Mačka", [-2.45, -0.25, 0], width=2.0, color=self.BLUE),
                self.box("sedi", [0, -0.25, 0], width=2.0, color=self.BLUE),
                self.box(".", [2.45, -0.25, 0], width=1.0, color=self.BLUE),
            )
            split = Text("tokenizacija", font_size=17, color=self.MUTED).move_to([0, 0.48, 0])
            return VGroup(source, split, tokens)

        if kind == "token":
            token = self.box("mačka", [-2.45, 0.15, 0], width=2.25, color=self.BLUE)
            arrow = self.arrow([-1.2, 0.15, 0], [0.4, 0.15, 0])
            id_card = self.box("token ID", [2.2, 0.15, 0], width=2.4, color=self.ORANGE)
            note = Text("jedna stavka iz rečnika modela", font_size=19, color=self.MUTED).move_to([0, -0.95, 0])
            return VGroup(token, arrow, id_card, note)

        if kind == "embedding":
            label = Text("token", font_size=22, color=self.INK).move_to([-3.5, 0.25, 0])
            arrow = self.arrow([-2.8, 0.25, 0], [-1.75, 0.25, 0])
            vector_label = Text("embedding vektora", font_size=20, color=self.MUTED).move_to([1.15, 1.05, 0])
            values = [0.52, 0.9, 0.36, 1.25, 0.68, 1.02, 0.43]
            bars = VGroup()
            for i, height in enumerate(values):
                bar = RoundedRectangle(
                    width=0.48,
                    height=height,
                    corner_radius=0.06,
                    stroke_width=0,
                    fill_color=self.ACCENT if i % 2 == 0 else "#78A7F5",
                    fill_opacity=0.95,
                ).move_to([-1.05 + i * 0.7, -0.35 + height / 2, 0])
                bars.add(bar)
            dots = Text("…", font_size=35, color=self.MUTED).next_to(bars, RIGHT, buff=0.25)
            return VGroup(label, arrow, vector_label, bars, dots)

        if kind in ("encoder", "decoder"):
            widths = [3.6, 2.7, 1.8, 1.05] if kind == "encoder" else [1.05, 1.8, 2.7, 3.6]
            labels = ["ulaz", "sloj", "sloj", "z"] if kind == "encoder" else ["z", "sloj", "sloj", "izlaz"]
            layers = VGroup()
            x_positions = [-4.35, -1.65, 1.05, 3.75]
            arrows = VGroup()
            for i, (width, label, x) in enumerate(zip(widths, labels, x_positions)):
                layers.add(self.box(label, [x, 0.1, 0], width=width, color=self.ACCENT if i in (0, 3) else self.MUTED,
                                    fill=self.PALE if i in (1, 2) else self.BG))
                if i < len(x_positions) - 1:
                    arrows.add(self.arrow([x + width / 2, 0.1, 0], [x_positions[i + 1] - widths[i + 1] / 2, 0.1, 0]))
            direction = "sabija informacije" if kind == "encoder" else "širi latentni opis"
            caption = Text(direction, font_size=19, color=self.MUTED).move_to([0, -1.0, 0])
            return VGroup(arrows, layers, caption)

        if kind == "reconstruction":
            original = self.box("original", [-3.1, 0.2, 0], width=2.5, color=self.BLUE)
            output = self.box("rekonstrukcija", [3.1, 0.2, 0], width=3.1, color=self.ORANGE)
            arrow = self.arrow([-1.7, 0.2, 0], [1.4, 0.2, 0])
            match = Text("što sličnije", font_size=18, color=self.MUTED).move_to([0, 0.65, 0])
            return VGroup(original, output, arrow, match)

        if kind == "manifold":
            axes = Axes(
                x_range=[-4, 4, 1], y_range=[-1.8, 1.8, 1],
                x_length=8.4, y_length=3.0,
                axis_config={"color": self.MUTED, "stroke_width": 1.4, "include_ticks": False},
                tips=False,
            )
            curve = axes.plot(lambda x: 0.42 * np.sin(0.92 * x) + 0.05 * x, x_range=[-3.8, 3.8], color=self.ACCENT, stroke_width=4)
            dots = VGroup(*[
                Dot(axes.c2p(x, 0.42 * np.sin(0.92 * x) + 0.05 * x), radius=0.065, color=self.ORANGE)
                for x in [-3.1, -2.0, -0.7, 0.7, 1.9, 3.1]
            ])
            caption = Text("podaci se grupišu oko niže-dimenzionalne strukture", font_size=18, color=self.MUTED)
            caption.next_to(axes, DOWN, buff=0.15)
            return VGroup(axes, curve, dots, caption)

        if kind in ("prior", "noise"):
            axes = Axes(
                x_range=[-3.5, 3.5, 1], y_range=[0, 1.5, 0.5],
                x_length=7.6, y_length=2.8,
                axis_config={"color": self.MUTED, "stroke_width": 1.4, "include_ticks": False},
                tips=False,
            )
            curve = axes.plot(lambda x: 1.2 * np.exp(-(x**2) / 2), x_range=[-3.2, 3.2], color=self.ACCENT, stroke_width=4)
            elements = [axes, curve]
            if kind == "prior":
                label = Text("P(z)", font_size=30, color=self.INK).move_to([0, 1.15, 0])
                elements.append(label)
            else:
                sample_x = 1.15
                sample_y = 1.2 * np.exp(-(sample_x**2) / 2)
                sample = Dot(axes.c2p(sample_x, sample_y), radius=0.11, color=self.ORANGE)
                guide = DashedLine(axes.c2p(sample_x, 0), axes.c2p(sample_x, sample_y), color=self.ORANGE)
                label = Text("slučajan uzorak", font_size=18, color=self.ORANGE).move_to([2.5, 1.2, 0])
                elements.extend([guide, sample, label])
            return VGroup(*elements)

        if kind == "latent_space":
            axes = Axes(
                x_range=[-4, 4, 1], y_range=[-2.4, 2.4, 1],
                x_length=8.4, y_length=3.7,
                axis_config={"color": self.MUTED, "stroke_width": 1.4, "include_ticks": False},
                tips=False,
            )
            clusters = [
                ([-2.2, -1.5, -2.8, -1.8], [0.9, 1.35, 0.45, 1.0], self.BLUE, "mačke"),
                ([1.0, 1.6, 2.1, 2.7], [-0.9, -1.35, -0.55, -1.0], self.ORANGE, "psi"),
            ]
            marks = VGroup()
            for xs, ys, color, label in clusters:
                marks.add(*[Dot(axes.c2p(x, y), radius=0.08, color=color) for x, y in zip(xs, ys)])
                center = axes.c2p(sum(xs) / len(xs), sum(ys) / len(ys))
                marks.add(Text(label, font_size=17, color=color).move_to(center + np.array([0, 0.35, 0])))
            return VGroup(axes, marks)

        if kind == "latent_variable":
            equation = Text("z = μ + σ · ε", font_size=48, color=self.INK).move_to([0, 0.5, 0])
            captions = VGroup(
                Text("srednja vrednost", font_size=17, color=self.BLUE).move_to([-3.3, -0.55, 0]),
                Text("rasipanje", font_size=17, color=self.ORANGE).move_to([0, -0.55, 0]),
                Text("slučajni šum", font_size=17, color="#74849A").move_to([3.3, -0.55, 0]),
            )
            return VGroup(equation, captions)

        raise ValueError(f"Unknown concept visual: {kind}")

    def reveal_mobj(self, mobj):
        """Uses Write for text/formulas/vectors and Create for geometric shapes."""
        if isinstance(mobj, (Text, MarkupText, Tex, MathTex, Vector)):
            return Write(mobj, run_time=1.0)
        if isinstance(mobj, Arrow):
            return GrowArrow(mobj, run_time=1.0)
        if isinstance(mobj, VGroup) and len(mobj.submobjects) > 0:
            # Ako grupa sadrži i oblik (npr. karticu/okvir) i tekst, kreiraj oblik a ispiši tekst
            has_text = any(isinstance(sub, (Text, MarkupText, Tex, MathTex)) for sub in mobj.family_members_with_points())
            has_geom = any(
                not isinstance(sub, (Text, MarkupText, Tex, MathTex, VGroup))
                for sub in mobj.family_members_with_points()
            )
            if has_text and has_geom:
                return AnimationGroup(*[self.reveal_mobj(sub) for sub in mobj.submobjects], run_time=1.0)
        return Create(mobj, run_time=1.0)

    def animate_visual(self, visual):
        self.play(self.reveal_mobj(visual), run_time=1.8)

    def construct(self):
        self.camera.background_color = ManimColor(self.BG)
        category = Text(self.CATEGORY.upper(), font_size=13, weight=BOLD, color=self.ACCENT)
        category.move_to([-5.1, 3.42, 0])
        title = Text(self.TITLE, font="DejaVu Serif", font_size=39, color=self.INK)
        if title.width > 11.8:
            title.scale(11.8 / title.width)
        title.move_to([0, 2.64, 0])
        divider = Line([-5.9, 2.17, 0], [5.9, 2.17, 0], color="#D7DFEA", stroke_width=1.3)
        visual = self.build_visual()
        if not self.KEEP_VISUAL_POSITION:
            visual.move_to([0, 0.15, 0])
        body = Text(self.BODY, font_size=22, color=self.INK, line_spacing=0.9)
        if body.width > 11.7:
            body.scale(11.7 / body.width)
        body.move_to([0, -2.65, 0])
        footer_line = Line([-5.9, -3.45, 0], [5.9, -3.45, 0], color="#D7DFEA", stroke_width=1)
        footer = Text("Dejan Lisica  ·  Reprezentacija sadržaja i latentni prostor", font_size=11, color=self.MUTED)
        footer.move_to([0, -3.7, 0])

        self.play(
            Write(category, run_time=1.0),
            Write(title, run_time=1.0),
            Create(divider, run_time=1.0),
            Create(footer_line, run_time=1.0),
            Write(footer, run_time=1.0),
            run_time=1.6,
        )
        self.animate_visual(visual)
        self.play(Write(body, run_time=1.8), run_time=1.8)
        self.wait(0.4)
