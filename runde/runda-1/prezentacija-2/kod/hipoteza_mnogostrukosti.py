"""3D manifold hypothesis visualization: 3D axes, 120 small sampled points, and a strongly curved 2D surface."""

from manim import *
import numpy as np
from manim_slides import ThreeDSlide


class HipotezaMnogostrukosti(ThreeDSlide):
    BG = "#F8F9FB"
    INK = "#1F293B"
    MUTED = "#64748B"
    BLUE = "#0284C7"
    ORANGE = "#F24B0B"
    RED = "#C91E1E"

    @staticmethod
    def manifold_z(x, y):
        # Dosta zakrivljen talasasti S-profil sa sedlastim uvijanjem po y osi
        return 1.25 * np.sin(1.25 * x + 0.55 * y) * np.cos(0.95 * y) + 0.28 * np.cos(1.8 * x)

    def construct(self):
        self.camera.background_color = ManimColor(self.BG)
        self.set_camera_orientation(phi=65 * DEGREES, theta=-42 * DEGREES)

        # ── FIKSNI ELEMENTI U KADRU (2D overlay) ──
        category = Text("ARHITEKTURA", font_size=13, weight=BOLD, color=self.RED)
        category.move_to([-5.1, 3.42, 0])

        title = Text(
            "Hipoteza mnogostrukosti (Manifold Hypothesis)",
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
            "1. Visokodimenzionalni prostor svih mogućih kombinacija (npr. svi pikseli)",
            font_size=19,
            color=self.MUTED,
        ).move_to([0, -2.85, 0])

        step2_caption = Text(
            "2. Stvarni, smisleni podaci ne ispunjavaju ceo prostor nasumično...",
            font_size=19,
            color=self.ORANGE,
        ).move_to([0, -2.85, 0])

        step3_caption = Text(
            "3. ...već leže na zakrivljenoj niže-dimenzionalnoj površi (mnogostrukosti)!",
            font_size=20,
            weight=BOLD,
            color=self.BLUE,
        ).move_to([0, -2.68, 0])

        step3_sub = Text(
            "Zato enkoder može da opiše podatke pomoću malog broja koordinata na toj površi.",
            font_size=16,
            color=self.INK,
        ).move_to([0, -3.10, 0])

        self.add_fixed_in_frame_mobjects(
            category,
            title,
            divider,
            footer_line,
            footer,
        )

        # ── 3D PROSTOR (zauzima centralni deo ekrana) ──
        axes = ThreeDAxes(
            x_range=[-3.2, 3.2, 1],
            y_range=[-2.6, 2.6, 1],
            z_range=[-1.9, 1.9, 1],
            x_length=8.6,
            y_length=6.4,
            z_length=3.3,
            axis_config={
                "color": "#64748B",
                "stroke_width": 1.8,
                "include_ticks": False,
            },
            tips=True,
        ).shift(UP * 0.22)

        # Oznake osa fiksirane prema kameri
        x_label = Text("x₁", font_size=16, color=self.MUTED).move_to(axes.c2p(3.45, 0, 0))
        y_label = Text("x₂", font_size=16, color=self.MUTED).move_to(axes.c2p(0, 2.85, 0))
        z_label = Text("x₃", font_size=16, color=self.MUTED).move_to(axes.c2p(0, 0, 2.12))
        axis_labels = VGroup(x_label, y_label, z_label)

        # ── 120 SITNIH TAČAKA POMOĆU np.linspace (12 × 10 mreža uz blagi deterministički pomak) ──
        xs = np.linspace(-2.65, 2.65, 12)
        ys = np.linspace(-2.05, 2.05, 10)
        points_group = VGroup()
        for idx_i, x_val in enumerate(xs):
            for idx_j, y_val in enumerate(ys):
                dx = 0.08 * np.sin(2.3 * idx_i + 1.7 * idx_j)
                dy = 0.08 * np.cos(1.9 * idx_i - 2.1 * idx_j)
                px = np.clip(x_val + dx, -2.78, 2.78)
                py = np.clip(y_val + dy, -2.18, 2.18)
                pz = self.manifold_z(px, py)
                pt_3d = Dot(
                    point=axes.c2p(px, py, pz),
                    radius=0.042,
                    color=self.ORANGE,
                )
                points_group.add(pt_3d)

        # ── ZAKRIVLJENA 2D MNOGOSTRUKOST (Surface fitovan kroz tačke) ──
        manifold_surface = Surface(
            lambda u, v: axes.c2p(u, v, self.manifold_z(u, v)),
            u_range=[-2.85, 2.85],
            v_range=[-2.25, 2.25],
            resolution=(26, 20),
            fill_color=self.BLUE,
            fill_opacity=0.36,
            stroke_color=self.BLUE,
            stroke_width=1.0,
            checkerboard_colors=[self.BLUE, "#38BDF8"],
        )

        # ── KORAK 1: Iscrtavanje 3D prostora ──
        self.add_fixed_orientation_mobjects(*axis_labels)
        self.add_fixed_in_frame_mobjects(step1_caption)
        self.play(
            Create(axes, run_time=1.8),
            Write(axis_labels, run_time=1.8),
            Write(step1_caption, run_time=1.8),
            run_time=1.8,
        )
        self.wait(0.15)
        self.next_slide()

        # ── KORAK 2: Iscrtavanje 120 sitnih tačaka u prostoru ──
        self.remove(step1_caption)
        self.add_fixed_in_frame_mobjects(step2_caption)
        self.add_fixed_orientation_mobjects(*points_group)
        self.play(
            Write(step2_caption, run_time=2.2),
            LaggedStart(
                *[Create(pt, run_time=1.0) for pt in points_group],
                lag_ratio=0.012,
                run_time=2.2,
            ),
            run_time=2.2,
        )
        self.wait(0.15)
        self.next_slide()

        # ── KORAK 3: Fitovanje zakrivljene mnogostrukosti (2D površi) na tačke + rotacija kamere ──
        self.remove(step2_caption)
        self.add_fixed_in_frame_mobjects(step3_caption, step3_sub)
        self.play(
            Write(step3_caption, run_time=2.2),
            Write(step3_sub, run_time=2.2),
            Create(manifold_surface, run_time=2.2),
            run_time=2.2,
        )
        self.wait(0.15)
        self.next_slide()

        self.begin_ambient_camera_rotation(rate=0.14, about="theta")
        self.next_slide(loop=True)
        self.wait(6)
        self.stop_ambient_camera_rotation(about="theta")
