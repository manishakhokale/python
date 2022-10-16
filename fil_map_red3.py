# by using Normal function
def cube(num):
    return num ** 3


num = [2, 3, 6, 9, 10]

cubed = list(map(cube, num))
print("Cube of numbers is :",cubed)

# by using lambda function

cubed = list(map(lambda n : n ** 3, num))
print("Cube of numbers is :", cubed)