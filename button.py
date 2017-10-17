import random
count = 0
for i in range(0,100) :
    # count = 0
    total = 0
    while(total<1) :
        total += random.uniform(0,1)
        count += 1
    # print(count)
print(count/100.0)
