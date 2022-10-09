# Exercise 1: Print First 10 natural numbers using while loop
i = 1

while i <= 10:
    print(i)
    i = i + 1


# Write a program to print the following number pattern using a loop.
print("Number Pattern ")

# Decide the row count. (above pattern contains 5 rows)
row = 5
# start : 1
# stop : row + 1 (range never include stop number in result)
# step : 1
# run loop 5 times
for i in range(1, row + 1, 1):
    # run inner loop i+1 times
    for j in range(1, i + 1):
        print(j, end=' ')
    # empty line after each row
    print("")



# Exercise 3: Calculate the sum of all numbers from 1 to a given number
# s: store sum of all numbers
    s = 0
n = int(input(" Enter the number "))
# run loop n times
# stop: n+1 ( range never include stop number in result)
for i in range(0, n+1, 1):
    # add current number to sum variable
    s += i
print("\n")
print("sum is: ", s)

print("------------")

# solution 2 :
n = int(input(" enter the number"))
x = sum(range(0, n+1, 1))
print("sum is: ", x)
print("------------")


# Exercise 4: Write a program to print multiplication table of a given number
n = 2
# stop : 11(because range never include stop number in result)
# run loop 10 times
for i in range(1, 11):
    # 2 * i (current number)
    p = n * i
    print(p)


