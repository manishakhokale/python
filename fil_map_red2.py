# by using Normal function
def start_with_a(s):
    return s[0] == "A"


fruits = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = list(map(start_with_a,fruits))
print("Map Object by using normal function :",map_object)


# by using lambda function

map_object = list(map(lambda s:s[0] == "A", fruits))
print("Map Object by using lambda function :", map_object)