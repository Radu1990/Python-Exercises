a = input('Insert word here: ')


def display_letters_backwards(word):
    index = len(word)-1
    while index > -1:
        letter = word[index]
        print(letter)
        index = index-1


display_letters_backwards(a)
