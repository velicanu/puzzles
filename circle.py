a = [] 
for i in range(1,101) :
    a.append(i) 

killed = 0
sword = 0
while( killed < 100 ) :
    sword+=1
    if(sword>99) :
        sword=0
    while ( a[sword]==0 ) :
        sword+=1
        if(sword>99) :
            sword = 0
    a[sword]=0
    print(sword+1,killed)
    while ( a[sword]==0 ) :
        sword+=1
        if(sword>99) :
            sword = 0
    killed+=1
    
    
    
