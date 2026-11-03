from manim import *

from .pojam_base import ConceptSlide


class LatentnaPromenljiva(ConceptSlide):
    TITLE = "Latentna promenljiva: konkretan uzorak u prostoru"
    CATEGORY = "Unutrašnji oblik"
    BODY = (
        "Latentna promenljiva z spaja izračunatu suštinu ulaza (μ, σ) i slučajni šum (ε)\n"
        "u jedan konačan vektor skrivenih osobina koji ulazi u dekoder."
    )
    ACCENT = ConceptSlide.ORANGE
    KEEP_VISUAL_POSITION = True

    def _term_chip(self, sym_str, desc_str, width, stroke_c, fill_c, sym_c, desc_c):
        rect = RoundedRectangle(
            width=width,
            height=0.88,
            corner_radius=0.10,
            stroke_color=stroke_c,
            stroke_width=1.8,
            fill_color=fill_c,
            fill_opacity=1,
        )
        s_mob = Text(sym_str, font_size=22, weight=BOLD, color=sym_c)
        d_mob = Text(desc_str, font_size=10.5, color=desc_c)
        s_mob.move_to(rect.get_center() + UP * 0.14)
        d_mob.move_to(rect.get_center() + DOWN * 0.21)
        return VGroup(rect, s_mob, d_mob)

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
            font_size=11.5,
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
        # ── GORNJI PANEL: Formula z = μ + σ · ε i tok od Enkodera do Dekodera ──
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
            "1. KAKO NASTAJE UZORAK z (TRIK REPARAMETRIZACIJE)",
            font_size=13,
            weight=BOLD,
            color=self.ORANGE,
        )
        top_heading.move_to([
            top_panel.get_left()[0] + 0.35 + top_heading.width / 2,
            top_panel.get_top()[1] - 0.30,
            0,
        ])

        top_note = Text(
            "Od parametara iz enkodera  ·  Do ulaza za dekoder",
            font_size=11.5,
            color=self.MUTED,
        )
        top_note.move_to([
            top_panel.get_right()[0] - 0.35 - top_note.width / 2,
            top_panel.get_top()[1] - 0.30,
            0,
        ])

        cy = 0.52

        # Levi blok: Enkoder daje parametre
        enc_box = RoundedRectangle(
            width=1.65,
            height=0.88,
            corner_radius=0.08,
            stroke_color="#64748B",
            stroke_width=1.5,
            fill_color="#F1F5F9",
            fill_opacity=1,
        ).move_to([-4.75, cy, 0])
        enc_t1 = Text("Enkoder", font_size=13, weight=BOLD, color="#1E293B").move_to([-4.75, cy + 0.14, 0])
        enc_t2 = Text("daje μ i σ", font_size=10.5, color="#475569").move_to([-4.75, cy - 0.18, 0])
        enc_group = VGroup(enc_box, enc_t1, enc_t2)

        arr_in = Arrow([-3.88, cy, 0], [-3.40, cy, 0], buff=0, color="#64748B", stroke_width=2.0, tip_length=0.12)

        # Članovi formule: μ  +  σ  ·  ε  =  z
        mu_chip = self._term_chip("μ", "centar (prosek)", 1.55, "#0284C7", "#E0F2FE", "#0369A1", "#0284C7")
        mu_chip.move_to([-2.55, cy, 0])

        plus_op = Text("+", font_size=24, weight=BOLD, color="#475569").move_to([-1.52, cy, 0])

        sigma_chip = self._term_chip("σ", "širina (rasipanje)", 1.65, "#EA580C", "#FFEDD5", "#9A3412", "#C2410C")
        sigma_chip.move_to([-0.44, cy, 0])

        dot_op = Text("·", font_size=28, weight=BOLD, color="#475569").move_to([0.58, cy, 0])

        eps_chip = self._term_chip("ε", "Gausov šum", 1.45, "#64748B", "#F1F5F9", "#334155", "#64748B")
        eps_chip.move_to([1.50, cy, 0])

        eq_op = Text("=", font_size=24, weight=BOLD, color="#475569").move_to([2.45, cy, 0])

        z_chip = self._term_chip("z", "latentni vektor", 1.55, "#0D9488", "#CCFBF1", "#0F766E", "#0D9488")
        z_chip.move_to([3.45, cy, 0])

        arr_out = Arrow([4.28, cy, 0], [4.68, cy, 0], buff=0, color="#0D9488", stroke_width=2.0, tip_length=0.12)

        dec_box = RoundedRectangle(
            width=1.08,
            height=0.88,
            corner_radius=0.08,
            stroke_color="#0D9488",
            stroke_width=1.5,
            fill_color="#F0FDFA",
            fill_opacity=1,
        ).move_to([5.24, cy, 0])
        dec_t1 = Text("Dekoder", font_size=12, weight=BOLD, color="#0F766E").move_to([5.24, cy + 0.12, 0])
        dec_t2 = Text("gradi izlaz", font_size=9.5, color="#0D9488").move_to([5.24, cy - 0.16, 0])
        dec_group = VGroup(dec_box, dec_t1, dec_t2)

        # ── DONJI PANELI: Objašnjenje z i trika reparametrizacije ──
        bot_y = -1.24
        left_card = self._info_card(
            "ŠTA PREDSTAVLJA VEKTOR z?",
            "Za razliku od celog prostora Z, malo slovo z označava jedan\n"
            "konkretan niz brojeva (npr. [0.42, -1.10, ...]) za dati ulaz.",
            -3.04,
            bot_y,
            "#0D9488",
            {"jedan konkretan niz brojeva": BOLD},
        )

        right_card = self._info_card(
            "ZAŠTO ZAJEDNO μ, σ I ε?",
            "Zato što direktno slučajno izvlačenje prekida tok učenja mreže.\n"
            "Ovom formulom šum ε dolazi spolja, pa model nesmetano uči μ i σ.",
            3.04,
            bot_y,
            "#EA580C",
            {"nesmetano uči μ i σ": BOLD},
        )

        self.z_parts = {
            "top_shell": VGroup(top_panel, top_heading, top_note),
            "enc_params": VGroup(enc_group, arr_in, mu_chip, plus_op, sigma_chip),
            "noise_and_z": VGroup(dot_op, eps_chip, eq_op, z_chip, arr_out, dec_group),
            "left_card": left_card,
            "right_card": right_card,
        }

        return VGroup(
            top_panel,
            top_heading,
            top_note,
            enc_group,
            arr_in,
            mu_chip,
            plus_op,
            sigma_chip,
            dot_op,
            eps_chip,
            eq_op,
            z_chip,
            arr_out,
            dec_group,
            left_card,
            right_card,
        )

    def animate_visual(self, visual):
        p = self.z_parts
        self.play(
            self.reveal_mobj(p["top_shell"]),
            self.reveal_mobj(p["enc_params"]),
            run_time=1.9,
        )
        self.wait(0.15)
        self.next_slide()

        self.play(
            self.reveal_mobj(p["noise_and_z"]),
            run_time=1.9,
        )
        self.wait(0.15)
        self.next_slide()

        self.play(
            self.reveal_mobj(p["left_card"]),
            self.reveal_mobj(p["right_card"]),
            run_time=2.0,
        )
