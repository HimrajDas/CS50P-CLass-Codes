name = input("What's your name? ").title()

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor.")
    case "Draco":
        print("Slytherine.")
    case _:
        print("Who?")
