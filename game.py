import tkinter
import random
from tkinter import Canvas
window = tkinter.Tk()

window.geometry('800x600')
window.title('Bable Hunter')

#сделай холст на все окно и сделать его цветной

canvas = Canvas(window, bg = 'blue', height=600, width=800)
canvas.pack()

# создаем фигуру круг

ball = canvas.create_oval(10,10, 100, 100, outline='white', fill='green')



def move_object(direction):
    
    if direction.keysym == 'Right':
        canvas.move(ball, 10, 0)
    elif direction.keysym == 'Left':
        canvas.move(ball, -10, 0)
    elif direction.keysym == 'Up':
        canvas.move(ball, 0, -10)
    elif direction.keysym == 'Down':
        canvas.move(ball, 0, 10)
    
window.bind('<Key>', move_object)





# import threading

class Bubble:
    def __init__(self, x, y, r, color):
        self.color = color
        self.r = r
        self.y = y
        self.x = x
        self.image = canvas.create_oval(
            self.x,
            self.y,
            self.x + self.r,
            self.y + self.r,
            outline=self.color
        )


bubbles = []
for i in range(5):
    bubbles.append(Bubble(
        random.randint(10, 800),
        random.randint(10, 600),
        random.randint(10, 30),
        'white'
    ))