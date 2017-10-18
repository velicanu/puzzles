import numpy as np
import matplotlib.pyplot as plt

x = []
for i in range(0,52) :
    x.append((-1)**i)
amax = []
for j in range(0,10000) :
    np.random.shuffle(x)
    max = 0
    sum = 0
    for i in x :
        sum+=i
        if(sum>max) :
            max = sum
    amax.append(max)

print(np.median(amax))
# myhist = plt.hist(amax,10,(0,10))
# plt.show()
            
