from json import loads
import os

data = {}

with open("Generate.json") as n:
    data = loads(n.read())

for x in data:
    name, file = x["name"], x["video"]
    os.system(f"mv {file} '{name}.mp4'")
    