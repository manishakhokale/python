print("Application to demonstrate industrial programming")


import Marvellousmodules


def main():
    print("Value of __name__ from main is: ", __name__)
    print("Enter First number: ")
    no1 = int(input())
    print("Enter Second number: ")
    no2 = int(input())

    Sum = Marvellousmodules.Addition(no1, no2)
    Sub = no1-no2
    mult = no1 * no2
    div = no1/no2

    print("Addition is:", Sum)
    print("subtraction is:", Sub)
    print("multiplication is:", mult)
    print("division is:", div)


if __name__ == "__main__":
    main()