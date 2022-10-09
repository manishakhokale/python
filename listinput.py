def main():
    arr = list()

    print("Enter how many elements you want to store?")
    size = int(input())

    print("Please Enter the values")

    for i in range(0, size, 1):
        no = int(input())

        arr.append(no)  # arr.insert(i,no)

    print(arr)


if __name__ == "__main__":
    main()
