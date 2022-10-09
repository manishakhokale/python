def main():
    print("enter number: ")
    No = int(input())

    i = 1
    print("Factor are: ")
    while(i <= int(No/2)):
        if((No % i) == 0):
            print(i)
        i = i + 1


if__name__ = "__main__"
main()