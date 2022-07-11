from datetime import datetime
from playsound import playsound  #to play sound
# import multiprocessing  #to stop playsound


#ask user when alarm will go off
alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")  #012345678910


def validate_time(alarm_time):
    if len(alarm_time) != 11:
        return 'Invalid format'
    else:
        if int(alarm_time[0:2]) > 12:
            return 'Invalid hour format! Please try again...'
        if int(alarm_time[3:5]) > 59:
            return 'Invalid minute format! Please try again...'
        if int(alarm_time[6:8]) > 59:
            return 'Invalid seconds format! Please try again...'
        else:
            return 'ok'


validate = validate_time(alarm_time.lower())
if validate != 'ok':
    print(validate)  #if input is not valid the user is prompted to enter the time again

else:
    print(f"Setting alarm for {alarm_time}...")   #execution heads to the next step

while True:
    # now we are sure input provided is valid
    alarm_hour = alarm_time[0:2]
    alarm_min = alarm_time[3:5]
    alarm_sec = alarm_time[6:8]
    alarm_period = alarm_time[9:].upper()


    # to get current time and compare it with user provided time
    now = datetime.now()

    current_hour = now.strftime('%H')
    current_min = now.strftime('%M')
    current_sec = now.strftime('%S')
    current_period = now.strftime('%p')

    if alarm_hour == current_hour:
        if alarm_min == current_min:
            if alarm_sec == current_sec:
                if alarm_period == current_period:
                    print('Wake Up!')
                    playsound('Alarm Clock_alarm.wav')
                    break
                    # p = multiprocessing.Process(target=playsound, args=("alarm.wav",))
                    # p.start()
                    # input('Press ENTER to stop playback')
                    # p.terminate()
                    # break


validate_time(alarm_time)

#HOW TO STOP THE ALARM WITH A COMMAND



# b = [1, 2, 3]
# print(b[0:2])