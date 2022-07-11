import time

print('You might be feeling sick or just want to stay healthy. \nLets help you calculate your temperature.')
print('Loading...')
time.sleep(1)
temp = input("Enter 'f' for fahrenheit and 'c' for celsius: ").lower()
if temp == 'f':
    fahrenheit = float(input('Enter your temperature in Fahrenheit: '))
    celsius = (fahrenheit - 32) * 5/9
    print('Converting to ℃...')    #ctrl+. to open emoji
    time.sleep(1)
    print(f"{temp.upper()} in {fahrenheit} is equal to {celsius} in celsius.")
if temp == 'c':
    celsius = float(input('Enter your temperature in celsius: '))
    fahrenheit = (celsius * 1.8) + 32
    print('Converting to ℉...')
    time.sleep(1)
    print(f"{temp.upper()} in {celsius} is equal to {fahrenheit} in fahrenheit.")
