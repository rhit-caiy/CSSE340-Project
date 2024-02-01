import numpy as np
import time
import matplotlib.pyplot as plt
n=1000
# np.random.seed(0)
p=0.75#probability of initial living
generation=1000

grid=np.random.choice(2, n**2, p=[p,1-p]).reshape(n, n)
# grid=np.random.randint(0,2,size=(n,n))#random with p=0.5

img=plt.imshow(grid, cmap='gray', interpolation='nearest')

t1=time.time()
for g in range(generation):
    neighbour_pad = np.pad(grid,((1,1),(1,1)),'constant')
    neighbour_num=neighbour_pad[0:-2,1:-1]+neighbour_pad[2:,1:-1]+neighbour_pad[1:-1,0:-2]+neighbour_pad[1:-1,2:]+neighbour_pad[0:-2,0:-2]+neighbour_pad[0:-2,2:]+neighbour_pad[2:,0:-2]+neighbour_pad[2:,2:]
    grid=(neighbour_num==3)|(grid&(neighbour_num==2))
    #update plot
    img.set_data(grid)
    plt.pause(0.001)
t2=time.time()
print(t2-t1)
# plt.imshow(grid, cmap='gray', interpolation='nearest')
# plt.show()