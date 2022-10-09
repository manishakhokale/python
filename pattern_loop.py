# Programs to print number pattern
rows = 5
# outer loop
for i in range(rows+1):
    # nested loop
    for j in range(i):
        # display number
        print(i,end=' ')
        # new line after each row
    print('')

print()
# Pyramid pattern of numbers
# In each row, every next number is incremented by 1.

rows = 5
for i in range(1, rows+1, 1):
    for j in range(1,i+1):
        print(j,end=' ')
    print(' ')

print()

# Inverted pyramid pattern of numbers

rows = 5
b = 0
# reverse for loop from 5 to 0
for i in range(rows, 0,-1):
    b += 1
    for j in range(1, i+1):
        print(b, end=' ')
    print('\r')

