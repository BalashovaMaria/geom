import random
from PIL import Image, ImageDraw  # Подключим необходимые библиотеки

image = Image.open("roof.jpg")  # Открываем изображение
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
width = image.size[0]  # Определяем ширину
height = image.size[1]  # Определяем высоту
pix = image.load()  # Выгружаем значения пикселей

for x in range(width):
    for y in range(height):
        a = pix[x, y][0]
        b = pix[x, y][1]
        c = pix[x, y][2]
        m = (a + b + c) // 3
        gray = 0 if m <= 43 else 85 if m <= 127 else \
            170 if m <= 212 else 255
        draw.point((x, y), (gray, gray, gray))

image.show()
del draw
