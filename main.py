import numpy as np
import matplotlib.pyplot as plt

def find_one(mass):
    for i in range(len(mass)):
        for l in range(len(mass[i])):
            if mass[i][l] == 1:
                return np.array([i, l])
    return np.array([-1, -1])

for l in range(1, 7, 1):
    mass = []
    with open(f"figure{l}.txt") as f:
        size = f.readline().split()[0]
        f.readline()
        for i in f:
            mass.append(sum(map(int, i.split())))
        if max(mass) > 0:
            print(f"Номинальное разрешение файла: figure{l}.txt = {float(size)/max(mass)}")
        else:
            print(f"В файле: figure{l}.txt отсутствует изображение")



im1 = np.loadtxt('img1.txt', skiprows=2)
im2 = np.loadtxt('img2.txt', skiprows=2)

difference = find_one(im1) - find_one(im2)

print(f"\nСмещение 2-го изображения относительно 1-го равно {difference[1]} x и {difference[0]} y")







