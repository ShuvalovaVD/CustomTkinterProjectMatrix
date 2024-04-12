import logic  # импортируем наш модуль с логикой
import tkinter as tk  # импортируем модуль tkinter
import customtkinter as ctk  # импортируем модуль customtkinter
from tkinter.messagebox import *  # пока не изучено, опробовано лишь на практике!

# ОСТАЛОСЬ РЕАЛИЗОВАТЬ РАБОТУ С ОШИБКАМИ И ИСКЛЮЧЕНИЯМИ: ПОЛЬЗОВАТЕЛЬ ДОЛЖЕН ВВОДИТЬ ДАННЫЕ В ПРАВИЛЬНОМ ФОРМАТЕ,
# ИНАЧЕ БУДЕТ ВОЗНИКАТЬ ОКНО MESSAGE (КАК ПРИ ЗАКРЫТИИ) С ПОЯСНЕНИЕМ И БУДЕТ НОВАЯ ПОПЫТКА ВВОДА

# ДАЛЕЕ ПОДРОБНО ЗАДОКУМЕНТИРОВАТЬ И СОЗДАТЬ СХЕМУ ФУНКЦИЙ


def close_app():  # пока не изучено, опробовано лишь на практике!
    ans = askyesno(title="Выход", message="Вы ходите закрыть программу?")
    if ans:
        root.destroy()  # закрываем окно


def set_grid():  # создаёт сетку, в которой потом будем размещать виджеты с помощью метода .grid()
    # это один из трёх способов позиционирования, также есть pack и place
    rows, columns = 7, 5  # сетка 7 x 5
    for i in range(rows):
        root.rowconfigure(index=i, weight=1)
    for i in range(columns):
        root.columnconfigure(index=i, weight=1)


def show_menu():  # показывает меню выбора операций над матрицами
    menu_lbl.grid(row=0, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky="nsew")
    menu_btn_1.grid(row=1, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky="nsew")
    menu_btn_2.grid(row=2, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky="nsew")
    menu_btn_3.grid(row=3, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky="nsew")
    menu_btn_4.grid(row=4, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky="nsew")
    menu_btn_5.grid(row=5, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky="nsew")
    menu_btn_6.grid(row=6, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky="nsew")


def close_menu():  # скрывает меню
    menu_lbl.grid_forget()
    menu_btn_1.grid_forget()
    menu_btn_2.grid_forget()
    menu_btn_3.grid_forget()
    menu_btn_4.grid_forget()
    menu_btn_5.grid_forget()
    menu_btn_6.grid_forget()

def show_matrix_size_input():  # показывает ввод размеров матрицы
    if op_step == "matrix_size_input":
        matrix_size_input_lbl.configure(text=f"Введите размеры матрицы (кол-во строк и кол-во столбцов):")
    elif op_step == "matrix_1_size_input":
        matrix_size_input_lbl.configure(text=f"Введите размеры первой матрицы (кол-во строк и кол-во столбцов):")
    else:
        matrix_size_input_lbl.configure(text=f"Введите размеры второй матрицы (кол-во строк и кол-во столбцов):")
    matrix_size_input_lbl.grid(row=0, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky="nsew")
    matrix_size_input_lbl_rows.grid(row=1, column=1, ipadx=4, ipady=4, pady=6, sticky="nsew")
    rows_input_entry.delete(0, "end")
    rows_input_entry.grid(row=1, column=3, ipadx=4, ipady=4, pady=6, sticky="nsew")
    matrix_size_input_lbl_columns.grid(row=2, column=1, ipadx=4, ipady=4, pady=6, sticky="nsew")
    columns_input_entry.delete(0, "end")
    columns_input_entry.grid(row=2, column=3, ipadx=4, ipady=4, pady=6, sticky="nsew")
    matrix_size_input_btn_done.grid(row=4, column=1, ipadx=4, ipady=4, pady=6, sticky="nsew")
    matrix_size_input_btn_cancel.grid(row=4, column=3, ipadx=4, ipady=4, pady=6, sticky="nsew")


