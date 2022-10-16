# positional Arguments
def Add(No1,No2):
    print("Value of No1:",No1)
    print("Value of No2:", No2)
    return No1+No2


def Sub1(No1,No2):
    print("Value of No1:",No1)
    print("Value of No2:", No2)
    return No1-No2


def main():
    Ans = 0                 # Ans = Add(10,11) we can consider
    Ans = Add(10,11)
    print("Addition is",Ans)
    Ans = Add(No1 = 10, No2 = 11)
    print("Substration is :",Ans)
    Ans = Add(No1=10, No2=11)
    print("Addition is :", Ans)


if __name__ == '__main__':
    main()