#Used for https://ctflearn.com/challenge/227
#To decrypt q{vpln'bH_varHuebcrqxetrHOXEj


def strtobin(instr):
    """Converts a string to a list of the binary\
representations of each character"""
    binlst = []
    for c in instr:
        binlst.append(format(ord(c), 'b')) #check https://www.tutorialspoint.com/How-to-convert-string-to-binary-in-Python

    # we need 8 bits for each character
    for B in binlst:
        if B.__len__() == 8:
            pass
        else:
            binlst[binlst.index(B)] = ('0' * (8 - B.__len__())) + B
    return binlst

# Code stolen from https://www.geeksforgeeks.org/convert-binary-to-string-using-python/
def bintodec(binary):
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal

def bintostr(binary):
    str_data = ''
    for i in range(0, len(binary), 8):
        temp_data = int(binary[i:i + 8])
        decimal_data = bintodec(temp_data)
        str_data += chr(decimal_data)
    return str_data
# End of stolen code

def xorbrute(lst1):
    '''I'm not going to explain this, fuck you future me!!!'''
    lst_tmp = []
    newlst = []
    tmpB = ''
    answr = ''

    # generates all possible 8bit xor keys
    for i in range(256):
        lst_tmp.append(bin(i))
    
    # removes the 0b prefix
    for i in range(lst_tmp.__len__()):
        lst_tmp[i] = lst_tmp[i][2:]

    # ensures that each key is 8 chars long (for ex.: the first key is 0b0 that gets to 0 and here to 00000000)
    for B in lst_tmp:
        if B.__len__() == 8:
            pass
        else:
            lst_tmp[lst_tmp.index(B)] = ('0' * (8 - B.__len__())) + B

    # xor all possible keys with each element from the list given by strtobin()
    for poss in lst_tmp:    
        for B in lst1:
            for i in range(8):
                tmpB += str(int(B[i]) ^ int(poss[i])) 
            newlst.append(tmpB)
            tmpB = ''
        binary = ''.join(newlst[b] for b in range(newlst.__len__()))
        print('\n' + bintostr(binary))
        newlst = []        
        answr = input('is this correct? [s/n]')
        # if the given text is readable, stop; else continue xor
        if answr == 's':
            print("The xor key was 0b" + poss)
            return
        else:
            pass

xorbrute(strtobin(input("String: ")))

