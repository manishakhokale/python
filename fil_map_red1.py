# by using Normal function
def myfunc(a):
    return a*a


a = [1, 2, 3]
square = list(map(myfunc, a))
print("square is:", square)

# by using Lambda function
a = [1, 2, 3]
square = list(map(lambda a:a*a,a))
print("square is :",square)

# filter by using lambda function
b = list(filter(lambda x : x>2, a))
print(b)

# reduce by using lambda
from functools import reduce

c = reduce(lambda x,y:x+y,a)
print(c)
