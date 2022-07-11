import random

board = [" " for _ in range(9)]
print(board)
# board.count()
print(board.count(" "))
for row in [board[i*3:(i+1)*3] for i in range(3)]:
    # print(row)
    print("| " + "| ".join(row) + "| ")

# for _ in range(5):
#     print(_, end=" ")
# print()
# for i in range(5):
#     print(i, end=" ")
# print()
# for i in range(5, -1, -1):  #to reverse string
#     print(i, end=" ")
# print()
# list1 = [10, 20, 30, 40, 50]  #to reverse list
# print(list1[::-1])
# print(list1[::-2])
# for i in reversed(range(7)):
#     print(i, end=" ")
# print()
# million = 1_000_000
# binary = 0b_0010
# hexa = 0x_23_ab
# octa = 0o_64
# print(million)
# print(binary)
# print(hexa)
# print(octa)
print(random.randint(1, 9))