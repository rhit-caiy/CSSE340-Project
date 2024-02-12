import numpy as np
import matplotlib.pyplot as plt
from itertools import product
import random
# import time

wolfram_code=54
# random.seed(0)

rule={t:int(b) for t,b in zip(product((1,0),repeat=3),'{:08b}'.format(wolfram_code))}
print(wolfram_code,'{:08b}'.format(wolfram_code),rule)

n=100#number of cells
generation=100

#random cells
cells=[0]+random.choices([0,1],k=n)+[0]
# print(cells)
history=[cells]+[[0 for j in range(n+2)] for i in range(generation)]

# t1=time.time()
for g in range(1,generation+1):
    newcells=history[g]
    for i in range(n):
        newcells[i+1]=rule[tuple(cells[i:i+3])]
    cells=newcells
# t2=time.time()
# print(t2-t1,"s")
plt.imshow(np.array(history),cmap='gray',interpolation='nearest')