def close_matrix_size_input():  # скрывает ввод размеров матрицы
    matrix_size_input_lbl.grid_forget()
    matrix_size_input_lbl_rows.grid_forget()
    rows_input_entry.grid_forget()
    matrix_size_input_lbl_columns.grid_forget()
    columns_input_entry.grid_forget()
    matrix_size_input_btn_done.grid_forget()
    matrix_size_input_btn_cancel.grid_forget()


def show_matrix_input():  # показывает ввод матрицы
    global op_step
    if op_step == "matrix_input":
        matrix_input_lbl.configure(text=f"Введите матрицу {rows_input} x {columns_input}:")
    elif op_step == "matrix_1_input":
        matrix_input_lbl.configure(text=f"Введите первую матрицу {rows_1_input} x {columns_1_input}:")
    else:
        matrix_input_lbl.configure(text=f"Введите вторую матрицу {rows_2_input} x {columns_2_input}:")
    matrix_input_lbl.grid(row=0, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky="nsew")
    matrix_input_text.delete("1.0", "end")
    matrix_input_text.grid(row=1, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky="nsew")
    matrix_input_btn_done.grid(row=2, column=1, ipadx=4, ipady=4, pady=6, sticky="nsew")
    matrix_input_btn_cancel.grid(row=2, column=3, ipadx=4, ipady=4, pady=6, sticky="nsew")


def close_matrix_input():  # скрывает ввод матрицы
    matrix_input_text.grid_forget()
    matrix_input_lbl.grid_forget()
    matrix_input_btn_done.grid_forget()
    matrix_input_btn_cancel.grid_forget()


def show_number_input():  # показывает ввод числа
    number_input_lbl.grid(row=0, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky="nsew")
    number_input_entry.delete(0, "end")
    number_input_entry.grid(row=1, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky="nsew")
    number_input_btn_done.grid(row=2, column=1, ipadx=4, ipady=4, pady=6, sticky="nsew")
    number_input_btn_cancel.grid(row=2, column=3, ipadx=4, ipady=4, pady=6, sticky="nsew")


def close_number_input():  # скрывает вывод числа
    number_input_lbl.grid_forget()
    number_input_entry.grid_forget()
    number_input_btn_done.grid_forget()
    number_input_btn_cancel.grid_forget()


def show_matrix_output():  # показываем вывод итоговой матрицы
    matrix_output_lbl.configure(text=f"Ваша итоговая матрица с размерами {rows_output} x {columns_output}:")
    matrix_output_lbl.grid(row=0, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky="nsew")
    matrix_output_lbl_result.configure(text=matrix_output)
    matrix_output_lbl_result.grid(row=1, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky="nsew")
    matrix_output_btn_done.grid(row=2, column=1, ipadx=4, ipady=4, pady=6, sticky="nsew")
    matrix_output_btn_cancel.grid(row=2, column=3, ipadx=4, ipady=4, pady=6, sticky="nsew")


def close_matrix_output():  # скрывает вывод итоговой матрицы
    matrix_output_lbl.grid_forget()
    matrix_output_lbl_result.grid_forget()
    matrix_output_btn_done.grid_forget()
    matrix_output_btn_cancel.grid_forget()


def show_check_output():  # показывает вывод проверки матрицы
    check_output_lbl.configure(text=check_output)
    check_output_lbl.grid(row=1, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky="nsew")
    check_output_btn_done.grid(row=2, column=1, ipadx=4, ipady=4, pady=6, sticky="nsew")
    check_output_btn_cancel.grid(row=2, column=3, ipadx=4, ipady=4, pady=6, sticky="nsew")


def close_check_output():  # скрывает вывод проверки матрицы
    check_output_lbl.grid_forget()
    check_output_btn_done.grid_forget()
    check_output_btn_cancel.grid_forget()


def handle_pressing_menu_btn_1():
    global op_type, op_step
    op_type, op_step = 1, "matrix_size_input"
    close_menu()
    show_matrix_size_input()


def handle_pressing_menu_btn_2():
    global op_type, op_step
    op_type, op_step = 2, "matrix_size_input"
    close_menu()
    show_matrix_size_input()


