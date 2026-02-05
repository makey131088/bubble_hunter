import tkinter as tk
import random
from threading import Thread
from tkinter import Tk, Canvas
from submarine import Submarine
from bubble import Bubble
from time import sleep
from torpedo import Torpedo

class Game:
    def __init__(self):
        self.window = tk.Tk()
        self.setup_window()
        self.setup_canvas()
        self.setup_game()
        
    def setup_window(self):
        self.window.title("Bubble Hunter")
        self.window.geometry("900x700")
        
    def setup_canvas(self):
        self.canvas = tk.Canvas(self.window, bg='blue', width=900, height=700)
        self.canvas.pack()
        self.canvas.focus_set()
        
    def setup_game(self):
        # Создаём лодку
        self.submarine = Submarine(self.canvas)
        
        # Создаём пузыри
        self.bubbles = []
        for i in range(10):
            bubble = Bubble(
                self.canvas,
                random.randint(50, 750),
                random.randint(50, 550),
                random.randint(20, 40),
                'white'
            )
            self.bubbles.append(bubble)
        
        # Привязываем клавиши
        self.canvas.bind('<Key>', self.on_key_press)
        self.canvas.bind('<space>', self.on_space_press)  # Пробел для стрельбы
        
        # Запускаем игровой цикл
        self.game_loop()
    
    def on_key_press(self, event):
        """Управление лодкой"""
        self.submarine.move(event)
    
    def on_space_press(self, event):
        """Стрельба торпедой"""
        torpedo = self.submarine.shoot()
        if torpedo:
            print("Выстрел! Осталось торпед:", self.submarine.torpedo_count)
    
    def game_loop(self):
        
        # Обновляем торпеды
        self.submarine.update_torpedoes()
        
        # Проверяем попадания
        self.check_collisions()
        
        # Двигаем пузыри
        for bubble in self.bubbles:
            bubble.move()
        
        # Перезапускаем цикл
        self.window.after(50, self.game_loop)
    
    def check_collisions(self):
        # Проверка столкновений торпед с пузырями"
        for torpedo in self.submarine.torpedoes:
            if not torpedo.active:
                continue
                
            # Проверяем каждый пузырь
            for bubble in self.bubbles[:]:
                bubble_coords = bubble.canvas.coords(bubble.image)
                if bubble_coords and torpedo.check_hit(bubble_coords):
                    print("Попадание!")
                    
                    # Удаляем пузырь
                    bubble.canvas.delete(bubble.image)
                    self.bubbles.remove(bubble)
                    
                    # Уничтожаем торпеду
                    torpedo.destroy()
                    
                    # Создаём новый пузырь
                    new_bubble = Bubble(
                        self.canvas,
                        random.randint(50, 750),
                        600,
                        random.randint(20, 40),
                        'white'
                    )
                    self.bubbles.append(new_bubble)
                    break
    
    def run(self):
        self.window.mainloop()

# Запуск игры
if __name__ == "__main__":
    game = Game()
    game.run()












# установили pip install pillow библеотека
#  python3 -m venv .venv создание виртуального окружения
# deactivate выключить виртуальное окружение
# source .venv/bin/activate включить виртуальное окружение
# pip freeze > requirements.txt не помню что это)))

# занятие 23.12.2025
# sudo systemctl start ssh.service
# ifconfig чтобы узнать ip
# ssh-keygen -t ed25519
# cd .ssh переход в папку ssh
#  отреть общественный ключ cat bubble
# создать репозиторий
# генерирую пару ключей
# создать в домашней папке пользователя
# публичный ключ в 