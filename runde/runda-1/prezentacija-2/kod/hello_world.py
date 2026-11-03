from manim import *
from manim_slides import Slide


class HelloWorldPresentation(Slide):
    def construct(self):
        title = Text("Hello, World!", font_size=72, weight=BOLD)
        subtitle = Text("Made with Manim Slides", font_size=32, color=BLUE_C)
        subtitle.next_to(title, DOWN, buff=0.45)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.next_slide()

        self.play(FadeOut(subtitle), title.animate.scale(0.75).to_edge(UP))
        message = Text("Your first presentation is ready.", font_size=40)
        message.next_to(title, DOWN, buff=0.8)
        self.play(Write(message))
        self.next_slide()

        self.play(FadeOut(title), FadeOut(message))


