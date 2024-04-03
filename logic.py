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
    return matrix_output
