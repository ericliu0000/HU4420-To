from manim import *
from sys import argv

BACKGROUND_COLOR = "#444444"
TEXT_OFF_COLOR = "#222222"
class Generate(Scene):
    def construct(self) -> None:
        self.camera.background_color = BACKGROUND_COLOR

        phrase, total_time, part = argv[-3:]
        color = BLUE if part == "i" else GREEN
        text = Text(phrase, font="IBM Plex Sans", color=TEXT_OFF_COLOR)

        in_time = 0.2 * total_time
        hold_time = 0.3 * total_time
        decay_time = 0.2 * total_time
        dim_time = 0.3 * total_time

        self.play(text.animate().set_color(color), run_time=in_time)
        self.wait(hold_time)
        self.play(text.animate().set_color(TEXT_OFF_COLOR), run_time=decay_time)
        self.wait(dim_time)
