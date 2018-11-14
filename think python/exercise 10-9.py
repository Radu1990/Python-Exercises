import random
i = 23
#  kids in class


def random_day():
    x = random.randint(1, 31)
    return x


def list_of_bday(kids):
    list_of_birthdays = []
    for x in range(kids):
        list_of_birthdays = list_of_birthdays + [random_day()]
    print('Random list of bdays:', list_of_birthdays)
    return list_of_birthdays


def has_duplicates(input_list):
    filtered_list = []
    duplicates_list = []
    for x in input_list:
        if x not in filtered_list:
            filtered_list = filtered_list + [x]
        else:
            duplicates_list = duplicates_list + [x]
    len_days = len(duplicates_list)
    print('Duplicates list:', duplicates_list)
    print('Number of kids with same bday:', len_days)
    return len_days


def calculate_percentage(duplicates, total_kids):

    percentage = duplicates * 100 / total_kids
    print('The percentage of kids who have the same B-day is:', percentage, '%')


bday_variable = has_duplicates(list_of_bday(i))

calculate_percentage(bday_variable, i)