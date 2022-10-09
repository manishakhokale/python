# Print list in reverse order using a loop.
list1 = [10, 20, 30, 40, 50]
# solution 1 - using reversed () function & for loop
# reverse list
new_list = reversed(list1)
# iterate item using for loop
for item in new_list:
    print(item)

print()

# solution 2 - using len() function & for loop .
# get the list size
# len(list1)-1 : because index start with 0
# iterate list in reverse order
# start form last to start
size = len(list1)-1
for i in range(size, -1, -1):
    print(list1[i])
print()

# Exercise 9: Display numbers from -10 to -1 using for loop

my_list = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
# solution 1
new_list = reversed(my_list)
for i in new_list:
    print(i)
print()
# solution 2
size = len(my_list)-1
for i in range(size, -1, -1):
    print(my_list[i])
print()
# solution 3
for num in range(-10, 0, 1):
    print(num)
print()

# Exercise 10: Use else block to display a message “Done” after successful execution of for loop.

for i in range(5):
    print(i)
else:
    print("Done!")

# Exercise 11: Write a program to display all prime numbers within a range
start = 25
end = 50
print("prime number between",start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

# Exercise 12: Display Fibonacci series up to 10 terms
num1 = 0
num2 = 1

print("Fibonacci sequence:")
# Run loop 10 times
for i in range(10):
    # print next number of series
    print(num1, end=" ")
    # add last two numbers to get next number
    res = num1 + num2

    # update values

    num1 = num2
    num2 = res







