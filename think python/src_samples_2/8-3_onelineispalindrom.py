# this code shows how to use a string method for slicing words


def first(word):
    return word[0::]


def last(word):
    return word[::-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    print(first(word))
    print(last(word))

    if first(word) == last(word):
        print('True news!')
        return True

    else:
        print("Fake news!")
        return False


is_palindrome('doood')
