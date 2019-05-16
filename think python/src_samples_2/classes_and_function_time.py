class Time:
    """Represents the time of day
    attributes: hour, minute, second"""
    hour = int
    minute = int
    second = int

    def time_to_int(self):
        """
            This function converts times to integers
            :param self:
            :return seconds:
            """
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds



def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))


def is_after(t1, t2):
    t1_var = (t1.hour, t1.minute, t1.second)
    t2_var = (t2.hour, t2.minute, t2.second)
    return t1_var > t2_var


def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum


def increment(time, seconds):
    time.second += seconds

    if time.second >= 60:
        extra_minutes = time.second // 60
        extra_seconds = time.second % 60
        time.minute += extra_minutes
        time.second = extra_seconds

    if time.minute >= 60:
        extra_hours = time.minute // 60
        extra_minutes = time.minute % 60
        time.hour += extra_hours
        time.minute = extra_minutes


def time_to_int(time):
    """
    This function converts times to integers
    :param time:
    :return seconds:
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    """
    This function converts integers to times
    :param seconds:
    :return:
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


#######################################################################################################################


#  Time and time check
time_1 = Time()
time_1.hour = 11
time_1.minute = 59
time_1.second = 30
time_2 = Time()
time_2.hour = 11
time_2.minute = 59
time_2.second = 55
print('this is time 1')
print_time(time_1)
print('true or false if t2 > t1')
print(is_after(time_1, time_2))

#  When Movie ends
start = Time()
start.hour = 9
start.minute = 45
start.second = 0
duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0
done = add_time(start, duration)
print('after movie time')
print_time(done)

#  Increment time using modifier function
time_3 = Time()
time_3.hour = 11
time_3.minute = 30
time_3.second = 30
print('before incrementation'), print_time(time_3)
increment(time_3, 232)
print('after incrementation'), print_time(time_3)

#  Testing functions
time_4 = Time()
time_4.hour = 6
time_4.minute = 30
time_4.second = 0

print_time(time_4)
print(time_to_int(time_4))
print_time(int_to_time(23400))

#  Testing multiple values of time
x1 = 23400
x2 = 21000
x3 = 14500
x4 = 23800
x5 = 21500
x6 = 15500


def check_values(x):
    if time_to_int(int_to_time(x)) == x:
        return True
    return False


lst_values = [x1, x2, x3, x4, x5, x6]
for x in lst_values:
    print(check_values(x))
#  check is ok!

#  rewrite add_time
def add_time_var2(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


#  rewrite increment
def increment_var2(time, seconds):
    time_var = time_to_int(time) + seconds
    time_var = int_to_time(time_var)
    (time.hour, time.minute, time.second) = (time_var.hour, time_var.minute, time_var.second)


#  Testing increment rewritten
time_5 = Time()
time_5.hour = 11
time_5.minute = 30
time_5.second = 30
print('before incrementation'), print_time(time_5)
increment_var2(time_5, 232)
print('after incrementation'), print_time(time_5)


#  rewrite time_to_int
"""
def time_to_int(self):
    minutes = self.hour * 60 + self.minute
    seconds = minutes * 60 + self.second
    return seconds
"""

#  Testing new time_to_int method
time_6 = Time()
time_6.hour = 11
time_6.minute = 30
time_6.second = 30

print(time_6.time_to_int())

#  writing __init__ of Point


class Point:

    """
    Represents a point in 2D space:

    attributes: x coordinate, y coordinate
    """
    x = int
    y = int

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '%d,%d' % (self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            return self.x + other.x, self.y + other.y
        else:
            return self.x + other[0], self.y + other[1]

    def __radd__(self, other):
        return self.__add__(other)


point_1 = Point()
#  Testing print point object
print(point_1)
point_2 = Point(1, 17)
point_3 = Point(10, 20)
#  Testing point + point
print(point_2 + point_3)
#  Testing point + tuple
print(point_2 + (1, 2))
#  Testing right-side-add radd
print((1, 2) + point_2)

