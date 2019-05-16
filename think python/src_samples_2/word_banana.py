# making a function out of it
def lettercounter(word):
    count = 0
    for x in word:
        if x == "a":
            count = count + 1
    print(count)


lettercounter("banana")
# writting a word with uppercase letters
word = "romania"
new_word = word.upper()
print(new_word)

fruit = "banana"
if "an" in fruit:
    print("yes an is in fruit")
