import random

with open('./splashes.txt', 'r') as files:
    lines = files.readlines()

random.shuffle(lines)

with open('./splashes.txt', 'w') as files:
    files.writelines(lines)
