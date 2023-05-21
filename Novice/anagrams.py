def anagrams(word, words):
    dict1,dict2,anagrams={},{},[]
    for i in word:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    for word1 in words:
        for letter in word1:
            if letter in dict2:
                dict2[letter]+=1
            else:
                dict2[letter]=1
        if dict1==dict2:
            anagrams.append(word1)
        dict2.clear()
    return anagrams