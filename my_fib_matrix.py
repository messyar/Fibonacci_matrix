def mult_matrix(matrix_in_1, matrix_in_2):
    """
    Функция перемножения двух матриц matrix_in_1 и matrix_in_2
    :param matrix_in_1: входящая матрица 1
    :param matrix_in_2: входящая матрица 2
    :return: матрицу результат умножения матриц 1 и 2
    """
    matrix_return = [[0, 0],
                     [0, 0]]

    for i, row in enumerate(matrix_in_1):

        for k in range(len(row)):
            needed_element = 0
            for j in range(len(matrix_in_2)):
                needed_element += row[j] * matrix_in_2[j][k]

            matrix_return[i][k] = needed_element

    return matrix_return


def fib_matrix(n):
    """
    Фукнция вычисления числа фибоначи порядкового номера n
    :param n: порядковое число Фибоначчи
    :return: число Фибоначчи порядка n
    """

    matrix_one = [[1, 1], [1, 0]]
    matrix_cur = matrix_one

    if n == 0:
        return matrix_one[1][1]
    if n == 1:
        return matrix_one[0][1]

    steps = []
    cur_step = n
    while cur_step:
        steps.append(cur_step)
        cur_step //= 2

    steps = steps[:-1]
    steps = steps[::-1]

    for step in steps:
        matrix_cur = mult_matrix(matrix_cur, matrix_cur)

        if step % 2:
            matrix_cur = mult_matrix(matrix_cur, matrix_one)

    return matrix_cur[0][1] % 10


num = int(input())
fib_num = fib_matrix(num)
print(fib_num)