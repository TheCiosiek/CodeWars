import numpy as np

def simplify(poly):
    print(poly)
    #Zrób tablicę wszystkich wielomianów
    plus, minus = make_array(poly)
    
    #Pobiera numery z początku i przenosi je do odddzielnych komórek
    plus = get_num(plus)
    minus = get_num(minus)

    #Sortuje stringi w tablicach
    plus = sort(plus)
    minus = sort(minus)

    #Wykonuje obliczenia
    plus, minus = solve(plus, minus)


    #Łączy tablic i zmienianie ich na numpy
    for i in range (len(minus[0])):
        plus[0].append(minus[0][i])
        plus[1].append(-abs(minus[1][i]))
    plus[1] = list(map(str, plus[1]))

    #Sortowanie tablicy przez rząd z wielomianami
    arr = zip(*plus)
    arr = list(sorted(arr ,key=lambda x: (len(x[0]), x[0])))

    #Składa do wyniku
    poly_s = ""
    poly_s = make_string(arr, poly_s)

    return poly_s

def toString(s):
    return str(s)

def make_string(array, poly_s):
    if not array[0]:
        return poly_s
    if int(array[0][1]) == 0:
        pass
    elif not poly_s:
        if abs(int(array[0][1])) == 1:
            if int(array[0][1]) == -1:
                poly_s += '-'
            poly_s += array[0][0]
        else:
            poly_s+=array[0][1]
            poly_s += array[0][0]

    for i in range(1, len(array)):
        if int(array[i][1]) == 0:
            pass
        elif abs(int(array[i][1])) == 1:
            if int(array[i][1]) == -1:
                poly_s += '-'
            else:
                poly_s += '+'
            poly_s += array[i][0]
        else:
            if int(array[i][1]) > 0:
                 poly_s+='+'
            poly_s+=array[i][1]
            poly_s += array[i][0]
    
    return poly_s
        
def solve(plus, minus):
    length_p = len(plus[0])
    length_m = len(minus[0])

    #Wykonuje obliczenia
    i=0
    while True:
        if i >= length_p:
                break
        j= i + 1
        while True:
            if j >= length_p:
                break
            if i == j:
                # j+=1
                continue
            else:
                #Sprawdź czy istnieje inny taki sam wielomian
                if plus[0][i] == plus[0][j]:
                    #Dodaj do innego wielomianu ilość tego
                    plus[1][i] = plus[1][i] + plus[1][j]

                    #Usuń ten wielomian
                    del plus[0][j]
                    del plus[1][j]
                    j = j - 1
                    length_p = length_p - 1
            j+=1
        j= 0
        while True:
            if j >= length_m:
                break
            #Sprawdź czy istnieje inny taki sam wielomian
            if plus[0][i] == minus[0][j]:
                #Odejmij ilość wielomianu od tego
                plus[1][i] = plus[1][i] - minus[1][j]

                #Usuń ten wielomian
                del minus[0][j]
                del minus[1][j]
                j = j - 1
                length_m = length_m - 1
            j+=1
        i+=1

    i=0
    while True:
        if i >= length_m:
                break
        j = i + 1
        while True:
            if j >= length_m:
                break
            if i == j:
                continue
            else:
                #Sprawdź czy istnieje inny taki sam wielomian
                if minus[0][i] == minus[0][j]:
                    #Dodaj do innego wielomianu ilość tego
                    minus[1][i] = minus[1][i] + minus[1][j]

                    #Usuń ten wielomian
                    del minus[0][j]
                    del minus[1][j]
                    j = j - 1
                    length_m = length_m - 1
            j+=1
        i+=1
    return plus, minus

def sort(array):
    cnt=0
    for arr in array[0]:
        array[0][cnt]= ''.join(sorted(arr))
        cnt+=1
    return array

def make_array(poly):
    plus = [[],[]]
    minus = [[],[]]
    buff_s = ""
    buff_char = ''
    wasMinus = False
    wasPlus = False
    i = len(poly)
    for l in poly:

        if l == "-":
            if buff_s:
                if wasMinus:
                    minus[0].append(buff_s)
                else:
                    plus[0].append(buff_s)
                buff_s = ""
            wasMinus = True
            continue
            
        if l == '+':
            if buff_s:
                if wasMinus:
                    minus[0].append(buff_s)
                else:
                    plus[0].append(buff_s)
                buff_s = ""
            wasMinus = False
            continue
        
        buff_s += l

    if wasMinus:
        minus[0].append(buff_s)
    else:
        plus[0].append(buff_s)

    return plus, minus
        

def get_num(array):
    cnt = 0
    cnt2=0
    buff_s = ""
    for arr in array[0]:
        for i in arr:
            if ord(i) in range (48, 58):
                cnt2+=1
                buff_s= buff_s + i
                array[0][cnt] = arr[cnt2:]
            else:
                if buff_s:
                    array[1].append(int(buff_s))
                else:
                    array[1].append(1)
                buff_s = ""
                cnt2=0
                break
        cnt+=1
    return array


print(simplify("5y+11ab-z-ab+4y-4z"))

# Description:

# When we attended middle school were asked to simplify mathematical expressions like "3x-yx+2xy-x" (or usually bigger), and that was easy-peasy ("2x+xy"). But tell that to your pc and we'll see!

# Write a function: simplify, that takes a string in input, representing a multilinear non-constant polynomial in integers coefficients (like "3x-zx+2xy-x"), and returns another string as output where the same expression has been simplified in the following way ( -> means application of simplify):

#     All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, e.g.:

#     "cb+cba" -> "bc+abc", "2xy-yx" -> "xy", "-a+5ab+3a-c-2a" -> "-c+5ab"

#     All monomials appears in order of increasing number of variables, e.g.:

#     "-abc+3a+2ac" -> "3a+2ac-abc", "xyz-xz" -> "-xz+xyz"

#     If two monomials have the same number of variables, they appears in lexicographic order, e.g.:

#     "a+ca-ab" -> "a-ab+ac", "xzy+zby" ->"byz+xyz"

#     There is no leading + sign if the first coefficient is positive, e.g.:

#     "-y+x" -> "x-y", but no restrictions for -: "y-x" ->"-x+y"

# N.B. to keep it simplest, the string in input is restricted to represent only multilinear non-constant polynomials, so you won't find something like `-3+yx^2'. Multilinear means in this context: of degree 1 on each variable.

# Warning: the string in input can contain arbitrary variables represented by lowercase characters in the english alphabet.