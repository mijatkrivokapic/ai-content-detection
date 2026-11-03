from manim import *

from .pojam_base import ConceptSlide


class Token(ConceptSlide):
    TITLE = "Token i struktura rečnika modela"
    CATEGORY = "Spoljašnji oblik"
    BODY = "Sam redni broj (npr. ID 4821) je samo indeks u tabeli — on nema nikakvo matematičko značenje\ndok ne pređe u Ugrađivanje."
    ACCENT = ConceptSlide.BLUE
    KEEP_VISUAL_POSITION = True

    def _token_badge(self, text_str, fill_color, text_color):
        txt = Text(text_str, font="DejaVu Sans Mono", font_size=14, weight=BOLD, color=text_color)
        pad_x = 0.28
        rect = RoundedRectangle(
            width=txt.width + pad_x,
            height=0.36,
            corner_radius=0.06,
            stroke_width=0,
            fill_color=fill_color,
            fill_opacity=1,
        )
        txt.move_to(rect.get_center())
        return VGroup(rect, txt)

    def build_visual(self):
        # ── LEVA STRANA: Tabela rečnika ──
        tx = -2.90
        ty = 0.05
        tw = 5.80
        th = 3.30
        row_h = th / 6.0  # 0.55 po redu (1 zaglavlje + 5 redova)

        table_top = ty + th / 2
        table_left = tx - tw / 2
        table_right = tx + tw / 2

        col_id_x = table_left + 0.25
        col_sym_x = tx - 0.35
        col_kind_x = table_right - 0.25

        # Pozadina cele tabele
        table_bg = RoundedRectangle(
            width=tw,
            height=th,
            corner_radius=0.10,
            stroke_width=0,
            fill_color="#FFFFFF",
            fill_opacity=1,
        ).move_to([tx, ty, 0])

        # Zaglavlje (tamno)
        header_y = table_top - row_h / 2
        header_bg_round = RoundedRectangle(
            width=tw,
            height=row_h,
            corner_radius=0.10,
            stroke_width=0,
            fill_color="#0F172A",
            fill_opacity=1,
        ).move_to([tx, header_y, 0])
        header_bg_flat = Rectangle(
            width=tw,
            height=row_h / 2,
            stroke_width=0,
            fill_color="#0F172A",
            fill_opacity=1,
        ).move_to([tx, header_y - row_h / 4, 0])
        header_bg = VGroup(header_bg_round, header_bg_flat)

        h_id = Text("ID u rečniku", font_size=12, weight=BOLD, color="#FFFFFF")
        h_id.move_to([col_id_x + h_id.width / 2, header_y, 0])
        h_sym = Text("Simbol (Token)", font_size=12, weight=BOLD, color="#FFFFFF")
        h_sym.move_to([col_sym_x, header_y, 0])
        h_kind = Text("Vrsta jedinice", font_size=12, weight=BOLD, color="#FFFFFF")
        h_kind.move_to([col_kind_x - h_kind.width / 2, header_y, 0])
        header_group = VGroup(header_bg, h_id, h_sym, h_kind)

        rows_data = [
            ("13", '"."', "#F1F5F9", "#334155", "Interpunkcija", False),
            ("412", '"_je"', "#DBEAFE", "#1E3A8A", "Cela česta reč", False),
            ("4821", '"mačka"', "#FEE2E2", "#991B1B", "Imenica (ulaz za embedding)", True),
            ("8921", '"nost"', "#FEF08A", "#854D0E", "Čest deo reči (sufiks)", False),
            ("99840", '"ž"', "#F3E8FF", "#581C87", "Pojedinačno slovo (rezerva)", False),
        ]

        row_groups = VGroup()
        dividers = VGroup()

        for i, (id_str, sym_str, badge_bg, badge_fg, kind_str, is_hl) in enumerate(rows_data):
            ry = table_top - row_h * (i + 1.5)
            row_items = VGroup()

            if is_hl:
                hl_rect = Rectangle(
                    width=tw - 0.04,
                    height=row_h,
                    stroke_width=0,
                    fill_color="#FFF1F2",
                    fill_opacity=1,
                ).move_to([tx, ry, 0])
                row_items.add(hl_rect)

            id_txt = Text(id_str, font="DejaVu Sans Mono", font_size=14, weight=BOLD, color="#B91C1C")
            id_txt.move_to([col_id_x + id_txt.width / 2, ry, 0])

            badge = self._token_badge(sym_str, badge_bg, badge_fg)
            badge.move_to([col_sym_x, ry, 0])

            kind_color = "#B91C1C" if is_hl else "#64748B"
            kind_weight = BOLD if is_hl else NORMAL
            kind_txt = Text(kind_str, font_size=12, weight=kind_weight, color=kind_color)
            kind_txt.move_to([col_kind_x - kind_txt.width / 2, ry, 0])

            row_items.add(id_txt, badge, kind_txt)
            row_groups.add(row_items)

            if i < len(rows_data) - 1:
                line_y = table_top - row_h * (i + 2)
                div_line = Line(
                    [table_left + 0.02, line_y, 0],
                    [table_right - 0.02, line_y, 0],
                    color="#E2E8F0",
                    stroke_width=1.0,
                )
                dividers.add(div_line)

        table_outline = RoundedRectangle(
            width=tw,
            height=th,
            corner_radius=0.10,
            stroke_color="#1E293B",
            stroke_width=1.5,
            fill_opacity=0,
        ).move_to([tx, ty, 0])

        # ── DESNA STRANA: Dve info kartice ──
        rx = 3.15
        rw = 5.45
        rh = 1.52

        # Kartica 1: Konačan rečnik V
        cy1 = 0.89
        card1_bg = RoundedRectangle(
            width=rw,
            height=rh,
            corner_radius=0.12,
            stroke_color="#CBD5E1",
            stroke_width=1.3,
            fill_color="#FFFFFF",
            fill_opacity=1,
        ).move_to([rx, cy1, 0])

        c1_title = Text(
            "Konačan rečnik V (oko 100.000 simbola)",
            font_size=16,
            weight=BOLD,
            color="#0284C7",
        )
        c1_title.move_to([
            card1_bg.get_left()[0] + 0.30 + c1_title.width / 2,
            card1_bg.get_top()[1] - 0.34,
            0,
        ])

        c1_body = Text(
            "Kombinovanjem celih reči, podreči i pojedinačnih slova,\n"
            "model može da predstavi bilo koju reč bez greške\n"
            "„nepoznat token“.",
            font_size=12.5,
            color="#334155",
            line_spacing=0.85,
            t2w={"bilo koju reč": BOLD},
            t2c={"bilo koju reč": self.INK},
        )
        c1_body.move_to([
            card1_bg.get_left()[0] + 0.30 + c1_body.width / 2,
            cy1 - 0.16,
            0,
        ])
        card1 = VGroup(card1_bg, c1_title, c1_body)

        # Kartica 2: Tokeni nisu vezani samo za tekst!
        cy2 = -0.79
        card2_bg = RoundedRectangle(
            width=rw,
            height=rh,
            corner_radius=0.12,
            stroke_color="#CBD5E1",
            stroke_width=1.3,
            fill_color="#FFFFFF",
            fill_opacity=1,
        ).move_to([rx, cy2, 0])

        c2_title = Text(
            "Tokeni nisu vezani samo za tekst!",
            font_size=16,
            weight=BOLD,
            color="#EA580C",
        )
        c2_title.move_to([
            card2_bg.get_left()[0] + 0.30 + c2_title.width / 2,
            card2_bg.get_top()[1] - 0.34,
            0,
        ])

        c2_body = Text(
            "Slike (kvantizovani blokovi 16×16 piksela) i zvuk takođe se\n"
            "mogu pretvoriti u nizove diskretnih tokena iz konačnog\n"
            "rečnika.",
            font_size=12.5,
            color="#334155",
            line_spacing=0.85,
        )
        c2_body.move_to([
            card2_bg.get_left()[0] + 0.30 + c2_body.width / 2,
            cy2 - 0.16,
            0,
        ])
        card2 = VGroup(card2_bg, c2_title, c2_body)

        self.token_parts = {
            "table_shell": VGroup(table_bg, header_group, dividers, table_outline),
            "rows": row_groups,
            "card1": card1,
            "card2": card2,
        }

        return VGroup(
            table_bg,
            row_groups,
            dividers,
            header_group,
            table_outline,
            card1,
            card2,
        )

    def animate_visual(self, visual):
        p = self.token_parts
        self.play(
            self.reveal_mobj(p["table_shell"]),
            LaggedStart(
                *[self.reveal_mobj(row) for row in p["rows"]],
                lag_ratio=0.15,
            ),
            run_time=2.2,
        )
        self.wait(0.15)
        self.next_slide()

        self.play(
            self.reveal_mobj(p["card1"]),
            run_time=1.8,
        )
        self.wait(0.15)
        self.next_slide()

        self.play(
            self.reveal_mobj(p["card2"]),
            run_time=1.8,
        )
