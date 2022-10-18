import csv

name = input("Name: ").title()
home = input("Home: ").title()

with open("students_1.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
