"""3D latent space visualization: scattered points, coloring by legend, and organic transparent clouds."""

from manim import *
import numpy as np
from manim_slides import ThreeDSlide


class LatentniProstor(ThreeDSlide):
    BG = "#F8F9FB"
    INK = "#1F293B"
    MUTED = "#64748B"
    ORANGE = "#F24B0B"
    BLUE = "#0284C7"
    TEAL = "#0D9488"
    PURPLE = "#7C3AED"

    def _make_legend_card(self):
        bg = RoundedRectangle(
            width=2.65,
            height=1.72,
            corner_radius=0.10,
            stroke_color="#CBD5E1",
            stroke_width=1.3,
            fill_color="#FFFFFF",
            fill_opacity=0.95,
        ).move_to([4.42, 1.15, 0])

        heading = Text("LEGENDA POJMOVA", font_size=11.5, weight=BOLD, color=self.INK)
        heading.move_to([bg.get_left()[0] + 0.22 + heading.width / 2, bg.get_top()[1] - 0.25, 0])

        items = [
            (self.BLUE, "Mačke (životinje)"),
            (self.ORANGE, "Psi (bliske životinje)"),
            (self.TEAL, "Automobili (vozila)"),
            (self.PURPLE, "Stabla (priroda)"),
        ]
        rows = VGroup()
        for idx, (col, lbl_text) in enumerate(items):
            ry = bg.get_top()[1] - 0.56 - idx * 0.30
            dot = Dot([bg.get_left()[0] + 0.28, ry, 0], radius=0.065, color=col)
            txt = Text(lbl_text, font_size=11, color="#334155")
            txt.move_to([bg.get_left()[0] + 0.46 + txt.width / 2, ry, 0])
            rows.add(VGroup(dot, txt))

        return VGroup(bg, heading, rows)

    def _make_irregular_cloud(self, axes, center, basis_matrix, radii, deform_phases, color):
        """Creates an organic, non-spherical transparent 3D cloud surface."""
        rx, ry, rz = radii
        p1, p2, p3 = deform_phases

        def param_func(u, v):
            # Osnovni elipsoid
            local = np.array([
                rx * np.sin(u) * np.cos(v),
                ry * np.sin(u) * np.sin(v),
                rz * np.cos(u),
            ])
            # Organska deformacija (da ne bude obična lopta/elipsoid)
            wobble = (
                1.0
                + 0.22 * np.sin(2 * u + p1) * np.cos(2 * v + p2)
                + 0.14 * np.cos(3 * u + p3)
            )
            rotated = basis_matrix @ (local * wobble)
            return axes.c2p(*(center + rotated))

        return Surface(
            param_func,
            u_range=[0, PI],
            v_range=[0, TAU],
            resolution=(14, 18),
            fill_color=color,
            fill_opacity=0.17,
            stroke_color=color,
            stroke_width=0.45,
            stroke_opacity=0.28,
            checkerboard_colors=[color, color],
        )

    def construct(self):
        self.camera.background_color = ManimColor(self.BG)
        self.set_camera_orientation(phi=64 * DEGREES, theta=-44 * DEGREES)

        # ── FIKSNI 2D ELEMENTI U KADRU ──
        category = Text("UNUTRAŠNJI OBLIK", font_size=13, weight=BOLD, color=self.ORANGE)
        category.move_to([-5.1, 3.42, 0])

        title = Text(
            "Latentni prostor: mapa skrivenih osobina",
            font="DejaVu Serif",
            font_size=37,
            color=self.INK,
        )
        if title.width > 11.8:
            title.scale(11.8 / title.width)
        title.move_to([0, 2.64, 0])

        divider = Line([-5.9, 2.17, 0], [5.9, 2.17, 0], color="#D7DFEA", stroke_width=1.3)
        footer_line = Line([-5.9, -3.45, 0], [5.9, -3.45, 0], color="#D7DFEA", stroke_width=1)
        footer = Text(
            "Dejan Lisica  ·  Reprezentacija sadržaja i latentni prostor",
            font_size=11,
            color=self.MUTED,
        ).move_to([0, -3.7, 0])

        step1_caption = Text(
            "1. Svaki ulaz nakon enkodera postaje tačka (vektor z) u 3D latentnom prostoru...",
            font_size=18.5,
            color=self.MUTED,
        ).move_to([0, -2.85, 0])

        step2_caption = Text(
            "2. Slični pojmovi prirodno zauzimaju bliske regione — bliskost u prostoru znači sličnost po smislu!",
            font_size=18,
            weight=BOLD,
            color=self.INK,
        ).move_to([0, -2.68, 0])

        step2_sub = Text(
            "Mačke i psi su blizu jedni drugima, dok su automobili i stabla u udaljenim oblastima prostora.",
            font_size=15.5,
            color=self.MUTED,
        ).move_to([0, -3.10, 0])

        legend_card = self._make_legend_card()
        legend_bg, legend_heading, legend_rows = legend_card
        legend_dots = VGroup(*[r[0] for r in legend_rows])
        legend_texts = VGroup(*[r[1] for r in legend_rows])

        self.add_fixed_in_frame_mobjects(
            category,
            title,
            divider,
            footer_line,
            footer,
        )

        # ── 3D KOORDINATNI SISTEM LATENTNOG PROSTORA ──
        axes = ThreeDAxes(
            x_range=[-3.4, 3.4, 1],
            y_range=[-2.8, 2.8, 1],
            z_range=[-2.0, 2.0, 1],
            x_length=8.8,
            y_length=6.6,
            z_length=3.5,
            axis_config={
                "color": "#64748B",
                "stroke_width": 1.8,
                "include_ticks": False,
            },
            tips=True,
        ).shift(UP * 0.20 + LEFT * 0.35)

        z1_lbl = Text("z₁", font_size=16, color=self.MUTED).move_to(axes.c2p(3.62, 0, 0))
        z2_lbl = Text("z₂", font_size=16, color=self.MUTED).move_to(axes.c2p(0, 3.02, 0))
        z3_lbl = Text("z₃", font_size=16, color=self.MUTED).move_to(axes.c2p(0, 0, 2.18))
        axis_labels = VGroup(z1_lbl, z2_lbl, z3_lbl)

        # ── GENERISANJE RAZBACANIH (IZDUŽENIH / ZAKRIVLJENIH) OBLAKA TAČAKA ──
        rng = np.random.default_rng(42)

        def rot_z(angle):
            c, s = np.cos(angle), np.sin(angle)
            return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])

        def rot_x(angle):
            c, s = np.cos(angle), np.sin(angle)
            return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])

        cluster_specs = [
            # (centar, rotacija, polu-ose (rx, ry, rz), faze deformacije, boja, broj tačaka)
            (
                np.array([-1.75, 1.15, 0.70]),
                rot_z(0.55) @ rot_x(0.30),
                (1.15, 0.48, 0.44),
                (0.4, 1.1, 0.8),
                self.BLUE,
                28,
            ),
            (
                np.array([-0.35, 1.65, 0.35]),
                rot_z(-0.45) @ rot_x(-0.25),
                (1.05, 0.46, 0.42),
                (1.5, 0.3, 2.1),
                self.ORANGE,
                28,
            ),
            (
                np.array([1.85, -1.15, -0.55]),
                rot_z(0.75) @ rot_x(-0.35),
                (1.25, 0.50, 0.45),
                (2.2, 1.7, 0.5),
                self.TEAL,
                28,
            ),
            (
                np.array([-1.35, -1.45, -0.45]),
                rot_z(-0.65) @ rot_x(0.40),
                (1.10, 0.52, 0.42),
                (0.9, 2.4, 1.3),
                self.PURPLE,
                26,
            ),
        ]

        all_dots = VGroup()
        dot_target_colors = []
        clouds = VGroup()

        for center, basis, radii, phases, col, n_pts in cluster_specs:
            # Nepravilni transparentni oblak
            cloud_surf = self._make_irregular_cloud(axes, center, basis, radii, phases, col)
            clouds.add(cloud_surf)

            # Razbacane tačke duž izduženog, blago zakrivljenog luka (ne čista lopta)
            t_vals = np.linspace(-0.88, 0.88, n_pts)
            for idx, t in enumerate(t_vals):
                jitter = rng.normal(0, 0.32, size=3)
                # Dodajemo zakrivljenost po y i z u zavisnosti od t, plus rasipanje
                local_pt = np.array([
                    radii[0] * t + jitter[0] * 0.25,
                    radii[1] * (0.45 * np.sin(2.4 * t) + jitter[1] * 0.65),
                    radii[2] * (0.35 * np.cos(2.1 * t) + jitter[2] * 0.65),
                ])
                world_pt = center + basis @ local_pt
                dot = Dot(
                    point=axes.c2p(*world_pt),
                    radius=0.044,
                    color="#64748B",  # U prvom koraku sve tačke su sive (neobojene)
                )
                all_dots.add(dot)
                dot_target_colors.append(col)

        # Izmešamo redosled pojavljivanja tačaka u prvom koraku da deluje prirodno
        perm = rng.permutation(len(all_dots))
        shuffled_dots = [all_dots[i] for i in perm]

        # ── KORAK 1: Iscrtavanje 3D prostora i svih tačaka (sivih) ──
        self.add_fixed_orientation_mobjects(*axis_labels)
        self.add_fixed_in_frame_mobjects(step1_caption)
        self.play(
            Create(axes, run_time=1.8),
            Write(axis_labels, run_time=1.8),
            Write(step1_caption, run_time=1.8),
            run_time=1.8,
        )
        self.add_fixed_orientation_mobjects(*all_dots)
        self.play(
            LaggedStart(
                *[Create(d, run_time=1.0) for d in shuffled_dots],
                lag_ratio=0.012,
                run_time=2.2,
            ),
            run_time=2.2,
        )
        self.wait(0.15)
        self.next_slide()

        # ── KORAK 2: Bojenje tačaka prema legendi + transparentni nepravilni oblaci ──
        self.remove(step1_caption)
        self.add_fixed_in_frame_mobjects(step2_caption, step2_sub, legend_card)
        self.play(
            Write(step2_caption, run_time=2.4),
            Write(step2_sub, run_time=2.4),
            Create(legend_bg, run_time=2.4),
            Create(legend_dots, run_time=2.4),
            Write(legend_heading, run_time=2.4),
            Write(legend_texts, run_time=2.4),
            *[
                dot.animate(run_time=2.4).set_color(target_col)
                for dot, target_col in zip(all_dots, dot_target_colors)
            ],
            Create(clouds, run_time=2.4),
            run_time=2.4,
        )
        self.wait(0.15)
        self.next_slide()

        # ── KORAK 3 (loop): Lagana rotacija kamere u 3D prostoru ──
        self.begin_ambient_camera_rotation(rate=0.14, about="theta")
        self.next_slide(loop=True)
        self.wait(6)
        self.stop_ambient_camera_rotation(about="theta")
