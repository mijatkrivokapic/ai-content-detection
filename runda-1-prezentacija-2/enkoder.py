from manim import *

from .pojam_base import ConceptSlide


class Enkoder(ConceptSlide):
    TITLE = "Enkoder: sažimanje u suštinu"
    CATEGORY = "Arhitektura"
    BODY = (
        "Enkoder postepeno odbacuje suvišne detalje i svodi glomazan ulaz\n"
        "na kompaktan unutrašnji zapis (suštinu sadržaja)."
    )
    ACCENT = "#C91E1E"
    KEEP_VISUAL_POSITION = True

    def _stage_block(self, title_str, sub_str, width, height, stroke_c, fill_c, title_c, sub_c):
        rect = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.10,
            stroke_color=stroke_c,
            stroke_width=1.8,
            fill_color=fill_c,
            fill_opacity=1,
        )
        t_mob = Text(title_str, font_size=14, weight=BOLD, color=title_c)
        if t_mob.width > width - 0.16:
            t_mob.scale((width - 0.16) / t_mob.width)
        s_mob = Text(sub_str, font_size=10.5, color=sub_c)
        if s_mob.width > width - 0.16:
            s_mob.scale((width - 0.16) / s_mob.width)
        t_mob.move_to(rect.get_center() + UP * 0.16)
        s_mob.move_to(rect.get_center() + DOWN * 0.16)
        return VGroup(rect, t_mob, s_mob)

    def _info_card(self, title_str, body_str, x_pos, y_pos, accent_color, bold_map=None):
        bg = RoundedRectangle(
            width=5.72,
            height=1.35,
            corner_radius=0.12,
            stroke_color="#CBD5E1",
            stroke_width=1.3,
            fill_color="#FFFFFF",
            fill_opacity=1,
        ).move_to([x_pos, y_pos, 0])

        title = Text(title_str, font_size=13.5, weight=BOLD, color=accent_color)
        title.move_to([
            bg.get_left()[0] + 0.30 + title.width / 2,
            bg.get_top()[1] - 0.30,
            0,
        ])

        body = Text(
            body_str,
            font_size=12,
            color="#334155",
            line_spacing=0.85,
            t2w=bold_map or {},
            t2c={k: self.INK for k in (bold_map or {})},
        )
        body.move_to([
            bg.get_left()[0] + 0.30 + body.width / 2,
            y_pos - 0.16,
            0,
        ])
        return VGroup(bg, title, body)

    def build_visual(self):
        # ── GORNJI PANEL: Levak sažimanja ──
        top_panel = RoundedRectangle(
            width=11.8,
            height=2.20,
            corner_radius=0.12,
            stroke_color="#CBD5E1",
            stroke_width=1.3,
            fill_color="#FFFFFF",
            fill_opacity=1,
        ).move_to([0, 0.72, 0])

        top_heading = Text(
            "1. POSTEPENO SUŽAVANJE KROZ SLOJEVE (LEVAK INFORMACIJA)",
            font_size=13,
            weight=BOLD,
            color="#0284C7",
        )
        top_heading.move_to([
            top_panel.get_left()[0] + 0.35 + top_heading.width / 2,
            top_panel.get_top()[1] - 0.30,
            0,
        ])

        top_note = Text(
            "Manje brojeva  ·  Viši nivo apstrakcije",
            font_size=11.5,
            color=self.MUTED,
        )
        top_note.move_to([
            top_panel.get_right()[0] - 0.35 - top_note.width / 2,
            top_panel.get_top()[1] - 0.30,
            0,
        ])

        cy = 0.52
        specs = [
            ("Sirovi ulaz", "hiljade vrednosti", 2.15, 1.38, "#0284C7", "#E0F2FE", "#0369A1", "#0284C7", -4.40),
            ("Sloj 1", "osnovni oblici", 1.95, 1.14, "#64748B", "#F1F5F9", "#1E293B", "#64748B", -1.55),
            ("Sloj 2", "bitna svojstva", 1.80, 0.92, "#475569", "#E2E8F0", "#0F172A", "#475569", 1.15),
            ("Sažeti zapis", "sama suština", 1.95, 0.72, "#EA580C", "#FFEDD5", "#9A3412", "#C2410C", 3.90),
        ]

        # Trapezi u pozadini koji vizuelizuju levak
        funnel_guides = VGroup()
        for i in range(len(specs) - 1):
            _, _, w1, h1, _, _, _, _, x1 = specs[i]
            _, _, w2, h2, _, _, _, _, x2 = specs[i + 1]
            trap = Polygon(
                [x1 + w1 / 2, cy + h1 / 2 - 0.06, 0],
                [x2 - w2 / 2, cy + h2 / 2 - 0.06, 0],
                [x2 - w2 / 2, cy - h2 / 2 + 0.06, 0],
                [x1 + w1 / 2, cy - h1 / 2 + 0.06, 0],
                stroke_width=0,
                fill_color="#E2E8F0",
                fill_opacity=0.45,
            )
            funnel_guides.add(trap)

        blocks = VGroup()
        arrows = VGroup()
        for i, (t_str, s_str, w, h, sc, fc, tc, subc, x) in enumerate(specs):
            blk = self._stage_block(t_str, s_str, w, h, sc, fc, tc, subc)
            blk.move_to([x, cy, 0])
            blocks.add(blk)
            if i < len(specs) - 1:
                next_x = specs[i + 1][8]
                next_w = specs[i + 1][2]
                arr = Arrow(
                    [x + w / 2 + 0.06, cy, 0],
                    [next_x - next_w / 2 - 0.06, cy, 0],
                    buff=0,
                    color="#475569",
                    stroke_width=2.0,
                    tip_length=0.14,
                    max_tip_length_to_length_ratio=0.25,
                )
                arrows.add(arr)

        # ── DONJI PANELI: Objašnjenje suštine ──
        bot_y = -1.24
        left_card = self._info_card(
            "ŠTA SE ODBACUJE (SUVIŠNI DETALJI)",
            "Tačna boja svakog piksela, pozadinski šum ili slučajne\n"
            "varijacije koje ne menjaju smisao onoga što je na ulazu.",
            -3.04,
            bot_y,
            "#64748B",
            {"ne menjaju smisao": BOLD},
        )

        right_card = self._info_card(
            "ŠTA OSTAJE (APSTRAKTNA SUŠTINA)",
            "Samo ključne osobine — npr. koji je pojam u pitanju,\n"
            "njegov oblik, stil, položaj ili glavna tema sadržaja.",
            3.04,
            bot_y,
            "#EA580C",
            {"ključne osobine": BOLD},
        )

        self.enc_parts = {
            "top_shell": VGroup(top_panel, top_heading, top_note),
            "first_block": blocks[0],
            "funnel_steps": VGroup(*[
                VGroup(funnel_guides[i], arrows[i], blocks[i + 1])
                for i in range(len(arrows))
            ]),
            "left_card": left_card,
            "right_card": right_card,
        }

        return VGroup(
            top_panel,
            top_heading,
            top_note,
            funnel_guides,
            blocks,
            arrows,
            left_card,
            right_card,
        )

    def animate_visual(self, visual):
        p = self.enc_parts
        self.play(
            self.reveal_mobj(p["top_shell"]),
            self.reveal_mobj(p["first_block"]),
            run_time=1.6,
        )
        self.wait(0.15)
        self.next_slide()

        self.play(
            LaggedStart(
                *[self.reveal_mobj(step) for step in p["funnel_steps"]],
                lag_ratio=0.25,
            ),
            run_time=2.3,
        )
        self.wait(0.15)
        self.next_slide()

        self.play(
            self.reveal_mobj(p["left_card"]),
            self.reveal_mobj(p["right_card"]),
            run_time=2.0,
        )
