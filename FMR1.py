
def checkeven(no):
    return(no % 2 == 0)


def increment(no):
    return no+2


def filterX(Arr,Function_Name):
    Result = []
    for no in Arr:
        if (Function_Name(no)):
            Result.append(no)
            return Result


def mapX(Arr,Function_Name):
    Result = []
    for no in Arr:
        Value = Function_Name(no)
        Result.append(Value)
        return Result


def reduceX(Arr):
    Sum = 0
    for no in Arr:
        Sum = Sum+no
        return Sum


def main():
    Data = [2, 3, 1, 6, 4, 5,11,16,20]

    Data_Filter = list(filterX(Data,checkeven))


if __name__ == '__main__':
    main()
