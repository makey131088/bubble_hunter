import tkinter
import os
from PIL import ImageTk, Image
from PIL.Image import Transpose

class Submarine:
    canvas: tkinter.Canvas
    image: int
    __image_path: str = os.path.join(os.getcwd(), 'submarine.png')
    
    def __init__(self, canvas):
        self.canvas = canvas
        
        # Загружаем оригинал
        image_file = Image.open(self.__image_path)
        image_file = image_file.resize((100, 100), resample=Image.Resampling.LANCZOS)
        
        # Создаем сразу два варианта: обычный и отзеркаленный
        self._image_src_right = ImageTk.PhotoImage(image_file)
        self._image_src_left = ImageTk.PhotoImage(image_file.transpose(Transpose.FLIP_LEFT_RIGHT))
        
        # Добавляем движение верх и вниз
        self._image_src_up = ImageTk.PhotoImage(image_file.rotate(90))
        self._image_src_down = ImageTk.PhotoImage(image_file.rotate(-90))
        # Создаем объект на холсте, по умолчанию смотрим вправо
        self.image = self.canvas.create_image(200, 200, image=self._image_src_right)
    
    def move(self, event):
        if event.keysym == 'Right':
            self.canvas.move(self.image, 10, 0)
            # Меняем картинку на "правую"
            self.canvas.itemconfig(self.image, image=self._image_src_right)
        elif event.keysym == 'Left':
            self.canvas.move(self.image, -10, 0)
            # Меняем картинку на "левую"
            self.canvas.itemconfig(self.image, image=self._image_src_left)
        elif event.keysym == 'Up':
            self.canvas.move(self.image, 0, -10)
            self.canvas.itemconfig(self.image, Image = self._image_src_up)
        elif event.keysym == 'Down':
            self.canvas.move(self.image, 0, 10)
            self.canvas.itemconfig(self.image, Image = self._image_src_down)