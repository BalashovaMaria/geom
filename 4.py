import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("roof.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width = image.size[0] #Определяем ширину
height = image.size[1] #Определяем высоту
pix = image.load() #Выгружаем значения пикселей
green = [0]*256
red = [0]*256
blue = [0]*256
gray = [0]*256
for x in range(width):
    for y in range(height):
        red[pix[x, y][0]] += 1
        green[pix[x, y][1]] += 1
        blue[pix[x, y][2]] += 1
relation1 = max(green) // 512
relation2 = max(red) // 512
relation3 = max(blue) // 512
for i in range(255):
    gray[i] += (red[i] + green[i] + blue[i]) // 3
for x in range(width):
    for y in range(height):
        a = pix[x, y][0]
        b = pix[x, y][1]
        c = pix[x, y][2]
        if x <= 511 and y <= 511 and y >= 511 - green[x//2] // relation1:
            draw.point((x, y), (0, 255, 0))
        elif x >= width // 2 and x <= width // 2 + 511 and y >= 511 - red[(x - width // 2) // 2] // relation2 and y <= 511:
            draw.point((x, y), (255, 0, 0))
        elif x >= width // 2 and x <= width // 2 + 511 and y >= height - blue[(x - width // 2) // 2] // relation3:
            draw.point((x, y), (0, 0, 255))
        elif x <= 511 and y >= height - gray[x // 2] // relation3:
            draw.point((x, y), (192, 192, 192))
        else:
            draw.point((x, y), (a, b, c))

image.show()
del draw
