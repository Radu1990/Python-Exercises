input_word = input('Insert word: ')
input_string = input('Insert string: ')


def uses_only(x, y):
    # x word
    # y string of letters
    for letter in y:
        if letter in x:
            pass
        else:
            print("...First check failed...please insert words again")
            return False
    print("...First check is ok...")

    for letter in x:
        if letter in y:
            pass
        else:
            print("...Second check failed...please insert words again")
            return False
    print("...Second check is ok...")

    print('Word contains only the letters from the string! :)')

uses_only(input_word, input_string)
