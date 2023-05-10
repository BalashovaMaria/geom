import math
import random
from PIL import Image, ImageDraw  # Подключим необходимые библиотеки


def one(i: int):
    if i > 100:
        return 100
    return i


image1 = Image.open("winter.jpg")  # Открываем изображение
image2 = Image.open("park.jpg")
draw = ImageDraw.Draw(image1)  # Создаем инструмент для рисования
width = image1.size[0]  # Определяем ширину
height = image1.size[1]  # Определяем высоту
pix1 = image1.load()  # Выгружаем значения пикселей
pix2 = image2.load()

steps = width / 3 / 2
length = width / 3 / steps
st = -1

for x in range(width):
    if width / 3 <= x < width * 2 / 3 and x % length == 0:
        st += 1
        print(st)
    for y in range(height):
        a1 = pix1[x, y][0]
        b1 = pix1[x, y][1]
        c1 = pix1[x, y][2]
        a2 = pix2[x, y][0]
        b2 = pix2[x, y][1]
        c2 = pix2[x, y][2]
        if x < width // 3:
            draw.point((x, y), (a2, b2, c2))
        elif x < width * 2 // 3:
            draw.point((x, y), (int((st * a1 / steps + (steps - st) / steps * a2)),
                                int((st * b1 / steps + (steps - st) / steps * b2)),
                                int((st * c1 / steps + (steps - st) / steps * c2))))
        else:
            draw.point((x, y), (a1, b1, c1))

image1.show()
del draw
