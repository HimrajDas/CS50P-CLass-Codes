def main():
    height = int(input("Height: "))
    pyramid(height)


def pyramid(n):
    for i in range(n):
        for j in range(n):
            print("#", end="")
        print()


main()
