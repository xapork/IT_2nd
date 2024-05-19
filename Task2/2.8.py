import math

class Gayes:
    def __init__(self, x, y):
        self.points = [(x, y)]

    def add_t(self, x, y):
        self.points.append((x, y))
        return self.points

    def interval(self):
        if len(self.points) < 2:
            print("Недостаточно точек для расчета расстояния")
            return None
        p1, p2 = self.points[0], self.points[1]
        distance = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
        print(distance)
        return distance

    def move(self, x_s, y_s):
        x, y = self.points[0]
        self.points[0] = (x + x_s, y + y_s)
        return self.points

    def check_ot(self):
        x, y = self.points[0]
        if x == 0 or y == 0:
            print('Принадлежит')
            return True
        else:
            print('Не принадлежит')
            return False
g = Gayes(1, 2)
g.add_t(3, 4)
g.rasstoyanie()
g.peremesti(1, 1)
g.check_os()