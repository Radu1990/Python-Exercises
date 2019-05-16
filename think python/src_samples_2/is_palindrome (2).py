def first(word):
    print(word[0])
    return word[0]


def last(word):
    print(word[-1])
    return word[-1]


def middle(word):
    print(word[1:-1])
    return word[1:-1]


def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif first(word) != last(word):
        return False
    return is_palindrome(middle(word))
print(is_palindrome('booob'))





