# from manim import *

# pull phrase, frequency, and type from file
with open("frequencies_work.csv") as n:
    table = [line.strip().split(",") for line in n.readlines()]

    data = {}
    for line in table:
        data[line[0]] = [line[1], line[2]]

# 