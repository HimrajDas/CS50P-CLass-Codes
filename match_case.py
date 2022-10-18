name = input("What's your name? ").title()

match name:
    case "Harry":
        print("Gryffindoor.")
    case "Hermione":
        print("Gryffindoor.")
    case "Ron":
        print("Gryffindoor.")
    case "Draco":
        print("Slytherine.")
    case _:
        print("Who?")
        