from manim import *
from sys import argv

BACKGROUND_COLOR = "#444444"
TEXT_OFF_COLOR = "#222222"
class Generate(Scene):
    def construct(self) -> None:
        self.camera.background_color = BACKGROUND_COLOR

        phrase, total_time, part = argv[-3:]
        color = BLUE if part == "i" else GREEN
        text = Text(phrase, font="IBM Plex Sans Medium", color=TEXT_OFF_COLOR, font_size=200)

        total_time = float(total_time)
        in_time = 0.2 * total_time ** 0.5
        hold_time = 0.3 * total_time
        decay_time = 0.2 * total_time ** 0.5
        dim_time = total_time - in_time - hold_time - decay_time

        self.play(text.animate().set_color(color), run_time=in_time)
        self.wait(hold_time)
        self.play(text.animate().set_color(TEXT_OFF_COLOR), run_time=decay_time)
        self.wait(dim_time)
