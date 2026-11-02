from manim import *

from .pojam_base import ConceptSlide


class Tokenizacija(ConceptSlide):
    TITLE = "Tokenizacija: zašto delovi reči, a ne cele reči?"
    CATEGORY = "Spoljašnji oblik"
    BODY = "Podreči čuvaju korene i afikse, ali morfološki bogatiji jezici traže više tokena."
    ACCENT = ConceptSlide.BLUE
    KEEP_VISUAL_POSITION = True

    def _morpheme_chip(self, token_str, sub_str, width, stroke_color, fill_color, text_color, sub_color):
        rect = RoundedRectangle(
            width=width,
            height=0.80,
            corner_radius=0.08,
            stroke_color=stroke_color,
            stroke_width=1.6,
            fill_color=fill_color,
            fill_opacity=1,
        )
        main_txt = Text(token_str, font_size=18, weight=BOLD, color=text_color)
        sub_txt = Text(sub_str, font_size=11, color=sub_color)
        main_txt.move_to(rect.get_center() + UP * 0.14)
        sub_txt.move_to(rect.get_center() + DOWN * 0.19)
        return VGroup(rect, main_txt, sub_txt)

    def _flat_pill(self, label, width, fill_color, text_color="#1E293B"):
        rect = RoundedRectangle(
            width=width,
            height=0.44,
            corner_radius=0.06,
            stroke_width=0,
            fill_color=fill_color,
            fill_opacity=1,
        )
        txt = Text(label, font_size=15, weight=BOLD, color=text_color)
        if txt.width > width - 0.16:
            txt.scale((width - 0.16) / txt.width)
        txt.move_to(rect.get_center())
        return VGroup(rect, txt)

    def build_visual(self):
        # ── 1. GORNJI PANEL: Razlaganje na morfeme i podreči ──
        top_panel = RoundedRectangle(
            width=11.8,
            height=1.95,
            corner_radius=0.12,
            stroke_color="#CBD5E1",
            stroke_width=1.3,
            fill_color="#FFFFFF",
            fill_opacity=1,
        ).move_to([0, 0.82, 0])

        top_heading = Text(
            "1. RAZLAGANJE NA MORFEME I PODREČI",
            font_size=14,
            weight=BOLD,
            color="#0284C7",
        )
        top_heading.move_to([
            top_panel.get_left()[0] + 0.35 + top_heading.width / 2,
            top_panel.get_top()[1] - 0.32,
            0,
        ])

        top_note = Text(
            'Donja crta „_“ označava razmak pre tokena',
            font_size=12,
            color=self.MUTED,
        )
        top_note.move_to([
            top_panel.get_right()[0] - 0.35 - top_note.width / 2,
            top_panel.get_top()[1] - 0.32,
            0,
        ])

        row_y = 0.54
        sent_rect = RoundedRectangle(
            width=3.65,
            height=0.76,
            corner_radius=0.08,
            stroke_color="#94A3B8",
            stroke_width=1.4,
            fill_color="#F1F5F9",
            fill_opacity=1,
        ).move_to([-3.72, row_y, 0])
        sent_txt = Text(
            '"Neprimetnost žiga je važna."',
            font_size=16,
            weight=BOLD,
            color=self.INK,
        ).move_to(sent_rect.get_center())
        source_box = VGroup(sent_rect, sent_txt)

        split_arrow = Arrow(
            [-1.84, row_y, 0],
            [-1.24, row_y, 0],
            buff=0.04,
            color="#0284C7",
            stroke_width=2.2,
            tip_length=0.15,
            max_tip_length_to_length_ratio=0.25,
        )

        chip_specs = [
            ("Ne", "prefiks", 0.68, "#0284C7", "#E0F2FE", "#0369A1", "#0284C7"),
            ("prim", "koren", 0.72, "#0284C7", "#E0F2FE", "#0369A1", "#0284C7"),
            ("et", "sufiks", 0.64, "#0284C7", "#E0F2FE", "#0369A1", "#0284C7"),
            ("nost", "čest sufiks", 0.94, "#EAB308", "#FEF08A", "#854D0E", "#A16207"),
            ("_žiga", "cela reč", 0.78, "#94A3B8", "#F1F5F9", "#334155", "#64748B"),
            ("_je", "česta reč", 0.84, "#94A3B8", "#F1F5F9", "#334155", "#64748B"),
            ("_važna", "cela reč", 0.98, "#94A3B8", "#F1F5F9", "#334155", "#64748B"),
            (".", "znak", 0.54, "#94A3B8", "#F1F5F9", "#334155", "#64748B"),
        ]
        chips = VGroup()
        curr_x = -1.16
        gap = 0.088
        for tok, sub, w, sc, fc, tc, subc in chip_specs:
            chip = self._morpheme_chip(tok, sub, w, sc, fc, tc, subc)
            chip.move_to([curr_x + w / 2, row_y, 0])
            chips.add(chip)
            curr_x += w + gap

        # ── 2. DONJI LEVI PANEL: Engleski jezik ──
        bot_y = -1.18
        left_panel = RoundedRectangle(
            width=5.72,
            height=1.38,
            corner_radius=0.12,
            stroke_color="#CBD5E1",
            stroke_width=1.3,
            fill_color="#FFFFFF",
            fill_opacity=1,
        ).move_to([-3.04, bot_y, 0])

        en_heading = Text(
            "ENGLESKI JEZIK (3 tokena)",
            font_size=13,
            weight=BOLD,
            color="#0D9488",
        )
        en_heading.move_to([
            left_panel.get_left()[0] + 0.32 + en_heading.width / 2,
            left_panel.get_top()[1] - 0.30,
            0,
        ])

        en_specs = [
            ('"Invisibility"', 1.48),
            ('"_matters"', 1.32),
            ('"."', 0.56),
        ]
        en_pills = VGroup()
        en_x = left_panel.get_left()[0] + 0.32
        for label, w in en_specs:
            pill = self._flat_pill(label, w, "#CCFBF1", "#0F172A")
            pill.move_to([en_x + w / 2, bot_y - 0.16, 0])
            en_pills.add(pill)
            en_x += w + 0.12

        # ── 3. DONJI DESNI PANEL: Srpski jezik ──
        right_panel = RoundedRectangle(
            width=5.72,
            height=1.38,
            corner_radius=0.12,
            stroke_color="#CBD5E1",
            stroke_width=1.3,
            fill_color="#FFFFFF",
            fill_opacity=1,
        ).move_to([3.04, bot_y, 0])

        sr_heading = Text(
            "SRPSKI JEZIK (6 tokena za isti smisao!)",
            font_size=13,
            weight=BOLD,
            color="#E11D48",
        )
        sr_heading.move_to([
            right_panel.get_left()[0] + 0.32 + sr_heading.width / 2,
            right_panel.get_top()[1] - 0.30,
            0,
        ])

        sr_specs = [
            ('"Ne"', 0.68),
            ('"prim"', 0.82),
            ('"et"', 0.64),
            ('"nost"', 0.82),
            ('"_znači"', 0.94),
            ('"."', 0.50),
        ]
        sr_pills = VGroup()
        sr_x = right_panel.get_left()[0] + 0.32
        for label, w in sr_specs:
            pill = self._flat_pill(label, w, "#FFE4E6", "#0F172A")
            pill.move_to([sr_x + w / 2, bot_y - 0.16, 0])
            sr_pills.add(pill)
            sr_x += w + 0.10

        self.tok_parts = {
            "top_panel": VGroup(top_panel, top_heading, top_note),
            "source": source_box,
            "arrow": split_arrow,
            "chips": chips,
            "left_panel": VGroup(left_panel, en_heading),
            "en_pills": en_pills,
            "right_panel": VGroup(right_panel, sr_heading),
            "sr_pills": sr_pills,
        }
        return VGroup(
            top_panel, top_heading, top_note,
            source_box, split_arrow, chips,
            left_panel, en_heading, en_pills,
            right_panel, sr_heading, sr_pills,
        )

    def animate_visual(self, visual):
        p = self.tok_parts
        self.play(
            self.reveal_mobj(p["top_panel"]),
            self.reveal_mobj(p["source"]),
            run_time=1.6,
        )
        self.wait(0.15)
        self.next_slide()

        self.play(
            GrowArrow(p["arrow"], run_time=1.0),
            LaggedStart(
                *[self.reveal_mobj(chip) for chip in p["chips"]],
                lag_ratio=0.12,
            ),
            run_time=2.2,
        )
        self.wait(0.15)
        self.next_slide()

        self.play(
            self.reveal_mobj(p["left_panel"]),
            LaggedStart(
                *[self.reveal_mobj(pill) for pill in p["en_pills"]],
                lag_ratio=0.12,
            ),
            self.reveal_mobj(p["right_panel"]),
            LaggedStart(
                *[self.reveal_mobj(pill) for pill in p["sr_pills"]],
                lag_ratio=0.10,
            ),
            run_time=2.2,
        )
