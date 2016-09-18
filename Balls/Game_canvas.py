import tkinter

def paint(event):
    """
    Обработчик событий для холста
    :param event:
    :return:
    """
    print(event.x, event.y)
    if event.widget != canvas:
        print("Такого не должно быть")
        return
    canvas.coords(line, 0, 0, event.x, event.y)

root = tkinter.Tk()

canvas = tkinter.Canvas(root, background="deeppink", width=400, height=400)
canvas.bind("<Motion>", paint)
canvas.pack()

line = canvas.create_line(0, 0, 10, 10)
for i in range(10):
    oval = canvas.create_oval(5+i*40, 5+i*40, i*40+30, i*40+30, fill="black", width=3)

root.mainloop()
print("Вы вышли из приложения")