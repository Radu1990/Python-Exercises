fin = open('words.txt')

words_lst = []


#  FAST VERSION 1 second

counter = 0

for line in fin:

    word = line.strip()

    words_lst = words_lst + [word]
    print(words_lst)

    counter = counter + 1

    if counter == 1000:
       break

print(words_lst)


#  SLOW VERSION 31.92 seconds

#counter = 0
#
#for line in fin:
#
#    word = line.strip()
#    words_lst.append(word)
#    print(words_lst)
#
#    counter = counter + 1
#
#    if counter == 10000:
#        break
#
#print(words_lst)

