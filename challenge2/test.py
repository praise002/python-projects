word = "boom"
guess = input('Guess: ')
word_completion = "_" * len(word)
word_as_list = list(word_completion)
print(word_as_list)
indices = [i for i, letter in enumerate(word) if letter == guess]
print(indices)
for index in indices:
    print(index)
    word_as_list[index] = guess
    word_completion = "".join(word_as_list)
    print(word_completion)



def find_all(word, guess):
    indices = [i for i, letter in enumerate(word) if letter == guess]
    #index_number, letter n tuple(0, b) if letter is in guess
    for index in indices:
        word_as_list[index] = guess
    word_completion = "".join(word_as_list)
    return word_completion



# print(find_all(word, guess))