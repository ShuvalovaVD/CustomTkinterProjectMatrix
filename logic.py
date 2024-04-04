def convert_matrix_input_to_matrix(matrix_input, rows, columns):
    lst = matrix_input.split()  # разбивает всё в одномерный список, из которого сформируем двумерный
    matrix = []
    for i in range(rows):
        tmp = [0] * columns
        matrix.append(tmp)
    for i in range(rows):
        for j in range(columns):
            ind = i * columns + j
            matrix[i][j] = int(lst[ind])
    return matrix


def convert_matrix_to_matrix_output(matrix, rows, columns):
    s_output = ""
    for i in range(rows):
        for j in range(columns):
            s_output += str(matrix[i][j])
            if j == columns - 1:
                s_output += "\n"
            else:
                s_output += " "
    return s_output


def convert_number_input_to_number(number_input):
    number = int(number_input)
    return number


def multiply_matrix_by_number(rows_input, columns_input, matrix_input, number_input):  # умножает матрицу на число
    number = int(number_input)
    rows = int(rows_input)
    columns = int(columns_input)
    matrix = convert_matrix_input_to_matrix(matrix_input, rows, columns)
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] *= number
    matrix_output = convert_matrix_to_matrix_output(matrix, rows, columns)
    rows_output, columns_output = rows_input, columns_input
    return (rows_output, columns_output, matrix_output)


def transpone_matrix(rows_input, columns_input, matrix_input):  # транспонирует матрицу
    rows = int(rows_input)
    columns = int(columns_input)
    matrix = convert_matrix_input_to_matrix(matrix_input, rows, columns)
    new_rows, new_columns = columns, rows
    # изначально заполним новую (транспонированную) матрицу нулями
    new_matrix = []
    for i in range(new_rows):
        tmp = [0] * new_columns
        new_matrix.append(tmp)
    # теперь перезаписываем новую матрицу
    for j in range(columns):
        for i in range(rows):
            new_matrix[j][i] = matrix[i][j]
    matrix_output = convert_matrix_to_matrix_output(new_matrix, new_rows, new_columns)
    rows_output, columns_output = columns_input, rows_input
    return (rows_output, columns_output, matrix_output)


def check_symmetry_of_matrix(rows_input, columns_input, matrix_input):  # проверяет матрицу на симметричность
    rows = int(rows_input)
    columns = int(columns_input)
    matrix = convert_matrix_input_to_matrix(matrix_input, rows, columns)
    # как только находит что-то несимметричное, сразу flag = False, иначе в самом конце если ничего не нашло = True
    flag = True
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] != matrix[j][i]:
                flag = False
                break
        if not flag:
            break
    check_output = "Матрица симметрична" if flag else "Матрица несимметрична"
    return check_output


def add_two_matrix(rows_1_input, columns_1_input, matrix_1_input, rows_2_input, columns_2_input, matrix_2_input):
    # складывает две матрицы
    rows_1 = int(rows_1_input)
    columns_1 = int(columns_1_input)
    matrix_1 = convert_matrix_input_to_matrix(matrix_1_input, rows_1, columns_1)
    rows_2 = int(rows_2_input)
    columns_2 = int(columns_2_input)
    matrix_2 = convert_matrix_input_to_matrix(matrix_2_input, rows_2, columns_2)
    # результат будет складываться в матрицу matrix1
    rows, columns = rows_1, columns_1
    for i in range(rows):
        for j in range(columns):
            matrix_1[i][j] += matrix_2[i][j]
    matrix_output = convert_matrix_to_matrix_output(matrix_1, rows, columns)
    rows_output, columns_output = rows_1, columns_1
    return (rows_output, columns_output, matrix_output)


def subtract_two_matrix(rows_1_input, columns_1_input, matrix_1_input, rows_2_input, columns_2_input, matrix_2_input):
    # вычитает из первой матрицы вторую
    # matrix1 - matrix2 = matrix1 + (-1 * matrix2)
    rows_2_opposite, columns_2_opposite, matrix_2_opposite = multiply_matrix_by_number(rows_2_input, columns_2_input,\
                                                                                       matrix_2_input, '-1')
    rows_output, columns_output, matrix_output = add_two_matrix(rows_1_input, columns_1_input, matrix_1_input,\
                                                                rows_2_opposite, columns_2_opposite, matrix_2_opposite)
    return (rows_output, columns_output, matrix_output)


def multiply_two_matrix(rows_1_input, columns_1_input, matrix_1_input, rows_2_input, columns_2_input, matrix_2_input):
    # умножает две матрицы
    rows_1 = int(rows_1_input)
    columns_1 = int(columns_1_input)
    matrix_1 = convert_matrix_input_to_matrix(matrix_1_input, rows_1, columns_1)
    rows_2 = int(rows_2_input)
    columns_2 = int(columns_2_input)
    matrix_2 = convert_matrix_input_to_matrix(matrix_2_input, rows_2, columns_2)
    # умножение двух матриц определено, если кол-во столбцов 2-ой = кол-ву строк 1-ой, это уже проверено
    # размер результирующей матрицы: кол-во строк 1-ой и кол-во столбцов 2-ой
    rows, columns = rows_1, columns_2
    # изначально заполним результирующую матрицу нулями
    matrix = []
    for i in range(rows):
        tmp = [0] * columns
        matrix.append(tmp)
    # при умножении двух матрицы строки первой покоординатно умножаются на столбцы второй
    for i in range(rows):
        for j in range(columns):
            # ячейка [i][j] результирующей матрицы - это i-ая строка 1-ой, умноженная покоординатно на j-ый столбец 2-ой
            for k in range(columns_1):  # или rows2, неважно, они равны, если умножение матриц определено
                matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]  # постепенно покоординатно умножаем
    matrix_output = convert_matrix_to_matrix_output(matrix, rows, columns)
    rows_output, columns_output = str(rows), str(columns)
    return (rows_output, columns_output, matrix_output)
