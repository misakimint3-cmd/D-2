#D-1

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area_value = math.pi * self.radius * self.radius
        return round(area_value, 2)

    def perimeter(self):
        perimeter_value = 2 * math.pi * self.radius
        return round(perimeter_value, 2)

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        area_value = self.height * self.width
        return round(area_value, 2)

    def diagonal(self):
        diagonal_value = math.sqrt(self.height ** 2 + self.width ** 2)
        return round(diagonal_value, 2)

#D-2

rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())  # 30.00
print(rectangle1.diagonal())  # 7.81

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())  # 9.00
print(rectangle2.diagonal())  # 4.24

#D-3 
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

#D-4

square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21

class MyCounterV1:
    def __init__(self, value):
        self.value = value

    def count_up(self):
        self.value += 1

counter1 = MyCounterV1(value=0)
print(counter1.value)  # 0

counter1.count_up()
print(counter1.value)  # 1

counter1.count_up()
print(counter1.value)  # 2

counter2 = MyCounterV1(value=7)
print(counter2.value)  # 7

counter2.count_up()
print(counter2.value)  # 8

counter2.count_up()
print(counter2.value)  # 9

class MyCounterV2:
    def __init__(self, value, step):
        self.value = value
        self.step = step

    def count_up(self):
        self.value += self.step

#D-5

counter1 = MyCounterV2(value=0, step=1)
print(counter1.value)  # 0

counter1.count_up()
print(counter1.value)  # 1

counter1.count_up()
print(counter1.value)  # 2

counter2 = MyCounterV2(value=0, step=3)
print(counter2.value)  # 0

counter2.count_up()
print(counter2.value)  # 3

counter2.count_up()
print(counter2.value)  # 6

class MyCounterV3:
    def __init__(self, value, step):
        self.value = value
        self.step = step

    def count_up(self):
        self.value += self.step

    def count_down(self):
        self.value -= self.step

#D-6

counter1 = MyCounterV3(value=1, step=2)
print(counter1.value)  # 1

counter1.count_up()
print(counter1.value)  # 3

counter1.count_up()
print(counter1.value)  # 5

counter1.count_down()
print(counter1.value)  # 3

counter2 = MyCounterV3(value=3, step=4)
print(counter2.value)  # 3

counter2.count_down()
print(counter2.value)  # -1

counter2.count_down()
print(counter2.value)  # -5