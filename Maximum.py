

def maximum(no1, no2):
    if no1 > no2:
        return no1
    else:
        return no2


def main():

    print("Enter first number")
    value1 = input()

    print("Enter second number")
    value2 = input()

    ans = maximum(int(value1), int(value2))

    print("Largest number is :", ans)


if __name__ == "__main__":
    main()
