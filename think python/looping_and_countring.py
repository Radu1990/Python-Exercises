input_word = input('Insert word: ')
input_letter = input('Insert letter to be counted: ')
input_letterfrom = int(input('Insert position of letter where the search should start from: '))



def counting_letters(word, letter, letterfrom):
    count = 0
    index = letterfrom
    while index < len(word):
        if word[index] == letter:
            count = count + 1
            #print(word[index])
            #print(count)

        index = index + 1
    return count

print('the word', input_word, 'contains the letter', input_letter, counting_letters(input_word, input_letter, input_letterfrom), 'times!')



