"""It takes in the height and weight of the
individual and will calculate the BMI(Body Mass Index) of the person
It measures the body fat based on height and weight"""

cm_inch = input('cm or ft and inches(enter as fi): ').lower()
# weight = float(input('Enter your weight in kg: '))


def calculate_bmi():
    while True:
        try:
            if cm_inch == 'cm':
                height = float(input('Height in cm: '))
                weight = float(input('Enter your weight in kg: '))
                bmi = weight / (height / 100) ** 2
                return bmi

            elif cm_inch == 'fi':
                ft = float(input('ft: '))
                inch = float(input('Inches: '))
                weight = float(input('Enter your weight in kg: '))
                inches = (ft * 12) + inch
                height = inches * 2.54   # in cm
                # print(height)

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

# bmi = float(input('Enter bmi: '))
# if bmi <= 18.4:
#     print('You are underweight.')
# elif bmi <= 24.9:
#     print('You are healthy.')
# elif bmi <= 29.9:
#     print('You are overweight.')
# elif bmi <= 34.9:
#     print('You are severely overweight.')
# elif bmi <= 39.9:
#     print('You are obese.')
# else:
#     print('You are severely obese.')   #bmi cant be zero bcus its the system doing the calculation









