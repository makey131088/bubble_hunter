import tkinter
import random
from threading import Thread
from tkinter import Tk, Canvas
from submarine import Submarine
from bubble import Bubble
from time import sleep
window = Tk()

window.geometry('800x600')

window.title('Bubble Hunter')

#сделай холст на все окно и сделать его цветной

canvas = Canvas(window, bg = 'blue', height=600, width=800)
window.focus_set()
canvas.pack()

# добавляем объект подводной лодки 
submarine = Submarine(canvas)


# import threading

bubbles = []
for i in range(5):
    bubbles.append(Bubble(
        canvas,
        random.randint(10, 800),
        random.randint(10, 600),
        random.randint(10, 30),
        'white'
    ))
    
window.bind('<Key>', submarine.move)

def move_bubble():
    while True:
        for buble in bubbles:
            buble.move()
        sleep(.1)

Thread(
    target=move_bubble,
    daemon=True
).start()



window.mainloop()












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