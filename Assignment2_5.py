def main():
    num = 5
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                print("It is not prime number")
                break
        else:
            print("It is prime number")
    else:
        print("It is not prime number")


if__name__ = "__main__"
main()