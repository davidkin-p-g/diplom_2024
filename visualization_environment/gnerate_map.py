import re
import numpy as np
from PIL import Image, ImageDraw
import math

# Функция для чтения .wtb файла
def read_wtb_file(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
    return data

# Функция для извлечения информации о стенах
def parse_wtb_data(data):
    walls = []
    wall_pattern = re.compile(r'Wall\s*{[^}]*}')
    translation_pattern = re.compile(r'translation\s*([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)')
    rotation_pattern = re.compile(r'rotation\s*([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)')
    size_pattern = re.compile(r'size\s*([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)')
    
    wall_matches = wall_pattern.findall(data)
    
    for wall in wall_matches:
        translation_match = translation_pattern.search(wall)
        rotation_match = rotation_pattern.search(wall)
        size_match = size_pattern.search(wall)
        
        if translation_match and rotation_match and size_match:
            translation = tuple(map(float, translation_match.groups()))
            rotation = tuple(map(float, rotation_match.groups()))
            size = tuple(map(float, size_match.groups()))
            walls.append((translation, rotation, size))
    return walls

# Функция для создания 2D карты
def create_2d_map(walls, map_size=(300, 300), scale=100):
    map_array = np.zeros(map_size, dtype=np.uint8)
    map_image = Image.new('L', map_size, 0)
    draw = ImageDraw.Draw(map_image)
    
    for (translation, rotation, size) in walls:
        x = int(translation[0] * scale)
        y = int(translation[1] * scale)
        width = int(size[0] * scale)
        height = int(size[1] * scale)
        angle = rotation[3]
        
        # Преобразование координат и поворот
        cos_angle = math.cos(angle)
        sin_angle = math.sin(angle)
        
        half_width = width / 2
        half_height = height / 2
        
        points = [
            (x + half_width * cos_angle - half_height * sin_angle,
             y + half_width * sin_angle + half_height * cos_angle),
            (x - half_width * cos_angle - half_height * sin_angle,
             y - half_width * sin_angle + half_height * cos_angle),
            (x - half_width * cos_angle + half_height * sin_angle,
             y - half_width * sin_angle - half_height * cos_angle),
            (x + half_width * cos_angle + half_height * sin_angle,
             y + half_width * sin_angle - half_height * cos_angle)
        ]
        
        draw.polygon(points, fill=255)
    
    return map_image

# Функция для сохранения 2D карты в PNG файл
def save_2d_map(map_image, output_path):
    map_image.save(output_path)

# Основная функция
def main():
    file_path = 'word.wbt'
    output_path = 'output_map.png'
    
    data = read_wtb_file(file_path)
    walls = parse_wtb_data(data)
    map_image = create_2d_map(walls)
    save_2d_map(map_image, output_path)

if __name__ == '__main__':
    main()