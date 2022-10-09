def main():
    print("enter number: ")
    No = int(input())

    print("Factor are: ")
    for i in range(1,int(No/2)+1,1):
        if No % i ==0:
            print(i)


if__name__ = "__main__"
main()