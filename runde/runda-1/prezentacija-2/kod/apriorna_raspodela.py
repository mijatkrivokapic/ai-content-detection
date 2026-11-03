from manim import *
import numpy as np

from .pojam_base import ConceptSlide


class ApriornaRaspodela(ConceptSlide):
    TITLE = "Apriorna raspodela: uređeni raspored pre ulaza"
    CATEGORY = "Unutrašnji oblik"
    BODY = (
        "Apriorna raspodela P(z) zadaje unapred očekivani oblik latentnog prostora,\n"
        "tako da sažeti zapisi budu gusto i uredno složeni oko centra bez praznina."
    )
    ACCENT = ConceptSlide.ORANGE
    KEEP_VISUAL_POSITION = True

    def _info_card(self, title_str, body_str, x_pos, y_pos, accent_color, bold_map=None):
        bg = RoundedRectangle(
            width=5.45,
            height=1.18,
            corner_radius=0.10,
            stroke_color="#CBD5E1",
            stroke_width=1.3,
            fill_color="#FFFFFF",
            fill_opacity=1,
        ).move_to([x_pos, y_pos, 0])

        title = Text(title_str, font_size=12.5, weight=BOLD, color=accent_color)
        title.move_to([
            bg.get_left()[0] + 0.28 + title.width / 2,
            bg.get_top()[1] - 0.26,
            0,
        ])

        body = Text(
            body_str,
            font_size=11,
            color="#334155",
            line_spacing=0.82,
            t2w=bold_map or {},
            t2c={k: self.INK for k in (bold_map or {})},
        )
        body.move_to([
            bg.get_left()[0] + 0.28 + body.width / 2,
            y_pos - 0.14,
            0,
        ])
        return VGroup(bg, title, body)

    def build_visual(self):
        # ── LEVA STRANA: Zvonasta kriva P(z) = N(0, 1) ──
        lx = -2.90
        ly = -0.10
        lw = 5.80
        lh = 3.85

        panel = RoundedRectangle(
            width=lw,
            height=lh,
            corner_radius=0.12,
            stroke_color="#CBD5E1",
            stroke_width=1.3,
            fill_color="#FFFFFF",
            fill_opacity=1,
        ).move_to([lx, ly, 0])

        heading = Text(
            "OČEKIVANA GUSTINA VEROVATNOĆE P(z)",
            font_size=12.5,
            weight=BOLD,
            color=self.ORANGE,
        )
        heading.move_to([
            panel.get_left()[0] + 0.28 + heading.width / 2,
            panel.get_top()[1] - 0.28,
            0,
        ])

        axes = Axes(
            x_range=[-3.4, 3.4, 1],
            y_range=[0, 1.35, 0.5],
            x_length=4.90,
            y_length=2.40,
            axis_config={
                "color": "#94A3B8",
                "stroke_width": 1.4,
                "include_ticks": False,
                "tip_width": 0.14,
                "tip_height": 0.14,
            },
            tips=True,
        ).move_to([lx + 0.05, ly - 0.22, 0])

        gauss = lambda x: 1.08 * np.exp(-0.5 * x**2)
        curve = axes.plot(gauss, x_range=[-3.1, 3.1], color=self.ORANGE, stroke_width=3.6)
        area = axes.get_area(curve, x_range=[-3.1, 3.1], color="#FED7AA", opacity=0.45)

        center_line = DashedLine(
            axes.c2p(0, 0),
            axes.c2p(0, 1.08),
            color="#C2410C",
            stroke_width=1.6,
        )
        zero_lbl = Text("0 (centar)", font_size=10, weight=BOLD, color="#9A3412").move_to(
            axes.c2p(0, 0) + DOWN * 0.24
        )
        minus_lbl = Text("-2", font_size=9.5, color="#64748B").move_to(axes.c2p(-2, 0) + DOWN * 0.22)
        plus_lbl = Text("+2", font_size=9.5, color="#64748B").move_to(axes.c2p(2, 0) + DOWN * 0.22)

        pz_badge = RoundedRectangle(
            width=2.15,
            height=0.32,
            corner_radius=0.05,
            stroke_color="#EA580C",
            stroke_width=1.2,
            fill_color="#FFEDD5",
            fill_opacity=1,
        ).move_to(axes.c2p(1.65, 1.02))
        pz_lbl = Text("P(z) = N(0, 1)", font_size=11, weight=BOLD, color="#9A3412").move_to(
            pz_badge.get_center()
        )

        # Gusto raspoređene tačke oko nule, retke na repovima
        sample_xs = [-2.1, -1.25, -0.75, -0.38, -0.12, 0.14, 0.40, 0.78, 1.30, 2.15]
        sample_dots = VGroup(*[
            Dot(axes.c2p(x, 0.08), radius=0.055, color="#0284C7" if abs(x) < 1.0 else "#94A3B8")
            for x in sample_xs
        ])
        dense_lbl = Text("najgušća oblast", font_size=9.5, weight=BOLD, color="#0284C7")
        dense_lbl.move_to(axes.c2p(0, 0.32))

        # ── DESNA STRANA: Tri objašnjavajuće kartice ──
        rx = 3.15
        card1 = self._info_card(
            "1. ŠTA ZNAČI „APRIORNA“ (PRE ULAZA)?",
            "Pre nego što modelu pokažemo bilo kakvu sliku ili tekst, zadajemo\n"
            "pravilo gde bi sažeti zapisi trebalo da se nalaze u prostoru.",
            rx,
            1.24,
            "#EA580C",
            {"zadajemo pravilo": BOLD},
        )

        card2 = self._info_card(
            "2. STANDARDNO ZVONO OKO NULE N(0, 1)",
            "Najčešće biramo Gausovo zvono sa centrom u nuli: većina tačaka\n"
            "pada blizu sredine, dok su ekstremne vrednosti na krajevima retke.",
            rx,
            -0.10,
            "#0284C7",
            {"blizu sredine": BOLD},
        )

        card3 = self._info_card(
            "3. SPREČAVA „RUPE“ U PROSTORU",
            "Bez ovog pravila enkoder bi razbacao tačke daleko jedne od drugih,\n"
            "pa bi prostor između njih bio prazan i neupotrebljiv za generisanje.",
            rx,
            -1.44,
            "#0D9488",
            {"prazan i neupotrebljiv": BOLD},
        )

        self.prior_parts = {
            "shell": VGroup(panel, heading, axes, zero_lbl, minus_lbl, plus_lbl),
            "card1": card1,
            "curve": curve,
            "area": area,
            "center_line": center_line,
            "pz_badge_group": VGroup(pz_badge, pz_lbl),
            "card2": card2,
            "samples": VGroup(sample_dots, dense_lbl),
            "card3": card3,
        }

        return VGroup(
            panel,
            heading,
            axes,
            area,
            curve,
            center_line,
            zero_lbl,
            minus_lbl,
            plus_lbl,
            pz_badge,
            pz_lbl,
            sample_dots,
            dense_lbl,
            card1,
            card2,
            card3,
        )

    def animate_visual(self, visual):
        p = self.prior_parts
        self.play(
            self.reveal_mobj(p["shell"]),
            self.reveal_mobj(p["card1"]),
            run_time=1.8,
        )
        self.wait(0.15)
        self.next_slide()

        self.play(
            Create(p["curve"], run_time=3.2),
            self.reveal_mobj(p["card2"]),
            run_time=3.2,
        )
        self.play(
            FadeIn(p["area"], run_time=0.9),
            Create(p["center_line"], run_time=1.1),
            self.reveal_mobj(p["pz_badge_group"]),
            run_time=1.2,
        )
        self.wait(0.15)
        self.next_slide()

        self.play(
            self.reveal_mobj(p["samples"]),
            self.reveal_mobj(p["card3"]),
            run_time=2.0,
        )
