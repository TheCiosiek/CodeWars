def snail(snail_map):
    #dlugość boku
    side=len(snail_map)
    #ilość wszystkich wartości
    number=side**2
    array=[]
    circle=0
    #zlicza ilość wykonań, żeby był równy ilości wartości
    cnt=0
    if not snail_map[0]:
        return array
    while True:
        #Przechodzi bo bokach, aż nie zostanie na boku jednego miejsca. Od tego miejsca kolejny bok zaczyna żeby na końcu zrobić koło. Przechodzi do kolejnego kwadratu o 1 w prawo/dół (circle) i 1 w lewo/górę (side)
#       I I I J
#       L I J J
#       L L K J
#       L K K K
        i,j,k,l=circle,circle,side-1,side-1
        if (cnt+1)==number:
            array.append(snail_map[j][i])
            return array
        #Górny bok
        while i<side-1:
            cnt+=1
            array.append(snail_map[j][i])
            i+=1
        if (cnt+1)==number:
            array.append(snail_map[j][i])
            return array
        #Prawy bok
        while j<side-1:
            cnt+=1
            array.append(snail_map[j][i])
            j+=1
        if (cnt+1)==number:
            array.append(snail_map[j][k])
            return array
        #Dolny bok
        while k>circle:
            cnt+=1
            array.append(snail_map[j][k])
            k-=1
        if (cnt+1)==number:
            array.append(snail_map[l][k])
            return array
        #Lewy bok
        while l>circle:
            cnt+=1
            array.append(snail_map[l][k])
            l-=1
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




# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# expected = [1,2,3,6,9,8,7,4,5]
# test.assert_equals(snail(array), expected)


# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# expected = [1,2,3,4,5,6,7,8,9]
# test.assert_equals(snail(array), expected)


#Rozwiązanie z użyciem nampy, niefektywne, bo żongluje całą tablicą.
#import numpy as np

#def snail(array):
#    m = []
#    array = np.array(array)
#    while len(array) > 0:
#        m += array[0].tolist()
#        array = np.rot90(array[1:])
#    return m


"""
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

This image will illustrate things more clearly:

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array[[]].
"""
"HELLO WORLD2"
