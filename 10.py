import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("roof.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width = image.size[0] #Определяем ширину
height = image.size[1] #Определяем высоту
pix = image.load() #Выгружаем значения пикселей

freq = 18
step = width // (2 * freq)
move = 0

for x in range(width):
    if x % step == 0:
        move += 1
    for y in range(height):
        a = pix[x, y][0]
        b = pix[x, y][1]
        c = pix[x, y][2]

        if (x - width // 2) ** 2 + (y - height // 2) ** 2 <= 250 ** 2:
            draw.point((x, y), (255, 127, 0))

        elif height // 2 - 250 <= y <= height // 2 + 250 and move % 2 == 1:
            draw.point((x, y), (127, 255, 0))

        else:
            draw.point((x, y), (a, b, c))
image.show()
del draw
