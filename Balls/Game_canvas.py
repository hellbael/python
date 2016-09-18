import tkinter
from random import choice, randint

ball_initial_number = 30
ball_minimal_radius = 15
ball_maximal_radius = 40
ball_avaliable_colors = ["green", "blue", "yellow", "black", "pink", "grey", "brown", "red", "orange"]

def click_ball(event):
    """
    Обработчик событий для холста canvas
    :param event: событие с координатами клика
    По клику мышки нужно удалить тот объект, на который указывает мышка,
    а также засчитывать его в очки пользователя
    """
    #print(event.x, event.y)
    #if event.widget != canvas:
    #    print("Такого не должно быть")
    #    return
    #canvas.coords(line, 0, 0, event.x, event.y)
    #for obj in canvas:
    obj = canvas.find_closest(event.x, event.y)
    x1, y1, x2, y2 = canvas.coords(obj)
    if x1 <= event.x <= x2 and y1 <= event.y <= y2:
        canvas.delete(obj)
        create_random_ball()

def move_all_balls(event):
    """
        Передвигаем все шарики
    :return:
    """
    for obj in canvas.find_all():
        dx = randint(-1, 1)
        dy = randint(-1, 1)
        canvas.move(obj, dx,dy)

def create_random_ball():
    """
    Создаем шарик в случайном месте холста, при этом шарик не выходит за границы холста,
    при этом шарик не выходит за границы холста
    :return:
    """
    R = randint(ball_minimal_radius, ball_maximal_radius)
    x =  randint(0, int(canvas['width'])-1-2*R)
    y = randint(0, int(canvas['height'])-1-2*R)

    canvas.create_oval(x, y, x+2*R, y+2*R, fill=random_color(), width=3)

def random_color():
    """
    Возвращает рандомный цвет из набора цветов
    :return:
    """
    return choice(ball_avaliable_colors)

def init_ball_catch_game():
    """
    Создаем необходимое для игры количество шариков, по которым нужно будет кликать
    """
    for i in range(ball_initial_number):
        create_random_ball()

def init_main_window():
    global root, canvas

    root = tkinter.Tk()

    canvas = tkinter.Canvas(root, background="deeppink", width=400, height=400)
    canvas.bind("<Button>", click_ball)
    canvas.bind("<Motion>", move_all_balls)
    #canvas.move_all_balls()
    canvas.pack()

    #line = canvas.create_line(0, 0, 10, 10)
    #for i in range(10):

if __name__ == "__main__":
    init_main_window()
    init_ball_catch_game()
    root.mainloop()
    print("Приходите играть еще!")