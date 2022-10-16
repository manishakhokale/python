def CheckEven(No):
    if(No % 2 == 0):
        return True
    else:
        return False


def checkEvenX(No):
    return(No % 2 == 0)


    Ret = CheckEvenX(12)


    if(Ret == True):
        print("it's even")
    else:
        print("it's odd")