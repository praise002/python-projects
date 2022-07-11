word = "civic"
backward = word[::-1].isalnum()
forward = word[::1].isalnum()
print(backward == forward)


"""Part 2"""


def is_palidrome(string):
    reversed_string = string[::-1]
    status = True
    while status:
        if string == reversed_string:
            return status
        else:
            status = False
            return status


str = input("Enter a word or a sentence: ")
print(is_palidrome(str))
