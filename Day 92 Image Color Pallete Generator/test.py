import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

path = './static/Screenshot_from_2024-11-01_11-27-40.png'
picture = Image.open(path)
pic_array = np.array(picture)
rows = pic_array.shape[0]
columns = pic_array.shape[1]
print(rows)
list =[]
a = np.array([1,1,1])
b = np.array([2,2,2])
c = pic_array[0,0,0:3]
d = np.array([1,2,3])
list.append(a)
list.append(b)
list.append(c)
print(list)
print(np.any(np.all(np.array([1,1,1]) == list, axis=1)))
print(np.any(np.all(np.array([1,2,3]) == list, axis=1)))
print(np.any(np.all(pic_array[0,0,0:3] == list, axis=1)))
print(np.all(pic_array[0,0,0:3] != list, axis=1))
count=0

for i in range(0,rows):
    for j in range(0,columns):
        if np.any(np.all(pic_array[i,j,0:3] == list, axis=1)):
            list.append(pic_array[i,j,0:3])
            print('hello')
