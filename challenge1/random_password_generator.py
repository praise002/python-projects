import random
import string

user_input = int(input('Enter the length of the password: '))
pass_data = string.ascii_letters + string.digits
password = "".join(random.choices(pass_data, k=user_input))
if user_input > 10:
    raise Exception('Password cannot be greater than 10.')
else:
    print(password)
# print(password)