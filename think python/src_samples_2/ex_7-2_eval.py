# this program evaluates mathematical expressions
# until the user enters "done"

def eval_loop():
    while True:
        line = input('Enter input data to be evaluated here: \n>')
        if line == 'done':
            print('GAME OVER!')
            break
        result = eval(line)
        print(result)

eval_loop()
