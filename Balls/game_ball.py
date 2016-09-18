import tkinter # импорт модуля ткиннтер

def button1_command():
    print("button 1 default command")

def print_hello(event):
    #print("Hello!")
    #print(dir(event)) #dir - это функция показывающая любые возможности об объекте
    #print(event.char)
    #print(event.delta)
    #print(event.height)
    #print(event.keycode)
    #print(event.keysym)
    ##print(event.keysym_num)
    print(event.num)
    #print(event.send_event)
    #print(event.serial)
    #print(event.state)
    #print(event.time)
    #print(event.type)
    print(event.widget)
    #print(event.width)
    print(event.x)
    print(event.y)
    #print(event.x_root)
    #print(event.y_root)
    me = event.widget
    if me == button1:
        print("Hello!")
    elif me == button2:
        print("Press button 2")
    else:
        raise ValueError()


root = tkinter.Tk() # создаем виджет главного окна

button1 = tkinter.Button(root, text="Кнопка 1", command=button1_command) #создаем виджеты внутри виджета root, кнопка
button1.bind("<Button>", print_hello) #привязываем объекту обработчик
button1.pack() #упаковщик позиции объекта

button2 = tkinter.Button(root, text="Кнопка 2") #создаем виджеты внутри виджета root, кнопка
button2.bind("<Button>", print_hello) #привязываем объекту обработчик
button2.pack() #упаковщик позиции объекта

root.mainloop()