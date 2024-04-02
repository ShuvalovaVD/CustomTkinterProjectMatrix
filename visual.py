import logic  # импортируем наш модуль с логикой
from tkinter import *  # импортируем модуль tkinter
from tkinter.messagebox import *  # пока не изучено, опробовано лишь на практике!


def close_app():  # пока не изучено, опробовано лишь на практике!
    ans = askyesno(title="Выход", message="Вы ходите закрыть программу?")
    if ans:
        root.destroy()  # закрываем окно


def show_menu():  # показывает меню выбора операций над матрицами
    global menu_btn_1, menu_btn_2, menu_btn_3, menu_btn_4, menu_btn_5, menu_btn_6, menu_message
    # для позиционирования используем метод .grid(), который рисует сетку, в которой размещает виджеты
    rows, columns = 7, 5
    for i in range(rows):
        root.rowconfigure(index=i, weight=1)
    for i in range(columns):
        root.columnconfigure(index=i, weight=1)
    menu_message.grid(row=0, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    menu_btn_1.grid(row=1, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    menu_btn_2.grid(row=2, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    menu_btn_3.grid(row=3, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    menu_btn_4.grid(row=4, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    menu_btn_5.grid(row=5, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    menu_btn_6.grid(row=6, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)


def close_menu():  # скрывает меню
    global menu_btn_1, menu_btn_2, menu_btn_3, menu_btn_4, menu_btn_5, menu_btn_6, menu_message
    menu_message.grid_forget()
    menu_btn_1.grid_forget()
    menu_btn_2.grid_forget()
    menu_btn_3.grid_forget()
    menu_btn_4.grid_forget()
    menu_btn_5.grid_forget()
    menu_btn_6.grid_forget()

def show_matrix_size_input():  # показывает ввод размеров матрицы
    global matrix_size_message, rows_input, columns_input, decorative_mult_mark, matrix_size_btn_done
    rows, columns = 3, 5
    for i in range(rows):
        root.rowconfigure(index=i, weight=1)
    for i in range(columns):
        root.columnconfigure(index=i, weight=1)
    matrix_size_message.grid(row=0, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    rows_input.grid(row=1, column=1, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    decorative_mult_mark.grid(row=1, column=2, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    columns_input.grid(row=1, column=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)
    matrix_size_btn_done.grid(row=2, column=1, columnspan=3, ipadx=4, ipady=4, pady=6, sticky=NSEW)


def close_matrix_size_input():  # скрывает ввод размеров матрицы
    global matrix_size_message, rows_input, columns_input, decorative_mult_mark, matrix_size_btn_done
    matrix_size_message.grid_forget()
    rows_input.grid_forget()
    columns_input.grid_forget()
    decorative_mult_mark.grid_forget()
    matrix_size_btn_done.grid_forget()


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

def handle_pressing_matrix_size_btn_done(event):
    close_matrix_size_input()
    show_menu()


root = Tk()  # создаём окно и привязываем его переменной root
# через переменную root будем управлять атрибутами окна
root.title("Преобразования матриц")  # устанавливаем заголовок окна
root.geometry("1000x500")  # устанавливаем размеры окна

# о виджетах можно узнавать информацию через специальные методы, но чтобы это сделать, мы должны применить этот метод
root.update()  # без него все св-ва будут применены только при вызове метода .mainloop()
window_size_info = root.geometry()  # например, так мы узнаем размер окна, заданный ранее этим методом
# но в данной программе нам это не понадобится, это просто учебная информация

# создаём виджеты для меню
# текстовая метка Label() для сообщения в меню выбора команд
menu_message = Label()
# можно указывать св-ва при создании в Label(), а можно установить их позже в методе .config()
menu_message.config(text="Выберите операцию из списка:")
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

# создаём виджеты для ввода размеров матрицы
matrix_size_message = Label()
matrix_size_message.config(text="Введите размеры матрицы через пробел (количество строк и столбцов):")
decorative_mult_mark = Label()
decorative_mult_mark.config(text="X")
rows_input, columns_input = Entry(), Entry()
rows_input.config(justify=CENTER)
columns_input.config(justify=CENTER)
matrix_size_btn_done = Button()
matrix_size_btn_done.config(text="Готово")
matrix_size_btn_done.bind("<Button-1>", handle_pressing_matrix_size_btn_done)

# перехватываем событие закрытия окна: если нажат крестик, вызывается функция close_app()
root.protocol("WM_DELETE_WINDOW", close_app)

show_menu()
root.mainloop()  # отображаем окно и запускаем цикл обработки событий окна для взаимодействия c пользователем
