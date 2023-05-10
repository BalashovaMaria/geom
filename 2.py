import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("roof.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width = image.size[0] #Определяем ширину
height = image.size[1] #Определяем высоту
pix = image.load() #Выгружаем значения пикселей
for x in range(width):
    for y in range(height):
        a = pix[x, y][0]
        b = pix[x, y][1]
        c = pix[x, y][2]
        if x <= width // 3:
            draw.point((x, y), ((a+b) // 2, (a + b) // 2, 0))
        elif x <= width * 2 // 3:
            draw.point((x, y), (a, 0, 0))
        else:
            draw.point((x, y), (0, b, 0))
image.show()
del draw
