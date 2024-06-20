import random


# Глубина просмотра в секундах от и до:
min_deep_view = 60
max_deep_view = 70
deep_view = random.randint(min_deep_view, max_deep_view)


#Полный путь до chromedriver
path = '/home/haspro/PycharmProjects/views_booster_for_rutube/chromedriver/chromedriver'


#Ссылка на видео
url = 'https://rutube.ru/video/4b3878793d12f5fcc8adf3bb3b1a4023/'


#Количество одновреммено работающих процессов
max_workers = 2


