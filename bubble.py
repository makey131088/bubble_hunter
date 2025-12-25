import tkinter
from random import randint
class Bubble:
    
    
    def __init__(self, canvas, x, y, r, color):
        self.canvas = canvas
        self.color = color
        self.r = r
        self.y = y
        self.x = x
        self.speed = randint(1, 15)
        self.image = self.canvas.create_oval(
            self.x,
            self.y,
            self.x + self.r,
            self.y + self.r,
            outline=self.color
        )
        
    def __del__(self):
        self.canvas.delete(self.image)
        
    def move(self):
        self.canvas.move(self.image,randint(-2, 2),-self.speed)
        x1, y1, x2, y2 = self.canvas.coords(self.image)
        # при достижении верхней границы помещаем пузырь под нижний край окна
        if y2 < 0:
            window_height = self.canvas.winfo_height()
            self.canvas.move(self.image, 0, window_height + randint(10, 20))
        
        # при достижении верхней границы отдвигаем пузырь в область видимости
        window_width = self.canvas.winfo_width()
        if x2 > window_width:
            self.canvas.move(self.image, -self.r, 0)
        elif x2 < 0:
            self.canvas.move(self.image, self.r, 0)