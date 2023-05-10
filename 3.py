import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("roof.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width = image.size[0] #Определяем ширину
height = image.size[1] #Определяем высоту
pix = image.load() #Выгружаем значения пикселей

brightness = [0]*256 #список яркостей зелёного цвета

for x in range(width):
    for y in range(height):
        green = pix[x, y][1]
        brightness[green] += 1
relation = max(brightness)//512
for x in range(width):
    for y in range(height):
        a = pix[x, y][0]
        b = pix[x, y][1]
        c = pix[x, y][2]
        if x <= 511 and y <= 511 and y >= 511 - brightness[x//2] // relation:
            draw.point((x, y), (0, 255, 0))
        else:
            draw.point((x, y), (a, b, c))
image.show()
del draw
