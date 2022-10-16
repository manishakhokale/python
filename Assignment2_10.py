def main():
    print("Enter the number:")    # input 5187934
    no1 = int(input())
    Sum = 0
    while no1 > 0:
        rem = no1 % 10
        Sum = Sum+rem
        no1 = int(no1/10)

    print("sum of Digits in a Given Number:", Sum)


if__name__ = "__main__"
main()
