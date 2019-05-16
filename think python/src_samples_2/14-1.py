def sed(pattern_string, replacement_string, filename_1, filename_2):

    fin = open(filename_1)
    fout = open(filename_2, 'w')

    for line in fin:
        words = line.split()
        print(words)
        words = [x.replace(pattern_string, replacement_string) for x in words]
        print(words)
        new_string = ' '.join(words)

        fout.write(new_string)
        fout.write('\n')


sed('HUMBLE', 'happy', 'file_1.txt', 'file_2.txt')

