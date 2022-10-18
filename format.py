import re

name = input("What's your name? ").strip()
matches = re.fullmatch(r"(.+), ?(.+)", name)
if matches:
    name = matches.group(1) + " " + matches.group(2)
print(f"Hello, {name}")
