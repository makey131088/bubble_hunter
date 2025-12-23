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