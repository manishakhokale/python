# Exercise 5: Display numbers from a list using loop
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]
# iterate each item of a list
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    # check if number is divisible by 5
    elif item % 5 == 0:
        print(item)


# Exercise 6: Count the total number of digits in a number using a while loop.
# For example, the number is 75869, so the output should be 5.

num = 75869
count = 0
while num !=0:
    # floor division
    # reduce last digit from number
    num = num // 10
    # increment counter by 1
    count = count + 1
print("Total Digits are: ", count)

# Write a program to use for loop to print the following reverse number pattern
