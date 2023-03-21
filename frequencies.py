import os

TIME_FACTOR = 80
with open("frequencies_work.csv") as n:
    table = [line.strip().split(",") for line in n.readlines()]

# pull phrase, frequency, and type from file
data = {}
for line in table:
    data[line[0]] = [float(line[1]), line[2]]

# transform frequencies into times
for k, v in data.items():
    data[k][0] = 1 / data[k][0] * TIME_FACTOR

print(data)

# run animations
for k, v in data.items():
    phrase = k
    time, part = data[k]

    os.system(f"manim -qm --format=gif animate.py -o \"{phrase}\" {time} {part}")


# for value in ["test1", "test2", "test3"]:
#     os.system(f"manim -qm --format=gif animate.py -o {value}")