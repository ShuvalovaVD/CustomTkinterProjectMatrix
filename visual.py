import logic  # импортируем наш модуль с логикой
from tkinter import *  # импортируем модуль tkinter
from tkinter.messagebox import *  # пока не изучено, опробовано лишь на практике!


def close_app():  # пока не изучено, опробовано лишь на практике!
    ans = askyesno(title="Выход", message="Вы ходите закрыть программу?")
    if ans:
        root.destroy()  # закрываем окно


def set_grid():  # создаёт сетку, в которой потом будем размещать виджеты с помощью метода .grid()
    # это один из трёх способов позиционирования, также есть pack и place
    global root
    rows, columns = 7, 5
    for i in range(rows):
        root.rowconfigure(index=i, weight=1)
    for i in range(columns):
        root.columnconfigure(index=i, weight=1)


def show_menu():  # показывает меню выбора операций над матрицами
    global menu_btn_1, menu_btn_2, menu_btn_3, menu_btn_4, menu_btn_5, menu_btn_6, menu_lbl
    menu_lbl.grid(row=0, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    menu_btn_1.grid(row=1, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    menu_btn_2.grid(row=2, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    menu_btn_3.grid(row=3, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    menu_btn_4.grid(row=4, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    menu_btn_5.grid(row=5, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    menu_btn_6.grid(row=6, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)


def close_menu():  # скрывает меню
    global menu_btn_1, menu_btn_2, menu_btn_3, menu_btn_4, menu_btn_5, menu_btn_6, menu_lbl
    menu_lbl.grid_forget()
    menu_btn_1.grid_forget()
    menu_btn_2.grid_forget()
    menu_btn_3.grid_forget()
    menu_btn_4.grid_forget()
    menu_btn_5.grid_forget()
    menu_btn_6.grid_forget()

def show_matrix_size_input():  # показывает ввод размеров матрицы
    global matrix_size_input_lbl, rows_input_entry, columns_input_entry, decorative_multiplication_sign, matrix_size_input_btn_done,\
        matrix_size_input_btn_cancel
    matrix_size_input_lbl.grid(row=0, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    rows_input_entry.delete(0, END)
    rows_input_entry.grid(row=1, column=1, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    decorative_multiplication_sign.grid(row=1, column=2, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    columns_input_entry.delete(0, END)
    columns_input_entry.grid(row=1, column=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    matrix_size_input_btn_done.grid(row=2, column=1, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    matrix_size_input_btn_cancel.grid(row=2, column=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)


def close_matrix_size_input():  # скрывает ввод размеров матрицы
    global matrix_size_input_lbl, rows_input_entry, columns_input_entry, decorative_multiplication_sign, matrix_size_input_btn_done,\
        matrix_size_input_btn_cancel
    matrix_size_input_lbl.grid_forget()
    rows_input_entry.grid_forget()
    columns_input_entry.grid_forget()
    decorative_multiplication_sign.grid_forget()
    matrix_size_input_btn_done.grid_forget()
    matrix_size_input_btn_cancel.grid_forget()


def show_matrix_input():  # показывает ввод матрицы
    global rows_input, columns_input, matrix_input_text, matrix_input_lbl, matrix_input_btn_done,\
        matrix_input_btn_cancel
    matrix_input_lbl.config(text=f"Введите матрицу {rows_input} x {columns_input}:")
    matrix_input_lbl.grid(row=0, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    matrix_input_text.delete("1.0", END)
    matrix_input_text.grid(row=1, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    matrix_input_btn_done.grid(row=2, column=1, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    matrix_input_btn_cancel.grid(row=2, column=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)


def close_matrix_input():  # скрывает ввод матрицы
    global matrix_input_text, matrix_input_lbl, matrix_input_btn_done, matrix_input_btn_cancel
    matrix_input_text.grid_forget()
    matrix_input_lbl.grid_forget()
    matrix_input_btn_done.grid_forget()
    matrix_input_btn_cancel.grid_forget()


def show_number_input():  # показывает ввод числа
    global number_input_lbl, number_input_entry, number_input_btn_done, number_input_btn_cancel
    number_input_lbl.grid(row=0, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    number_input_entry.delete(0, END)
    number_input_entry.grid(row=1, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    number_input_btn_done.grid(row=2, column=1, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    number_input_btn_cancel.grid(row=2, column=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)


def close_number_input():  # показывает вывод числа
    global number_input_lbl, number_input_entry, number_input_btn_done, number_input_btn_cancel
    number_input_lbl.grid_forget()
    number_input_entry.grid_forget()
    number_input_btn_done.grid_forget()
    number_input_btn_cancel.grid_forget()


def show_matrix_output():  # показываем вывод итоговой матрицы
    global matrix_output_lbl, matrix_output_lbl_result, matrix_output_btn_done, rows_output, columns_output,\
        matrix_output
    matrix_output_lbl.config(text=f"Ваша итоговая матрица с размерами {rows_output} x {columns_output}:")
    matrix_output_lbl.grid(row=0, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    matrix_output_lbl_result.config(text=matrix_output)
    matrix_output_lbl_result.grid(row=1, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    matrix_output_btn_done.grid(row=2, column=2, ipadx=4, ipady=4, pady=6, sticky=NSEW)


def close_matrix_output():  # скрывает вывод итоговой матрицы
    global matrix_output_lbl, matrix_output_lbl_result, matrix_output_btn_done
    matrix_output_lbl.grid_forget()
    matrix_output_lbl_result.grid_forget()
    matrix_output_btn_done.grid_forget()


def handle_pressing_menu_btn_1(event):
    close_menu()
    show_matrix_size_input()

def handle_pressing_menu_btn_2(event):
    close_menu()

def handle_pressing_menu_btn_3(event):
    close_menu()

def handle_pressing_menu_btn_4(event):
    close_menu()

def handle_pressing_menu_btn_5(event):
    close_menu()

def handle_pressing_menu_btn_6(event):
    close_menu()

def handle_pressing_matrix_size_input_btn_done(event):
    global rows_input, columns_input, columns_input_entry
    # !!! пока предположим, что пользователь действительно что-то ввёл
    rows_input, columns_input = rows_input_entry.get(), columns_input_entry.get()
    close_matrix_size_input()
    show_matrix_input()


def handle_pressing_matrix_size_input_btn_cancel(event):
    close_matrix_size_input()
    show_menu()


def handle_pressing_matrix_input_btn_done(event):
    global matrix_input, matrix_input_text
    # !!! пока предположим, что пользователь ввел матрицу верно
    matrix_input = matrix_input_text.get("1.0", "end")
    close_matrix_input()
    show_number_input()

def handle_pressing_number_input_btn_done(event):
    global number_input, number_input_entry, matrix_output, rows_input, columns_input, matrix_input
    number_input = number_input_entry.get()
    close_number_input()
    # логика: передаем в модуль logic считанные от пользователя данные и получаем ответ
    matrix_output = logic.multiply_matrix_by_number(rows_input, columns_input, matrix_input, number_input)
    show_matrix_output()


def handle_pressing_number_input_btn_cancel(event):
    close_number_input()
    show_matrix_input()


def handle_pressing_matrix_input_btn_cancel(event):
    close_matrix_input()
    show_matrix_size_input()


def handle_pressing_matrix_output_btn_done(event):
    close_matrix_output()
    show_menu()


# создаём переменные, в которых будут лежать данные, которые считали от пользователя
# если операция будет производиться над одной матрицей
number_input, rows_input, columns_input, matrix_input = None, None, None, None
# если операция будет производиться над двумя матрицами
rows_1_input, columns_1_input, rows_2_input, columns_2_input = None, None, None, None
matrix_1_input, matrix_2_input = None, None

# создаём переменные, в которых будут лежать данные, которые будут выводиться пользователю
rows_output, columns_output = None, None
matrix_output = None

root = Tk()  # создаём окно и привязываем его переменной root
# через переменную root будем управлять атрибутами окна
root.title("Преобразования матриц")  # устанавливаем заголовок окна
root.geometry("1000x500")  # устанавливаем размеры окна

# о виджетах можно узнавать информацию через специальные методы, но чтобы это сделать, мы должны применить этот метод
root.update()  # без него все св-ва будут применены только при вызове метода .mainloop()
window_size_info = root.geometry()  # например, так мы узнаем размер окна, заданный ранее этим методом
# но в данной программе нам это не понадобится, это просто учебная информация

# создаём виджеты для меню - menu
# текстовая метка Label() для сообщения в меню выбора команд
menu_lbl = Label()
# можно указывать св-ва при создании в Label(), а можно установить их позже в методе .config()
menu_lbl.config(text="Выберите операцию из списка:")
# кнопки меню: позволят выбрать 6 преобразований матриц
menu_btn_1, menu_btn_2, menu_btn_3, menu_btn_4, menu_btn_5, menu_btn_6 = Button(), Button(), Button(),\
    Button(), Button(), Button()  # создаем кнопки
menu_btn_1.config(text="1. Умножение матрицы на число")
menu_btn_2.config(text="2. Транспонирование матрицы")
menu_btn_3.config(text="3. Проверка матрицы на симметричность")
menu_btn_4.config(text="4. Сложение двух матриц")
menu_btn_5.config(text="5. Вычитание двух матриц (из первой матрицы вычитается вторая)")
menu_btn_6.config(text="6. Умножение двух матриц (перед этим будет проверка на возможность умножения)")
# привязываем события к функциям-обработчикам событий
menu_btn_1.bind("<Button-1>", handle_pressing_menu_btn_1)
menu_btn_2.bind("<Button-1>", handle_pressing_menu_btn_2)
menu_btn_3.bind("<Button-1>", handle_pressing_menu_btn_3)
menu_btn_4.bind("<Button-1>", handle_pressing_menu_btn_4)
menu_btn_5.bind("<Button-1>", handle_pressing_menu_btn_5)
menu_btn_6.bind("<Button-1>", handle_pressing_menu_btn_6)

# виджеты для ввода размеров матрицы - matrix_size_input
matrix_size_input_lbl = Label()
matrix_size_input_lbl.config(text="Введите размеры матрицы (количество строк и столбцов):")
decorative_multiplication_sign = Label()
decorative_multiplication_sign.config(text="X")
rows_input_entry, columns_input_entry = Entry(), Entry()
rows_input_entry.config(justify=CENTER)
columns_input_entry.config(justify=CENTER)
matrix_size_input_btn_done, matrix_size_input_btn_cancel = Button(), Button()
matrix_size_input_btn_done.config(text="Готово")
matrix_size_input_btn_cancel.config(text="Назад")
matrix_size_input_btn_done.bind("<Button-1>", handle_pressing_matrix_size_input_btn_done)
matrix_size_input_btn_cancel.bind("<Button-1>", handle_pressing_matrix_size_input_btn_cancel)

# виджеты для ввода матрицы - matrix_input
matrix_input_text = Text()
matrix_input_lbl = Label()  # настраиваться текст будет в зависимости от размером матрицы
matrix_input_btn_done, matrix_input_btn_cancel = Button(), Button()
matrix_input_btn_done.config(text="Готово")
matrix_input_btn_cancel.config(text="Назад")
matrix_input_btn_done.bind("<Button-1>", handle_pressing_matrix_input_btn_done)
matrix_input_btn_cancel.bind("<Button-1>", handle_pressing_matrix_input_btn_cancel)

# виджеты для ввода числа - number_input
number_input_lbl = Label()
number_input_lbl.config(text="Введите число, на которое будет умножаться матрица:")
number_input_entry = Entry()
number_input_entry.config(justify=CENTER)
number_input_btn_done, number_input_btn_cancel = Button(), Button()
number_input_btn_done.config(text="Готово")
number_input_btn_cancel.config(text="Назад")
number_input_btn_done.bind("<Button-1>", handle_pressing_number_input_btn_done)
number_input_btn_cancel.bind("<Button-1>", handle_pressing_number_input_btn_cancel)

# виджеты для вывода матрицы - matrix_output
matrix_output_lbl = Label()  # настраиваться текст будет в зависимости от размером матрицы
matrix_output_lbl_result = Label()  # вывод матрицы в ответе
matrix_output_btn_done = Button()
matrix_output_btn_done.config(text="Готово")
matrix_output_btn_done.bind("<Button-1>", handle_pressing_matrix_output_btn_done)


# перехватываем событие закрытия окна: если нажат крестик, вызывается функция close_app()
root.protocol("WM_DELETE_WINDOW", close_app)

set_grid()
show_menu()
root.mainloop()  # отображаем окно и запускаем цикл обработки событий окна для взаимодействия c пользователем
