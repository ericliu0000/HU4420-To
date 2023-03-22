from manim import *
from sys import argv

BACKGROUND_COLOR = "#444444"
TEXT_OFF_COLOR = "#222222"
TIME_FACTOR = 80

with open("src/frequencies_work.csv") as n:
    table = [line.strip().split(",") for line in n.readlines()]

# pull phrase, frequency, and type from file
data = {}
for line in table:
    data[line[0]] = [float(line[1]), line[2]]

# transform frequencies into times
for k, v in data.items():
    data[k][0] = 1 / data[k][0] * TIME_FACTOR


class Generate(Scene):
    def construct(self) -> None:
        self.camera.background_color = BACKGROUND_COLOR

        count = 0
        for k, v in data.items():
            phrase = k
            total_time, part = v
            self.next_section(phrase)

            color = BLUE if part == "i" else GREEN
            text = MarkupText(phrase, font="IBM Plex Sans Medium", color=TEXT_OFF_COLOR, font_size=200)

            print(count, phrase, text.get_top()[1], text.get_bottom()[1])

            count += 1
            y = 0
            if ("i" in phrase):
                y += 0.1140625
            elif ("b" in phrase) or ("h" in phrase) or ("l" in phrase) or ("k" in phrase):
                y += 0.10820312

            if ("y" in phrase) or ("p" in phrase):
                y -= 0.2609375
            elif ("g" in phrase):
                y -= 0.277734375

            text.move_to((0, y, 0))

            total_time = float(total_time)
            in_time = 0.2 * total_time ** 0.5
            hold_time = 0.3 * total_time
            decay_time = 0.2 * total_time ** 0.5
            dim_time = total_time - in_time - hold_time - decay_time

            self.play(text.animate().set_color(color), run_time=in_time)
            self.wait(hold_time)
            self.play(text.animate().set_color(TEXT_OFF_COLOR), run_time=decay_time)
            self.wait(dim_time)

            self.remove(text)

