def main():
    num = 12
    Factor = [1]
    for i in range(2, num):
        if num % i == 0:
            Factor.append(i)
        ans = sum(Factor)
    print("The Sum of all the factors of ", num, "is", ans)


if__name__ = "__main__"
main()