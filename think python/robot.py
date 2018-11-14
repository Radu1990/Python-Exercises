class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_myself(self):
        print('My name is ' + self.name)


r1 = Robot('Jerry', 'red', 320)
r2 = Robot('Tom', 'blue', 140)
# r1.introduce_myself()


class Person:
    def __init__(self, name, personality, i, r):
        self.name = name
        self.personality = personality
        self.is_sitting = i
        self.robot_owned = r

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False


p1 = Person("Maria", "friendly", False, r2)
p2 = Person("Laura", "interesting", True, r1)

p1.robot_owned.introduce_myself()