def handle_pressing_menu_btn_3():
    global op_type, op_step
    op_type, op_step = 3, "matrix_size_input"
    close_menu()
    show_matrix_size_input()


def handle_pressing_menu_btn_4():
    global op_type, op_step
    op_type, op_step = 4, "matrix_1_size_input"
    close_menu()
    show_matrix_size_input()


def handle_pressing_menu_btn_5():
    global op_type, op_step
    op_type, op_step = 5, "matrix_1_size_input"
    close_menu()
    show_matrix_size_input()


def handle_pressing_menu_btn_6():
    global op_type, op_step
    op_type, op_step = 6, "matrix_1_size_input"
    close_menu()
    show_matrix_size_input()


def handle_pressing_matrix_size_input_btn_done():
    global op_step, rows_input, columns_input, rows_1_input, columns_1_input, rows_2_input, columns_2_input
    # !!! пока предположим, что пользователь действительно что-то ввёл
    if 1 <= op_type <= 3:
        rows_input, columns_input = rows_input_entry.get(), columns_input_entry.get()
        op_step = "matrix_input"
    else:
        if op_step == "matrix_1_size_input":
            rows_1_input, columns_1_input = rows_input_entry.get(), columns_input_entry.get()
            op_step = "matrix_1_input"
        else:
            rows_2_input, columns_2_input = rows_input_entry.get(), columns_input_entry.get()
            op_step = "matrix_2_input"
    close_matrix_size_input()
    show_matrix_input()


def handle_pressing_matrix_size_input_btn_cancel():
    global op_type, op_step
    close_matrix_size_input()
    if 4 <= op_type:
        if op_step == "matrix_2_size_input":
            op_step = "matrix_1_input"
            show_matrix_input()
        else:
            op_type, op_step = None, "menu"
            show_menu()
    else:
        op_type, op_step = None, "menu"
        show_menu()


def handle_pressing_matrix_input_btn_done():
    global op_step, matrix_input, rows_output, columns_output, matrix_output, check_output,\
        matrix_1_input, matrix_2_input
    # !!! пока предположим, что пользователь ввел матрицу верно
    if 1 <= op_type <= 3:
        matrix_input = matrix_input_text.get("1.0", "end")
        close_matrix_input()
        if op_type == 1:
            op_step = "number_input"
            show_number_input()
        elif op_type == 2:
            op_step = "matrix_output"
            rows_output, columns_output, matrix_output = logic.transpone_matrix(rows_input, columns_input, matrix_input)
            show_matrix_output()
        else:
            op_step = "check_output"
            check_output = logic.check_symmetry_of_matrix(rows_input, columns_input, matrix_input)
            show_check_output()
    else:
        if op_step == "matrix_1_input":
            matrix_1_input = matrix_input_text.get("1.0", "end")
            op_step = "matrix_2_size_input"
            close_matrix_input()
            show_matrix_size_input()
        else:
            matrix_2_input = matrix_input_text.get("1.0", "end")
            op_step = "matrix_output"
            close_matrix_input()
            if op_type == 4:
                rows_output, columns_output, matrix_output = logic.add_two_matrix(rows_1_input, columns_1_input,\
                                                                                  matrix_1_input, rows_2_input,\
                                                                                  columns_2_input, matrix_2_input)
            elif op_type == 5:
                rows_output, columns_output, matrix_output = logic.subtract_two_matrix(rows_1_input, columns_1_input,\
                                                                                  matrix_1_input, rows_2_input,\
                                                                                  columns_2_input, matrix_2_input)
            else:
                rows_output, columns_output, matrix_output = logic.multiply_two_matrix(rows_1_input, columns_1_input,\
                                                                                  matrix_1_input, rows_2_input,\
                                                                                  columns_2_input, matrix_2_input)
            show_matrix_output()


def handle_pressing_matrix_input_btn_cancel():
    global op_step
    if 1 <= op_type <= 3:
        op_step = "matrix_size_input"
    else:
        if op_step == "matrix_1_input":
            op_step = "matrix_1_size_input"
        else:
            op_step = "matrix_2_size_input"
    close_matrix_input()
    show_matrix_size_input()


