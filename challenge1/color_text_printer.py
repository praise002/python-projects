import colorama
from colorama import Back, Fore

#back: used to change d background colour of the text
#fore: to change the colour of the text itself

colorama.init(autoreset=True)  #reset the color values to default once the execution is over

text = input('Enter a phrase or sentence: ')
print(Fore.RED + text)
print(Back.LIGHTCYAN_EX + text)
print(Fore.BLACK + Back.WHITE + text)

