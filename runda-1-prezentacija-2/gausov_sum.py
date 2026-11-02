from manim import *
import numpy as np

from .pojam_base import ConceptSlide


class GausovSum(ConceptSlide):
    TITLE = "Gausov šum: izvor kontrolisane slučajnosti"
    CATEGORY = "Unutrašnji oblik"
    BODY = (
        "Slučajni uzorak ε iz normalne raspodele unosi blagu varijaciju u sažeti zapis,\n"
        "čineći okolinu svake tačke u latentnom prostoru neprekidnom i otpornom."
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
        # ── LEVA STRANA: Izvlačenje slučajnih uzoraka ε ~ N(0, 1) ──
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
            "IZVLAČENJE SLUČAJNOG UZORKA ε ~ N(0, 1)",
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
            y_length=2.25,
            axis_config={
                "color": "#94A3B8",
                "stroke_width": 1.4,
                "include_ticks": False,
                "tip_width": 0.14,
                "tip_height": 0.14,
            },
            tips=True,
        ).move_to([lx + 0.05, ly - 0.14, 0])

        gauss = lambda x: 1.08 * np.exp(-0.5 * x**2)
        curve = axes.plot(gauss, x_range=[-3.1, 3.1], color="#64748B", stroke_width=3.2)
        area = axes.get_area(curve, x_range=[-3.1, 3.1], color="#E2E8F0", opacity=0.45)
        zero_lbl = Text("0", font_size=9.5, color="#64748B").move_to(axes.c2p(0, 0) + DOWN * 0.18)

        # Tri konkretna izvučena uzorka
        s1_x, s2_x, s3_x = -0.65, 0.22, 1.05
        samples = VGroup()
        for sx, col, lbl_str, offset_vec in [
            (s1_x, "#0284C7", "ε₁ = -0.65", np.array([-0.52, 0.24, 0])),
            (s2_x, "#0D9488", "ε₂ = +0.22", np.array([0.22, 0.28, 0])),
            (s3_x, "#EA580C", "ε₃ = +1.05", np.array([0.52, 0.22, 0])),
        ]:
            sy = gauss(sx)
            vline = DashedLine(axes.c2p(sx, 0), axes.c2p(sx, sy), color=col, stroke_width=1.8)
            dot_top = Dot(axes.c2p(sx, sy), radius=0.065, color=col)
            dot_base = Dot(axes.c2p(sx, 0), radius=0.055, color=col)
            badge = RoundedRectangle(
                width=1.08,
                height=0.26,
                corner_radius=0.05,
                stroke_color=col,
                stroke_width=1.1,
                fill_color="#FFFFFF",
                fill_opacity=1,
            ).move_to(axes.c2p(sx, sy) + offset_vec)
            txt = Text(lbl_str, font="DejaVu Sans Mono", font_size=9.5, weight=BOLD, color=col).move_to(
                badge.get_center()
            )
            samples.add(VGroup(vline, dot_base, dot_top, badge, txt))

        note_bottom = Text(
            "Mali pomaci oko nule su česti  ·  Veliki skokovi su retki",
            font_size=10,
            color="#475569",
        ).move_to([lx, panel.get_bottom()[1] + 0.22, 0])

        # ── DESNA STRANA: Tri objašnjavajuće kartice ──
        rx = 3.15
        card1 = self._info_card(
            "1. ŠTA JE GAUSOV ŠUM (ε)?",
            "To je slučajan broj izvučen iz standardne normalne raspodele\n"
            "N(0, 1) — prosečna vrednost mu je 0, a odstupanje 1.",
            rx,
            1.24,
            "#EA580C",
            {"slučajan broj": BOLD},
        )

        card2 = self._info_card(
            "2. ZAŠTO DODAJEMO SLUČAJNOST?",
            "Ako bi svaki ulaz bio samo jedna fiksna tačka, model ne bi znao\n"
            "šta se nalazi u prostoru oko nje. Šum širi tačku u „oblak“.",
            rx,
            -0.10,
            "#0284C7",
            {"širi tačku u „oblak“": BOLD},
        )

        card3 = self._info_card(
            "3. OSNOVA ZA STVARANJE NOVOG SADRŽAJA",
            "Zahvaljujući kontrolisanom šumu, model pri uzorkovanju uvek\n"
            "bira malo drugačiju tačku i stvara sveže varijacije istog pojma.",
            rx,
            -1.44,
            "#0D9488",
            {"sveže varijacije istog pojma": BOLD},
        )

        self.noise_parts = {
            "shell": VGroup(panel, heading, axes, zero_lbl),
            "curve": curve,
            "area": area,
            "card1": card1,
            "samples": samples,
            "note": note_bottom,
            "card2": card2,
            "card3": card3,
        }

        return VGroup(
            panel,
            heading,
            axes,
            area,
            curve,
            zero_lbl,
            samples,
            note_bottom,
            card1,
            card2,
            card3,
        )

    def animate_visual(self, visual):
        p = self.noise_parts
        self.play(
            self.reveal_mobj(p["shell"]),
            Create(p["curve"], run_time=2.6),
            self.reveal_mobj(p["card1"]),
            run_time=2.6,
        )
        self.play(FadeIn(p["area"], run_time=0.7), run_time=0.7)
        self.wait(0.15)
        self.next_slide()

        self.play(
            LaggedStart(
                *[self.reveal_mobj(s) for s in p["samples"]],
                lag_ratio=0.22,
            ),
            Write(p["note"], run_time=1.0),
            self.reveal_mobj(p["card2"]),
            run_time=2.2,
        )
        self.wait(0.15)
        self.next_slide()

        self.play(
            self.reveal_mobj(p["card3"]),
            run_time=1.8,
        )
