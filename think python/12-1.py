s_text =('In this year the monastery at Westminster was hallowed on Childermas day (28 December). And king Eadward died on Twelfth-mass eve (5 January) and he was buried on Twelfth-mass day, in the newly hallowed church at Westminster. And earl Harold succeeded to the Kingdom of England, as the king had granted it to him and men had also chosen him thereto and he was blessed as king on Twelfth-mass day. And in the same year that he was king he went out with a naval force against William ... And the while count William landed at Hastings, on St. Michaels mass-day and Harold came from the north and fought against him before his army had all come and there he fell and his two brothers Gyrth and Leofwine and William subdued this land, and came to Westminster and archbishop Ealdred hallowed him king and men paid him tribute and gave him hostages and afterwards bought their land')


def most_frequent(inp_string):

    sentence = inp_string.replace(" ", "")
    #  this gets rid of all of the whitespaces over all
    wf = dict()
    #  here we add string letters to a dictionary collection
    wf_reversed = dict()
    #  word frequency (wf)  this opens a dictionary like {} where we add the k,v in reversed order

    for x in sentence:

        if x not in wf:
            wf[x] = 0
        else:
            wf[x] = wf[x] + 1
    #  adding letters as k,v in dictionary
    print('dictionary is', wf)

    for key in wf:
        val = wf[key]
        if val not in wf_reversed:
            wf_reversed[val] = key
        else:
            wf_reversed[val] = wf_reversed[val] + key
    #  adding swapping key with values and adding them to new dictionary collection
    print('wf reversed', wf_reversed)

    swfr = sorted(wf_reversed, reverse=True)
    #  making a list of decreasingly sorted order from the new dictionary`s keys
    print('swfr', swfr)

    for x in swfr:
        print('Letter frequency for ', x, wf_reversed[x])
    #  printing the keys and values (values and keys) from the new dictionary in the order from the sorted list


most_frequent(s_text)