import os


def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

# walk('c:/users')


def walk2(dirname):
    """Prints the names of all files in dirname and its subdirectories.

    This is the exercise solution, which uses os.walk.

    dirname: string name of directory
    """
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print(os.path.join(root, filename))