def handle_pressing_number_input_btn_done():
    global number_input, matrix_output, op_step, rows_output, columns_output
    number_input = number_input_entry.get()
    op_step = "matrix_output"
    close_number_input()
    # логика: передаем в модуль logic считанные от пользователя данные и получаем ответ
    rows_output, columns_output, matrix_output = logic.multiply_matrix_by_number(rows_input, columns_input,\
                                                                                 matrix_input, number_input)
    show_matrix_output()


def handle_pressing_number_input_btn_cancel():
    global op_step
    op_step = "matrix_input"
    close_number_input()
    show_matrix_input()


def handle_pressing_matrix_output_btn_done():
    global op_type, op_step
    op_type, op_step = None, "menu"
    close_matrix_output()
    show_menu()


def handle_pressing_matrix_output_btn_cancel():
    global op_step
    close_matrix_output()
    if op_type == 1:
        op_step = "number_input"
        show_number_input()
    elif 2 <= op_type <= 3:
        op_step = "matrix_input"
        show_matrix_input()
    else:
        op_step = "matrix_2_input"
        show_matrix_input()


def handle_pressing_check_output_btn_done():
    global op_type, op_step
    op_type, op_step = None, "menu"
    close_check_output()
    show_menu()


def handle_pressing_check_output_btn_cancel():
    global op_step
    op_step = "matrix_input"
    close_check_output()
    show_matrix_input()


# создаём переменные, в которых будут лежать данные, которые считали от пользователя
# если операция будет производиться над одной матрицей
number_input, rows_input, columns_input, matrix_input, check_output = None, None, None, None, None
# если операция будет производиться над двумя матрицами
rows_1_input, columns_1_input, rows_2_input, columns_2_input = None, None, None, None
matrix_1_input, matrix_2_input = None, None

# создаём переменные, в которых будут лежать данные, которые будут выводиться пользователю
rows_output, columns_output = None, None
matrix_output = None

# переменные-флаги, отвечающие за тип операции (1-6) и её этап
op_type, op_step = None, "menu"
# например, для операции 1 её этапы: matrix_size_input, matrix_input, number_input, matrix_output

root = ctk.CTk()  # создаём окно и привязываем его переменной root
# через переменную root будем управлять атрибутами окна
root.title("Преобразования матриц")  # устанавливаем заголовок окна
root.geometry("1000x500")  # устанавливаем размеры окна
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# о виджетах можно узнавать информацию через специальные методы, но чтобы это сделать, мы должны применить этот метод
root.update()  # без него все св-ва будут применены только при вызове метода .mainloop()
window_size_info = root.geometry()  # например, так мы узнаем размер окна, заданный ранее этим методом
# но в данной программе нам это не понадобится, это просто учебная информация

# создаём виджеты для меню - menu
# текстовая метка Label() для сообщения в меню выбора команд
menu_lbl = ctk.CTkLabel(master=root)
# можно указывать св-ва при создании в Label(), а можно установить их позже в методе .configure()
menu_lbl.configure(text="Выберите операцию из списка:")
# кнопки меню: позволят выбрать 6 преобразований матриц
menu_btn_1, menu_btn_2, menu_btn_3, menu_btn_4, menu_btn_5, menu_btn_6 = ctk.CTkButton(master=root),\
    ctk.CTkButton(master=root), ctk.CTkButton(master=root), ctk.CTkButton(master=root), ctk.CTkButton(master=root),\
    ctk.CTkButton(master=root)  # создаем кнопки
menu_btn_1.configure(text="1. Умножение матрицы на число", command=handle_pressing_menu_btn_1)
menu_btn_2.configure(text="2. Транспонирование матрицы", command=handle_pressing_menu_btn_2)
menu_btn_3.configure(text="3. Проверка матрицы на симметричность", command=handle_pressing_menu_btn_3)
menu_btn_4.configure(text="4. Сложение двух матриц", command=handle_pressing_menu_btn_4)
menu_btn_5.configure(text="5. Вычитание двух матриц (из первой матрицы вычитается вторая)",\
                     command=handle_pressing_menu_btn_5)
