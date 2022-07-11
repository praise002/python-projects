def calculate_bmi():
    while True:
        try:
            weight = float(input('Enter your weight in kg: '))
            height = float(input("Enter your height in cm: "))
            if weight < 1 or height < 1:
                print("Invalid input.")
                continue
            else:
                bmi = weight / (height / 100) ** 2
                return bmi

        except ValueError:   #work on rejecting negative value
            print('Invalid command.')
            continue


def bmi_index(bmi):

    if bmi <= 18.4:
        print('You are underweight.')
    elif bmi <= 24.9:
        print('You are healthy.')
    elif bmi <= 29.9:
        print('You are overweight.')
    elif bmi <= 34.9:
        print('You are severely overweight.')
    elif bmi <= 39.9:
        print('You are obese.')
    else:
        print('You are severely obese.')


bmi = calculate_bmi()
bmi_index(bmi)
