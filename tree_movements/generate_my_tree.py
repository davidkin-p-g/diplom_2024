import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance_matrix
import cv2


def is_free(x, y, map_array):
    """ Проверка, свободна ли точка """
    return map_array[x, y] == 255


def generate_points(num_points, map_array):
    """ Генерация случайных точек на карте, исключая стены """
    points = [(10, 10), (290, 290)]  # Добавляем начальную и конечную точки в список
    attempts = 0

    while len(points) < num_points + 2 and attempts < num_points * 10:
        x, y = np.random.randint(0, map_array.shape[0]), np.random.randint(0, map_array.shape[1])
        if is_free(x, y, map_array):
            points.append((x, y))
        attempts += 1
    return np.array(points)

def connect_points(points, map_array):
    """ Создание связей между точками, исключая связи через стены """
    dists = distance_matrix(points, points)
    connections = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if not intersects_wall(points[i], points[j], map_array):
                connections.append((points[i], points[j]))
    return connections

def intersects_wall(p1, p2, map_array):
    """ Проверка пересечения линии между точками p1 и p2 со стеной """
    line = np.linspace(p1, p2, num=100)  # Линейная интерполяция между двумя точками
    for (x, y) in line:
        if not is_free(int(x), int(y), map_array):
            return True
    return False

def main(map_array, num_points=40):
    points = generate_points(num_points, map_array)
    connections = connect_points(points, map_array)
    
    # Визуализация
    plt.imshow(map_array.T, cmap='gray', origin='lower')
    plt.scatter(*zip(*points), c='blue')  # точки
    for conn in connections:
        plt.plot(*zip(*conn), c='green')  # связи
    plt.show()
    
    # Сохранение связей
    with open('connections.txt', 'w') as f:
        for (p1, p2) in connections:
            f.write(f'connected loc-{p1[0]}-{p1[1]} loc-{p2[0]}-{p2[1]}\n')


if __name__ == '__main__':
    word_size =(300,300)
    word_array = np.zeros(word_size)
    word_array = np.full_like(word_array, 255)



    word = {
    'Wall_1' : {
    'translation': [1.5, -2.5],
    'size': [0.03, 1],
    'rotation' : 0,
    },
    'Wall_2' : {
    'translation': [1.5, -0.5],
    'size': [0.03, 1],
    'rotation' : 0,
    },
    'Wall_3' : {
    'translation': [0.5, -1.5],
    'size': [0.03, 1],
    'rotation' :  90,
    },
    'Wall_4' : {
    'translation': [2.7, -2],
    'size': [0.03, 0.6],
    'rotation' : 90,
    },
    }
    # j - x ||||| i - y

    def translate_position(mass):
        mass[0] = int(mass[0]*100)
        mass[1] = int(-mass[1]*100)
        return mass

    for i in range(300):
        for j in range(300):
            if i == 0 or i == 299:
                word_array[i][j] = 0
                print(i,j)
            if j == 0 or j ==  299:
                word_array[i][j] = 0
                print(i,j)

                    

    print('Wall 1:')
    x = int(word['Wall_1']['translation'][0] * 100)
    y = int(word['Wall_1']['translation'][1] * 100)
    y = -y
    size_x = int(word['Wall_1']['size'][0] * 100)
    size_y = int(word['Wall_1']['size'][1] * 100)
    print(x - size_x / 2)
    print(x, y, size_x, size_y)
    for i in range(300):
        for j in range(300):
            if x - size_x / 2 < j < x + size_x / 2 :
                if y - size_y / 2 < i < y + size_y / 2 :
                    word_array[i][j] = 0


    print('------')


    print('Wall 2:')
    x = int(word['Wall_2']['translation'][0] * 100)
    y = int(word['Wall_2']['translation'][1] * 100)
    y = -y
    size_x = int(word['Wall_2']['size'][0] * 100)
    size_y = int(word['Wall_2']['size'][1] * 100)
    print(x - size_x / 2)
    print(x, y, size_x, size_y)
    for i in range(300):
        for j in range(300):
            if x - size_x / 2 < j < x + size_x / 2 :
                if y - size_y / 2 < i < y + size_y / 2 :
                    word_array[i][j] = 0


    print('------')


    print('Wall 3:')
    x = int(word['Wall_3']['translation'][0] * 100)
    y = int(word['Wall_3']['translation'][1] * 100)
    y = -y
    # 90 rotation -> size_x = size_y; size_y = size_x;
    size_y = int(word['Wall_3']['size'][0] * 100)
    size_x = int(word['Wall_3']['size'][1] * 100)
    print(x - size_x / 2)
    print(x, y, size_x, size_y)
    for i in range(300):
        for j in range(300):
            if x - size_x / 2 < j < x + size_x / 2 :
                if y - size_y / 2 < i < y + size_y / 2 :
                    word_array[i][j] = 0


    print('------')


    print('Wall 4:')
    x = int(word['Wall_4']['translation'][0] * 100)
    y = int(word['Wall_4']['translation'][1] * 100)
    y = -y
    # 90 rotation -> size_x = size_y; size_y = size_x;
    size_y = int(word['Wall_4']['size'][0] * 100)
    size_x = int(word['Wall_4']['size'][1] * 100)
    print(x - size_x / 2)
    print(x, y, size_x, size_y)
    for i in range(300):
        for j in range(300):
            if x - size_x / 2 < j < x + size_x / 2 :
                if y - size_y / 2 < i < y + size_y / 2 :
                    word_array[i][j] = 0


    print('------')

    # print('add ball')
    # a = [1.05, -0.81]
    # a = translate_position(a)
    # print(a)
    # word_array[a[1]][a[0]] = 0


    cv2.imwrite(f'word_image.jpg', word_array)

    np.savetxt('file.txt', word_array, fmt="%d")
    #map_size = 300
    #map_array = np.zeros((map_size, map_size))
    # Пример стены (для теста)
    #map_array[150:160, :] = 255  
    # Пример начальной и конечной точек
    word_array[10, 10] = 1
    word_array[290, 290] = 2
    main(word_array)