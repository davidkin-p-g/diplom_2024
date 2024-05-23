import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance_matrix
import cv2
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