import tkinter as tk

class Torpedo:
    def __init__(self, canvas, x, y, direction):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.direction = direction  # 'left' или 'right'
        self.speed = 10
        self.active = True
        
        # Просто рисуем прямоугольник
        self.id = canvas.create_rectangle(
            x - 15, y - 5,
            x + 15, y + 5,
            fill='orange',
            outline='red',
            width=2,
            tags='torpedo'
        )
    
    def move(self):
        """Движение торпеды"""
        if not self.active:
            return
            
        # Двигаем вправо или влево
        if self.direction == 'right':
            self.canvas.move(self.id, self.speed, 0)
            self.x += self.speed
        else:
            self.canvas.move(self.id, -self.speed, 0)
            self.x -= self.speed
        
        # Проверяем, не вышла ли за экран
        if self.x < -50 or self.x > 850:
            self.destroy()
    
    def destroy(self):
        """Удаление торпеды"""
        self.active = False
        self.canvas.delete(self.id)
    
    def get_coords(self):
        """Получение координат торпеды"""
        return self.canvas.coords(self.id)
    
    def check_hit(self, target_coords):
        """Проверка попадания в цель"""
        torpedo_coords = self.get_coords()
        if not torpedo_coords:
            return False
            
        # Простая проверка пересечения
        t_left, t_top, t_right, t_bottom = torpedo_coords
        tg_left, tg_top, tg_right, tg_bottom = target_coords
        
        # Если прямоугольники пересекаются
        if (t_left < tg_right and 
            t_right > tg_left and 
            t_top < tg_bottom and 
            t_bottom > tg_top):
            return True
        return False