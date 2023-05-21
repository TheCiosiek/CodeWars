def DNA_strand(dna):
    j=0
    dnaStrand=[0]*(len(dna))
    for i in dna:
        dnaStrand[j]=i
        j+=1
    j=0
    for i in dnaStrand:
        if i=='A':
            dnaStrand[j]='T'
        elif i=='C':
            dnaStrand[j]='G'
        elif i=='T':
            dnaStrand[j]='A'
        else:
            dnaStrand[j]='C'
        j+=1
    str_dna=''
    for i in dnaStrand:
        str_dna+=i
    return str_dna
    
    """
    import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))
    # Python 3.4 solution || you don't need to import anything :)
    # return dna.translate(str.maketrans("ATCG","TAGC"))
    
    pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])
    
    
    Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more: http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

Example: (input --> output)

"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
"""
