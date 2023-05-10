import random
from PIL import Image, ImageDraw  # Подключим необходимые библиотеки

image = Image.open("roof.jpg")  # Открываем изображение
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
width = image.size[0]  # Определяем ширину
height = image.size[1]  # Определяем высоту
pix = image.load()  # Выгружаем значения пикселей

err = 0
dY = 0
step = (width - height) / width

for x in range(width):
    err += step
    if err >= 0.5:  # упрощённый алгоритм Брезенхема
        dY += 1
        err -= 1

    for y in range(height):
        a = pix[x, y][0]
        b = pix[x, y][1]
        c = pix[x, y][2]
        if (x >= y + dY and x >= height - y + dY and x >= width // 2) or \
                (x <= y + dY and x <= height - y + dY and x < width // 2):
            draw.point((x, y), (255, 0, 255))
        else:
            draw.point((x, y), (a, b, c))
image.show()
del draw
