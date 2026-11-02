from manim import *

from .pojam_base import ConceptSlide


class Rekonstrukcija(ConceptSlide):
    TITLE = "Rekonstrukcija: provera očuvane suštine"
    CATEGORY = "Arhitektura"
    BODY = (
        "Poređenjem ulaza i izlaza merimo koliko je suštine sačuvano u sažetom zapisu\n"
        "— to je signal pomoću kog model uči šta je važno, a šta nebitno."
    )
    ACCENT = "#C91E1E"
    KEEP_VISUAL_POSITION = True

    def _media_box(self, label_str, sub_str, x_pos, y_pos, stroke_c, fill_c, text_c, sub_c, clean=False):
        card = RoundedRectangle(
            width=2.35,
            height=1.28,
            corner_radius=0.10,
            stroke_color=stroke_c,
            stroke_width=1.8,
            fill_color=fill_c,
            fill_opacity=1,
        ).move_to([x_pos, y_pos, 0])

        # Mala ilustracija planine i sunca levo u kartici
        art_x = x_pos - 0.72
        art_y = y_pos + 0.08
        frame = RoundedRectangle(
            width=0.68,
            height=0.56,
            corner_radius=0.05,
            stroke_color=stroke_c,
            stroke_width=1.3,
            fill_color="#FFFFFF",
            fill_opacity=1,
        ).move_to([art_x, art_y, 0])
        sun = Circle(radius=0.07, stroke_width=0, fill_color="#F59E0B", fill_opacity=1).move_to(
            [art_x + 0.16, art_y + 0.12, 0]
        )
        mtn = Polygon(
            [art_x - 0.27, art_y - 0.21, 0],
            [art_x - 0.05, art_y + 0.09, 0],
            [art_x + 0.07, art_y - 0.05, 0],
            [art_x + 0.20, art_y + 0.05, 0],
            [art_x + 0.27, art_y - 0.21, 0],
            stroke_width=0,
            fill_color="#60A5FA" if not clean else "#34D399",
            fill_opacity=1,
        )
        art = VGroup(frame, sun, mtn)
        if not clean:
            # Sitne tačkice koje predstavljaju pozadinski šum na originalnom ulazu
            specks = VGroup(
                Dot([art_x - 0.18, art_y + 0.16, 0], radius=0.018, color="#94A3B8"),
                Dot([art_x - 0.02, art_y + 0.19, 0], radius=0.016, color="#94A3B8"),
                Dot([art_x + 0.21, art_y - 0.04, 0], radius=0.018, color="#94A3B8"),
            )
            art.add(specks)

        t_mob = Text(label_str, font_size=12.5, weight=BOLD, color=text_c)
        s_mob = Text(sub_str, font_size=10, color=sub_c)
        t_mob.move_to([x_pos + 0.38, y_pos + 0.16, 0])
        s_mob.move_to([x_pos + 0.38, y_pos - 0.14, 0])

        return VGroup(card, art, t_mob, s_mob)

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
        # ── GORNJI PANEL: Ceo krug (Ulaz → Enkoder → Sažeti zapis → Dekoder → Rekonstrukcija) ──
        top_panel = RoundedRectangle(
            width=11.8,
            height=2.25,
            corner_radius=0.12,
            stroke_color="#CBD5E1",
            stroke_width=1.3,
            fill_color="#FFFFFF",
            fill_opacity=1,
        ).move_to([0, 0.72, 0])

        top_heading = Text(
            "1. CEO TOK KROZ USKO GRLO I PROVERA TAČNOSTI",
            font_size=13,
            weight=BOLD,
            color="#C91E1E",
        )
        top_heading.move_to([
            top_panel.get_left()[0] + 0.35 + top_heading.width / 2,
            top_panel.get_top()[1] - 0.30,
            0,
        ])

        top_note = Text(
            "Cilj: sačuvati smisao uprkos suženju",
            font_size=11.5,
            color=self.MUTED,
        )
        top_note.move_to([
            top_panel.get_right()[0] - 0.35 - top_note.width / 2,
            top_panel.get_top()[1] - 0.30,
            0,
        ])

        cy = 0.62
        orig_box = self._media_box(
            "Polazni ulaz", "svi detalji + šum", -4.40, cy, "#0284C7", "#E0F2FE", "#0369A1", "#0284C7", clean=False
        )

        # Srednji mini-levak (Enkoder -> Sažeti zapis -> Dekoder)
        enc_trap = Polygon(
            [-2.45, cy + 0.54, 0],
            [-1.05, cy + 0.30, 0],
            [-1.05, cy - 0.30, 0],
            [-2.45, cy - 0.54, 0],
            stroke_color="#64748B",
            stroke_width=1.5,
            fill_color="#F1F5F9",
            fill_opacity=1,
        )
        enc_txt = Text("Enkoder", font_size=12, weight=BOLD, color="#334155").move_to([-1.75, cy, 0])

        core_rect = RoundedRectangle(
            width=1.50,
            height=0.66,
            corner_radius=0.08,
            stroke_color="#EA580C",
            stroke_width=1.8,
            fill_color="#FFEDD5",
            fill_opacity=1,
        ).move_to([0, cy, 0])
        core_t1 = Text("Sažeti zapis", font_size=11.5, weight=BOLD, color="#9A3412").move_to([0, cy + 0.11, 0])
        core_t2 = Text("usko grlo", font_size=9.5, color="#C2410C").move_to([0, cy - 0.13, 0])
        core_box = VGroup(core_rect, core_t1, core_t2)

        dec_trap = Polygon(
            [1.05, cy + 0.30, 0],
            [2.45, cy + 0.54, 0],
            [2.45, cy - 0.54, 0],
            [1.05, cy - 0.30, 0],
            stroke_color="#64748B",
            stroke_width=1.5,
            fill_color="#F1F5F9",
            fill_opacity=1,
        )
        dec_txt = Text("Dekoder", font_size=12, weight=BOLD, color="#334155").move_to([1.75, cy, 0])

        recon_box = self._media_box(
            "Rekonstrukcija", "očuvana suština", 4.40, cy, "#0D9488", "#CCFBF1", "#0F766E", "#0D9488", clean=True
        )

        # Kratke strelice između segmenata
        arr1 = Arrow([-3.18, cy, 0], [-2.50, cy, 0], buff=0, color="#475569", stroke_width=2.0, tip_length=0.12)
        arr2 = Arrow([-1.02, cy, 0], [-0.77, cy, 0], buff=0, color="#475569", stroke_width=2.0, tip_length=0.10)
        arr3 = Arrow([0.77, cy, 0], [1.02, cy, 0], buff=0, color="#475569", stroke_width=2.0, tip_length=0.10)
        arr4 = Arrow([2.50, cy, 0], [3.18, cy, 0], buff=0, color="#475569", stroke_width=2.0, tip_length=0.12)

        # Donja povratna sprega poređenja (Polazni ulaz <-> Rekonstrukcija)
        cmp_y = -0.18
        cmp_left = DashedLine([-4.40, cy - 0.66, 0], [-4.40, cmp_y, 0], color="#E11D48", stroke_width=1.6)
        cmp_right = DashedLine([4.40, cy - 0.66, 0], [4.40, cmp_y, 0], color="#E11D48", stroke_width=1.6)
        cmp_horiz = DashedLine([-4.40, cmp_y, 0], [4.40, cmp_y, 0], color="#E11D48", stroke_width=1.6)

        badge_bg = RoundedRectangle(
            width=4.35,
            height=0.34,
            corner_radius=0.06,
            stroke_color="#F43F5E",
            stroke_width=1.2,
            fill_color="#FFE4E6",
            fill_opacity=1,
        ).move_to([0, cmp_y, 0])
        badge_txt = Text(
            "Poređenje: koliko se izlaz razlikuje od ulaza?",
            font_size=11,
            weight=BOLD,
            color="#BE123C",
        ).move_to(badge_bg.get_center())
        comparison_group = VGroup(cmp_left, cmp_right, cmp_horiz, badge_bg, badge_txt)

        # ── DONJI PANELI: Zašto idemo u krug? ──
        bot_y = -1.24
        left_card = self._info_card(
            "ZAŠTO UOPŠTE REKONSTRUIŠEMO ULAZ?",
            "Zato što model nema nikoga da mu ručno označi šta je suština.\n"
            "Kvalitet sažetka proverava tako što iz njega pokuša da vrati ulaz.",
            -3.04,
            bot_y,
            "#C91E1E",
            {"proverava tako što iz njega pokuša da vrati ulaz": BOLD},
        )

        right_card = self._info_card(
            "EFEKAT „USKOG GRLA“ (SAMO BITNO PROLAZI)",
            "Pošto u sažeti zapis ne može da stane sve, model je primoran\n"
            "da upamti opšta pravila i oblike, a zanemari slučajan šum.",
            3.04,
            bot_y,
            "#0D9488",
            {"upamti opšta pravila i oblike": BOLD},
        )

        self.rec_parts = {
            "top_shell": VGroup(top_panel, top_heading, top_note),
            "orig": orig_box,
            "pipeline": VGroup(arr1, enc_trap, enc_txt, arr2, core_box, arr3, dec_trap, dec_txt, arr4, recon_box),
            "comparison": comparison_group,
            "left_card": left_card,
            "right_card": right_card,
        }

        return VGroup(
            top_panel,
            top_heading,
            top_note,
            orig_box,
            arr1,
            enc_trap,
            enc_txt,
            arr2,
            core_box,
            arr3,
            dec_trap,
            dec_txt,
            arr4,
            recon_box,
            comparison_group,
            left_card,
            right_card,
        )

    def animate_visual(self, visual):
        p = self.rec_parts
        self.play(
            self.reveal_mobj(p["top_shell"]),
            self.reveal_mobj(p["orig"]),
            run_time=1.6,
        )
        self.wait(0.15)
        self.next_slide()

        self.play(
            LaggedStart(
                *[self.reveal_mobj(mob) for mob in p["pipeline"]],
                lag_ratio=0.12,
            ),
            run_time=2.5,
        )
        self.wait(0.15)
        self.next_slide()

        self.play(
            self.reveal_mobj(p["comparison"]),
            self.reveal_mobj(p["left_card"]),
            self.reveal_mobj(p["right_card"]),
            run_time=2.2,
        )
