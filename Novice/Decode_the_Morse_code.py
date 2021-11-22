def decodeMorse(morse_code):
    begin=0
    i=0
    spaceCnt=0
    morse_code+=" "
    morse_code_decode=""
    word=""
    while i<len(morse_code):
        try:
            if ord(morse_code[i]) in range (44,47):
                if spaceCnt==3 and begin==1:
                    morse_code_decode+=" "
                spaceCnt=0
                word+=morse_code[i]
                i+=1
                begin=1
            else:
                spaceCnt+=1
                i+=1
            if spaceCnt==1:
                morse_code_decode+=MORSE_CODE[word]
                word=""
        except KeyError:
            pass
    return morse_code_decode
