import os
import pathlib

import matplotlib.pyplot as plt
import numpy
import numpy as np
from PIL import Image

store = []
d = []
binary = []
cwd = os.getcwd()
print(cwd)
MNIST_path = os.path.join(cwd, 'MNIST_DS')
print(MNIST_path)
classes = os.listdir(MNIST_path)
opath = (MNIST_path, 0)
print(opath)

f = open("Barcode.txt", "w")
g = open("Address.txt", "w")
f.write("")
g.write("")
f.close()
g.close()


# w tells python we are opening the file to write into it
r = open("User.txt", "r")
path = r.readline()
print(path)

arr = np.array(Image.open(path))
A1 = numpy.sum(arr, axis=1)  # 0 degree projection

# Average for 0 degree projection
A1average = sum(A1) / len(A1)

# 90 Degree Projection
A2 = numpy.sum(arr, axis=0)

A2average = sum(A2) / len(A2)

# 45 Degree Projection
A3 = [np.trace(arr, offset=i) for i in range(-np.shape(arr)[0] + 2, np.shape(arr)[1] - 1)]

# 135 Degree projection
A3average = numpy.average(A3)

A4 = [np.trace(np.fliplr(arr), offset=i) for i in range(-np.shape(arr)[0] + 2, np.shape(arr)[1] - 1)]
A4average = numpy.average(A4)

B1 = []
B2 = []
B3 = []
B4 = []
h = []

# Converting to barcode(0 angle project array)
for k in range(len(A1)):
    if A1[k] <= A1average:
        B1.append(0)
    else:
        B1.append(1)
#print("B:", B1)

for r in range(len(A2)):
    if A2[r] <= A2average:
        B2.append(0)
    else:
        B2.append(1)
# print("B2:", B2)

for l in range(len(A3)):
    if A3[l] <= A3average:
        B3.append(0)
    else:
        B3.append(1)
#print("B3:", B3)

for y in range(len(A4)):
    if A4[y] <= A4average:
        B4.append(0)
    else:
        B4.append(1)
#print("B4:", B4)

AA = B1 + B2 + B3 + B4
print("User image barcode: ", AA)
print('\n')

possible = []
wantedpath = " "
maxH = 100
for c in classes:

    images_path = os.path.join(MNIST_path, c)
    print(images_path)
    for image_path in pathlib.Path(images_path).iterdir():
        path = image_path
        print(path)

        arr = np.array(Image.open(path))

        A1 = numpy.sum(arr, axis=1)  # 0 degree projection

        # Average for 0 degree projection
        A1average = sum(A1) / len(A1)

        # 90 Degree Projection
        A2 = numpy.sum(arr, axis=0)

        A2average = sum(A2) / len(A2)

        # 45 Degree Projection
        A3 = [np.trace(arr, offset=i) for i in range(-np.shape(arr)[0] + 2, np.shape(arr)[1] - 1)]

        # 135 Degree projection
        A3average = numpy.average(A3)

        A4 = [np.trace(np.fliplr(arr), offset=i) for i in range(-np.shape(arr)[0] + 2, np.shape(arr)[1] - 1)]
        A4average = numpy.average(A4)

        B1 = []
        B2 = []
        B3 = []
        B4 = []
        h = []
        f = open("Barcode.txt", "a")
        g = open("Address.txt", "a")
        # Converting to barcode(0 angle project array)
        for k in range(len(A1)):
            if A1[k] <= A1average:
                B1.append(0)
            else:
                B1.append(1)
        #print("B:", B1)

        for r in range(len(A2)):
            if A2[r] <= A2average:
                B2.append(0)
            else:
                B2.append(1)
        # print("B2:", B2)

        for l in range(len(A3)):
            if A3[l] <= A3average:
                B3.append(0)
            else:
                B3.append(1)
        #print("B3:", B3)

        for y in range(len(A4)):
            if A4[y] <= A4average:
                B4.append(0)
            else:
                B4.append(1)
        #print("B4:", B4)

        BB = B1 + B2 + B3 + B4
        f.write(str(BB) + "\n")
        g.write(str(path) + "\n")
        print(BB)
        h=0
        for x in range(len(AA)):
            if(AA[x]!=BB[x]):
                h=h+1 #hamming distance
        if h < maxH:
            maxH = h
            wantedpath = path
        if h == maxH:
            possible.append(str(wantedpath))
        # f.close()
        # g.close()

print("Closest: ", wantedpath)
print("Possible options could be: ")
m=0
while(m<len(possible)):
    print(possible[m])
    m+=1


