from manim import *

with open("frequencies_work.csv") as n:
    table = [line.strip().split(",") for line in n.readlines()]

# pull phrase, frequency, and type from file
data = {}
for line in table:
    data[line[0]] = [float(line[1]), line[2]]

# transform frequencies into times
for k, v in data.items():
    data[k][0] = 1 / data[k][0]

class Generate(Scene):
    def construct(self) -> None:
        text = Text("Testing")

        self.play(FadeIn(text), run_time=0.2)
        self.play(FadeOut(text), run_time=0.4)
        self.wait(0.4)