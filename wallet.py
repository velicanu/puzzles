a = [0] # expected value of change
total = 0 
for i in range(1,51) :
    penny = 1-i
    if i > 0:            # draw a penny, repeat for X-1
        penny = a[i-1] 
    nickle = 5-i
    if i > 4:            # draw a nickle, repeat for X-5 or give 5-X change
        nickle = a[i-5]
    dime = 10-i
    if i > 9:            # draw a dime, repeat for X-10 or give 10-X change
        dime = a[i-10]
    quarter = 25-i
    if i > 24:           # draw a quarter, repeat for X-25 or give 25-X change
        quarter = a[i-25]
        
    a.append(0.25*(penny + nickle + dime + quarter))  # equal probability of drawing each coin
    total+=a[i]
    print(i,a[i],total/i)
    
