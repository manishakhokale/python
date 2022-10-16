def main():
    print("Enter the number:")    # input 5187934
    no1 = int(input())
    Count = 0
    while no1 > 0:
        no1 = no1 // 10
        Count = Count + 1

    print("Number of Digits in a Given Number = %d" % Count)


if__name__ = "__main__"
main()
