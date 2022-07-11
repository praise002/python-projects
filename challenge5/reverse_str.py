"""Using recursive"""


def reverse_str(str1):
    if len(str1) == 1:  #stopping condition
        return str1
    else:
        return reverse_str(str1[1:]) + str1[0]


str1 = input("Enter the string: ")
str2 = reverse_str(str1)
print("Reversed string is", str2)


"""part 2, using iterative"""
#str = food
#r_s = f + "", i= f and it goes on like that


def reverse(string):
    reversed_string = ""
    for i in string:
        reversed_string = i + reversed_string
    print("Reversed string is", reversed_string)


string = input("Enter a string: ")
print("Entered string:", string)
reverse(string)
