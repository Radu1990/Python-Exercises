# this code rotates a string a number of times

s = input('Enter String: ')
r = int(input('Enter number of rotations: '))


# (Guardian) this function proves if the letter is uppercase or lowercase if not returns false
def letter_is_up_or_low(a):
    if a.isupper():
        return a
    elif a.islower():
        return a
    else:
        print('Sorry word contains a non alphabetical symbol, please enter a letter from A-Z or a-Z')
        return False


# this function filters the string and if it contains only letters it outputs the string once again
def filter_string_function(a):
    filtered_string = ''
    for letter in a:
        x = letter_is_up_or_low(letter)
        filtered_string = filtered_string + x
    print(filtered_string)
    return filtered_string


def change_symbols_ntimes(a, b):
    new_word = ''
    for letter in a:
        num_code = ord(letter)
        changed_num_code = num_code - b
        back_to_character = chr(changed_num_code)
        new_word = new_word + back_to_character
    return new_word


newstring = filter_string_function(s)

print('Encrypted word is:',change_symbols_ntimes(newstring, r))
