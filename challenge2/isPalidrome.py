"""
The word is the same forwards and backwards
return a boolean value
should only consider letters A-Z
ignore their case
"""
import string


# def is_palidrome(string):
#     reversed_string = string[::-1]
#     status = True  #a flag
#     while status:
#         if string.lower() == reversed_string.lower():
#             return status
#         else:
#             status = False
#             return status
#
# # string.ascii_letters
# print(is_palidrome('love'))
# string.isalpha()  #returns true if all ch is alphabet



"""Part 2"""

import re


def is_palidrome(phrase):
     forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))  #finds all occurences of a given pattern
     backwards = forwards[::-1]
     return forwards == backwards


phrase = input('Enter a word: ')
print(is_palidrome(phrase))
