print("Enter 'q' to quit.")
user_input = input('Enter a phrase: ')
phrase = user_input.replace('of', '').split()  #to ignore of from the input if any
#.split() fn to breakdown the string into individual words and store them as a list in phrase variable
acronym = ''  #to store the acronym

for word in phrase:   #itr phrase variable
    acronym += word[0].upper()  #index 0 of each phrase
print(f"Acronym of {user_input} is {acronym}")




