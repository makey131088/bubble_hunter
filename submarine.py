import tkinter
import os
from PIL import ImageTk, Image
from PIL.Image import Transpose
from torpedo import Torpedo

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
        self.torpedoes = []
        self.torpedo_count = 5
    
    def shoot(self):
        if self.torpedo_count <= 0:
            return None
        
        x, y = self.get_position()
        torpedo = Torpedo(self.canvas, x, y, self.direction)
        self.torpedoes.append(torpedo)
        self.torpedo_count -= 1
        return torpedo
    
    def update_torpedoes(self):
        for torpedo in self.torpedoes[:]:
            torpedo.move()
            if not torpedo.active:
                self.torpedoes.remove(torpedo)

    def get_position(self):
        coords = self.canvas.coords(self.image)
        if coords:
            return coords[0], coords[1]
        return 200, 200
    
    def direction(self):
        return self.direction

    
    def move(self, event):
        x1, y1, x2, y2 = self.canvas.bbox(self.image)  # Получаем координаты объекта
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
    
        if event.keysym == 'Right' and x2 < canvas_width:
            self.canvas.move(self.image, 10, 0)
            self.canvas.itemconfig(self.image, image=self._image_src_right)
        elif event.keysym == 'Left' and x1 > 0:
            self.canvas.move(self.image, -10, 0)
            self.canvas.itemconfig(self.image, image=self._image_src_left)
        elif event.keysym == 'Up' and y1 > 0:
            self.canvas.move(self.image, 0, -10)
        elif event.keysym == 'Down' and y2 < canvas_height:
            self.canvas.move(self.image, 0, 10)