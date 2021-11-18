def first_non_repeating_letter(string):
    dict={}
    i=0
    while i<len(string):
        a=string[i].lower()
        if a in dict:
            dict[a][0]+=1
        else: dict[a]=[1, string[i]]
        i+=1
    for key in dict:
        if dict[key][0]==1:
            return dict[key][1]
    return ''