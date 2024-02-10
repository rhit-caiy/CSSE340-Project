import numpy as np
import matplotlib.pyplot as plt
from itertools import product
# import random

wolfram_code=170
# random.seed(0)

rule={t:int(b) for t,b in zip(product((0,1),repeat=3),'{:08b}'.format(wolfram_code))}
# print(wolfram_code,'{:08b}'.format(wolfram_code),rule)

s="1234567890qwertyuiopasdfghjklzxcvbnmαāДд≈‱∫√？⠀⚛☻"
print(s)
messagechar=[i for i in map(ord,s)]

message=[]
for m in messagechar:
    message+=list(map(int,'{:016b}'.format(m)))
print("".join(map(str,message)))

n=len(message)#number of cells

generation=300

#random cells
cells=message
# print(cells)
history=[cells]+[[0 for j in range(n)] for i in range(generation)]

for g in range(1,generation+1):
    newcells=history[g]
    for i in range(1,n-1):
        newcells[i]=rule[tuple(cells[i-1:i+2])]
    newcells[0]=rule[tuple(cells[-1:]+cells[:2])]
    newcells[-1]=rule[tuple(cells[-2:]+cells[:1])]
    cells=newcells
plt.imshow(np.array(history),cmap='gray',interpolation='nearest')
out="".join(map(str,cells))

outstr=""

for i in range(n//16):
    outstr+=chr(int("".join(out[16*i:16*i+16]),2))
print(outstr)


