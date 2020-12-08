import base64

opc = input("Encode or Decode? [E/D]: ").lower()

if opc == "e":
    txt = input("Texto para encode: ")
    out = base64.encodebytes(txt.encode()).decode()
    print("Texto encoded:", out)

elif opc == "d":
    txt = input("Texto para decode: ")
    out = base64.decodebytes(txt.encode()).decode()
    print("Texto decoded:", out)
