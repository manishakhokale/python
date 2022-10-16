print("Demonstration of set")

# data = Heterogeneous
# ordered = No
# indexed = No
# mutable = yes
# duplicates = No

data = {11, 21, 51, 101, 21, 11}
data1 = {11, 90.80, True, "Hello"}

print("first set data:", data)
print("length of data:", len(data))
print("data is Heterogeneous :", data1)
print("data is ordered:", data1)
# print("data is index 2:", data1[2])
print("data with unique elements:", data)

print("set is mutable")

# insert element in set
data.add(211)
print("data after insertion:", data)
# remove element from set
data.remove(211)
print("data after removal:", data)

data.remove(201)
print("data after removal:", data)

data.discard(201)
print("data after discard:", data)