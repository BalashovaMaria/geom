import math
import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("winter.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width = image.size[0] #Определяем ширину
height = image.size[1] #Определяем высоту
pix1 = image.load() #Выгружаем значения пикселей

rad = min(height, width)//2
part = math.ceil(rad/3/100)

for x in range(width):
    for y in range(height):
        a = pix1[x, y][0]
        b = pix1[x, y][1]
        c = pix1[x, y][2]
        if (x - width // 2) ** 2 + (y - height // 2) ** 2 <= (rad*2//3) ** 2:
            draw.point((x, y), (a, b, c))

        elif (x - width // 2) ** 2 + (y - height // 2) ** 2 <= rad ** 2:
            rel = (math.sqrt((x - width // 2) ** 2 + (y - height // 2) ** 2)
                    - (rad * 2 // 3)) / (rad - (rad * 2 // 3))
            draw.point((x, y), (int((rel * 255 + (1 - rel) * a)),
                                int((rel * 255 + (1 - rel) * b)),
                                int((rel * 255 + (1 - rel) * c))))

        else:
            draw.point((x, y), (255, 255, 255))

image.show()
del draw