menu_btn_6.configure(text="6. Умножение двух матриц (перед этим будет проверка на возможность умножения)",\
                     command=handle_pressing_menu_btn_6)

# виджеты для ввода размеров матрицы (не важно, какая операция 1-6) - matrix_size_input
matrix_size_input_lbl = ctk.CTkLabel(master=root)  # настраиваться текст будет в зависимости от типа операции
matrix_size_input_lbl_rows, matrix_size_input_lbl_columns = ctk.CTkLabel(master=root), ctk.CTkLabel(master=root)
matrix_size_input_lbl_rows.configure(text="Количество строк:")
matrix_size_input_lbl_columns.configure(text="Количество столбцов:")
rows_input_entry, columns_input_entry = ctk.CTkEntry(master=root), ctk.CTkEntry(master=root)
rows_input_entry.configure(justify="center")
columns_input_entry.configure(justify="center")
matrix_size_input_btn_done, matrix_size_input_btn_cancel = ctk.CTkButton(master=root), ctk.CTkButton(master=root)
matrix_size_input_btn_done.configure(text="Готово", command=handle_pressing_matrix_size_input_btn_done)
matrix_size_input_btn_cancel.configure(text="Назад", command=handle_pressing_matrix_size_input_btn_cancel)

# виджеты для ввода матрицы (не важно, какая операция 1-6) - matrix_input
matrix_input_text = ctk.CTkTextbox(master=root)
matrix_input_lbl = ctk.CTkLabel(master=root)  # настраиваться текст будет в зависимости от размеров матрицы
matrix_input_btn_done, matrix_input_btn_cancel = ctk.CTkButton(master=root), ctk.CTkButton(master=root)
matrix_input_btn_done.configure(text="Готово", command=handle_pressing_matrix_input_btn_done)
matrix_input_btn_cancel.configure(text="Назад", command=handle_pressing_matrix_input_btn_cancel)

# виджеты для ввода числа - number_input
number_input_lbl = ctk.CTkLabel(master=root)
number_input_lbl.configure(text="Введите число, на которое будет умножаться матрица:")
number_input_entry = ctk.CTkEntry(master=root)
number_input_entry.configure(justify="center")
number_input_btn_done, number_input_btn_cancel = ctk.CTkButton(master=root), ctk.CTkButton(master=root)
number_input_btn_done.configure(text="Готово", command=handle_pressing_number_input_btn_done)
number_input_btn_cancel.configure(text="Назад", command=handle_pressing_number_input_btn_cancel)

# виджеты для вывода матрицы (не важно, какая операция 1-6) - matrix_output
matrix_output_lbl = ctk.CTkLabel(master=root)  # настраиваться текст будет в зависимости от размером матрицы
matrix_output_lbl_result = ctk.CTkLabel(master=root)  # вывод матрицы в ответе
matrix_output_btn_done, matrix_output_btn_cancel = ctk.CTkButton(master=root), ctk.CTkButton(master=root)
matrix_output_btn_done.configure(text="Готово", command=handle_pressing_matrix_output_btn_done)
matrix_output_btn_cancel.configure(text="Назад", command=handle_pressing_matrix_output_btn_cancel)

# виджеты для вывода вердикта проверки матрицы на симметричность - check_output
check_output_lbl = ctk.CTkLabel(master=root)  # настраиваться текст будет в зависимости от результата проверки
check_output_btn_done, check_output_btn_cancel = ctk.CTkButton(master=root), ctk.CTkButton(master=root)
check_output_btn_done.configure(text="Готово", command=handle_pressing_check_output_btn_done)
check_output_btn_cancel.configure(text="Назад", command=handle_pressing_check_output_btn_cancel)

# перехватываем событие закрытия окна: если нажат крестик, вызывается функция close_app()
root.protocol("WM_DELETE_WINDOW", close_app)

set_grid()
show_menu()
root.mainloop()  # отображаем окно и запускаем цикл обработки событий окна для взаимодействия c пользователем
