# normal function or named functions
def Add(No1,No2):
    return No1+No2

# Lambda function / unnamed function
# Lambda parameters : body


AddFunction= lambda A,B:A+B

Ans1 = Add(10,11)
Ans2 = AddFunction(10,11)

print("Addition using normal function:", Ans1)
print("Addition using normal function:", Ans2)

print("Type of Lambda function is:",type(AddFunction))