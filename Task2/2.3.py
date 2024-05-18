class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        a, b, c = self.a, self.b, self.c
        if a <= 0 or b <= 0 or c <= 0:
            print('С отрицательными числами ничего не выйдет')
            return
        try:
            if a + b > c and a + c > b and b + c > a:
                print('Ура, можно постороить треугольник')
            else:
                print('Жаль, но из этого треугольника сделать')
        except TypeError:
            print('Нужно вводить только числа!')

triangle = TriangleChecker(354, -24, 12)
triangle.is_triangle()