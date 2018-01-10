def reverse(input=''):
    number = len(input)-1
    strRe=''
    while number >= 0:
        strRe+=input[number]
        number-=1;
    print(strRe)
    return  strRe
