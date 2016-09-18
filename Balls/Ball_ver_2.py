import tkinter # импорт модуля ткиннтер


def button1_command():
    print("button 1 default command")


def print_hello(event):
    print(event.num)
    print(event.widget)
    print(event.x)
    print(event.y)
    me = event.widget
    if me == button1:
        print("Hello!")
    elif me == button2:
        print("Press button 2")
    else:
        raise ValueError()


def init_main_window():
    """
    Инициализация главного окна, создание всех объектов и их упаковка
    :return:
    """

    global root, button1, button2, label, text, scale
    root = tkinter.Tk()  # создаем виджет главного окна

    button1 = tkinter.Button(root, text="Кнопка 1", command=button1_command)  # создаем виджеты внутри виджета root, кнопка
    button1.bind("<Button>", print_hello)  # привязываем объекту обработчик

    button2 = tkinter.Button(root, text="Кнопка 2")  # создаем виджеты внутри виджета root, кнопка
    button2.bind("<Button>", print_hello)  # привязываем объекту обработчик

    variable = tkinter.IntVar(0)
    label = tkinter.Label(root, textvariable=variable)
    scale = tkinter.Scale(root, orient=tkinter.HORIZONTAL, length=300, from_=0, to=100, tickinterval=10, resolution=5, variable=variable)
    text = tkinter.Entry(root, textvariable = variable)
    for obj in button1, button2, label, text, scale:
        obj.pack()


if __name__ == "__main__":
    init_main_window()

    root.mainloop()
