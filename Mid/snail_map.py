def snail(snail_map):
    side=len(snail_map)
    number=side**2
    array=[]
    circle=0
    cnt=0
    if not snail_map[0]:
        return array
    while True:
        i,j,k,l=circle,circle,side-1,side-1
        if (cnt+1)==number:
            array.append(snail_map[j][i])
            return array
        while i<side-1:
            if cnt==number:
                return array
            cnt+=1
            array.append(snail_map[j][i])
            i+=1
        if (cnt+1)==number:
            array.append(snail_map[j][i])
            return array
        while j<side-1:
            if cnt==number:
                return array
            cnt+=1
            array.append(snail_map[j][i])
            j+=1
        if (cnt+1)==number:
            array.append(snail_map[j][k])
            return array
        while k>circle:
            if cnt==number:
                return array
            cnt+=1
            array.append(snail_map[j][k])
            k-=1
        if (cnt+1)==number:
            array.append(snail_map[l][k])
            return array
        while l>circle:
            if cnt==number:
                return array
            cnt+=1
            array.append(snail_map[l][k])
            l-=1
        if cnt==number:
            return array
        side-=1
        circle+=1
        
array = [[1,2,3,4,5,6, 7],
         [24,25,26,27,28,29,8],
         [23,40,41,42,43,30,9],
         [22,39,48,49,44,31,10],
         [21,38,47,46,45,32,11],
         [20,37,36,35,5,33,12],
         [19,18,17,16,15,14,13]]

string=snail(array)
print(string)