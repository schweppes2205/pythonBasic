"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
класса (метод init()), который должен принимать данные (список списков)
для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы
в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц). Результатом сложения
должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый
элемент первой строки первой матрицы складываем с первым элементом
первой строки второй матрицы и т.д."""


class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix
        self.i = len(matrix)
        self.j = len(matrix[0])

    @property
    def get_matrix_i(self):
        return self.i

    @property
    def get_matrix_j(self):
        return self.j

    def __str__(self):
        result = ""
        for i in range(self.i):
            for j in range(self.j):
                result += f"{(self.matrix[i][j])} "
            result += "\n"
        return result

    def __add__(self, other):
        result = []
        if self.i == other.i and self.j == other.j:
            for i in range(self.i):
                temp_list = []
                for j in range(self.j):
                    temp_list.append(self.matrix[i][j] + other.matrix[i][j])
                result.append(temp_list)
        else:
            print(f"both matrix should have equal amount of lines and columns. Now its {self.i}:{self.j} "
                  f"and {other.i}:{other.j}")
            return None
        return result


my_matrix_01 = Matrix(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12],
    ]
)
my_matrix_02 = Matrix(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12],
        [10, 11, 12],
    ]
)

print(f"first matrix\n{my_matrix_01}Second matrix\n{my_matrix_02}")

try:
    print("let's try to make a new Matrix object out of them")
    my_matrix_03 = Matrix(my_matrix_01 + my_matrix_02)
    print(my_matrix_03)
except:
    pass
my_matrix_02 = Matrix(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12],
    ]
)
try:
    print("now let's do it correctly")
    my_matrix_03 = Matrix(my_matrix_01 + my_matrix_02)
    print(my_matrix_03)
except:
    pass