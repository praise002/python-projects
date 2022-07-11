"""Understanding rows and columns"""
l = [
    [1, 2, 3],
    [4, 5, 6]
]

print(len(l))  #ans is 2
print(len(l[0]))  #ans is 3
print(len(l[1]))
#so:
l_row = len(l)
l_col = len(l[0])

#write in loops
for row_index in range(l_row):
    for column_index in range(l_col):
        print(l[row_index][column_index], end=" ")
    print()
