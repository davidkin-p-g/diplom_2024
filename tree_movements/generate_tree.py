import numpy as np
import random
import math
from PIL import Image, ImageDraw

# Функция для генерации случайных точек
def generate_random_points(num_points, map_size=(300, 300), margin=10):
    points = []
    while len(points) < num_points:
        x = random.randint(margin, map_size[0] - margin)
        y = random.randint(margin, map_size[1] - margin)
        points.append((x, y))
    return points

# Функция для добавления начальной и конечной точки
def add_start_end_points(points, start, end):
    points.insert(0, start)
    points.append(end)
    return points

# Функция для соединения точек
def connect_points(points, max_distance=50):
    connections = []
    num_points = len(points)
    for i in range(num_points):
        for j in range(i + 1, num_points):
            dist = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
            if dist <= max_distance:
                connections.append((points[i], points[j], dist))
    return connections

# Функция для фильтрации соединений
def filter_connections(connections, map_array):
    valid_connections = []
    for (p1, p2, dist) in connections:
        x1, y1 = p1
        x2, y2 = p2
        if not check_wall_collision(x1, y1, x2, y2, map_array):
            valid_connections.append((p1, p2, dist))
    return valid_connections

# Функция для проверки пересечения со стенами
def check_wall_collision(x1, y1, x2, y2, map_array):
    line = create_line(x1, y1, x2, y2)
    for (x, y) in line:
        if map_array[y, x] == 255:  # Проверка на наличие стены
            return True
    return False

# Функция для создания линии между двумя точками
def create_line(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    return points

# Функция для записи соединений в файл
def write_connections_to_file(connections, output_path):
    with open(output_path, 'w') as f:
        for (p1, p2, dist) in connections:
            f.write(f'connected loc-{p1[0]}-{p1[1]} loc-{p2[0]}-{p2[1]} {dist}\n')

# Функция для добавления стен на карту
def add_walls(map_array):
    walls = [
        ((50, 50), (250, 50)),
        ((100, 100), (100, 200)),
        ((150, 50), (150, 250)),
        ((50, 150), (250, 150))
    ]
    for (start, end) in walls:
        line = create_line(start[0], start[1], end[0], end[1])
        for (x, y) in line:
            for i in range(-2, 3):
                for j in range(-2, 3):
                    if 0 <= x + i < map_array.shape[1] and 0 <= y + j < map_array.shape[0]:
                        map_array[y + j, x + i] = 255
    return map_array

# Основная функция
def main():
    num_points = 100
    map_size = (300, 300)
    start_point = (20, 20)
    end_point = (280, 280)
    output_path = 'connections.txt'
    output_image = 'map.png'
    
    # Генерация случайных точек
    points = generate_random_points(num_points, map_size)
    points = add_start_end_points(points, start_point, end_point)
    
    # Создание карты и добавление стен
    map_array = np.zeros(map_size, dtype=np.uint8)
    map_array = add_walls(map_array)
    
    # Соединение точек
    connections = connect_points(points)
    valid_connections = filter_connections(connections, map_array)
    
    # Запись соединений в файл
    write_connections_to_file(valid_connections, output_path)
    
    # Визуализация точек и соединений
    map_image = Image.new('RGB', map_size, (255, 255, 255))
    draw = ImageDraw.Draw(map_image)
    
    # Рисуем соединения синим цветом
    for (p1, p2, dist) in valid_connections:
        draw.line([p1, p2], fill=(0, 0, 255), width=1)
    
    # Рисуем точки
    for point in points:
        color = (255, 0, 0)  # По умолчанию красный цвет для точек
        if point == start_point:
            color = (0, 255, 0)  # Зеленый для начальной точки
        elif point == end_point:
            color = (0, 0, 0)  # Черный для конечной точки
        draw.ellipse([point[0] - 2, point[1] - 2, point[0] + 2, point[1] + 2], fill=color)
    
    # Рисуем стены
    for y in range(map_size[1]):
        for x in range(map_size[0]):
            if map_array[y, x] == 255:
                draw.rectangle([x - 2, y - 2, x + 2, y + 2], fill=(0, 0, 0))
    
    # Сохраняем изображение
    map_image.save(output_image)

if __name__ == '__main__':
    main()
