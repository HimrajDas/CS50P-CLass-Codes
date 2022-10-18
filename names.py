names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())


rank = 1
for name in sorted(names):
    print(f"{rank} {name}")
    rank += 1
