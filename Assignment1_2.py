def main():

    print("Enter the number")
    ChkNum = int(input())
    if (ChkNum % 2) == 0:
        print("Even Number".format(ChkNum))
    else:
        print("Odd Number".format(ChkNum))


if __name__ == "__main__":
    main()
