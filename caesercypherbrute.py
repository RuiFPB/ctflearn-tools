txt = input("Texto a descriptografar: ")
abc = 'abcdefghijklmnopqrstuvwxyz'
ABC = abc.upper()

print("Opções: ")
for i in range(27):
    newmsg = ""
    for c in txt:
        if c in abc:
            pos = abc.find(c)
            newpos = (pos - i) % 26
            newc = abc[newpos]
            newmsg += newc
        elif c in ABC:
            pos = ABC.find(c)
            newpos = (pos - i) % 26
            newc = ABC[newpos]
            newmsg += newc
        else:
            newmsg += c
    print(i, newmsg)