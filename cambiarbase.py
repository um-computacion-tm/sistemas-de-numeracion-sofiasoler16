import unittest

def binariodecimal(numero):
    lista = []
    posicion = len(numero) - 1
    for d in numero:
        lista.append(int(d) * 2**posicion)
        posicion -= 1
    resp = sum(lista)
    return (resp)

def binariohexa(numero):
    diccnum = {"0000": 0, "0001":1, "0010":2, "0011": 3, "0100": 4, "0101": 5, "0110": 6, "0111":7, "1000":8, "1001":9, "1010":"A", "1011":"B", 
               "1100":"C", "1101":"D", "1110":"E", "1111":"F"}
    
    d = numero.split(" ")

    fin = []
    for c in d:
        for x, v in diccnum.items():
            if c == x:
                fin.append(str(v))


    result = "".join(fin)
    return result

def binariooctal(numero):
    diccnum = {"000": 0, "001":1, "010":2, "011": 3, "100": 4, "101": 5, "110": 6, "111":7}

    d = numero.split(" ")
    print (d)
    fin = []
    for c in d:
        for x, v in diccnum.items():
            if c == x:
                fin.append(str(v))
                print (fin)

    result = "".join(fin)
    return result
print (binariooctal("001 011 111"))


def decimalbinario(numero):
    c = []
    while numero > 1:
        resultado = numero/2
        d = int(numero%2)
        c.append(str(d))
        numero = resultado
    r = int(numero)
    if r == 0:
        False
    else:
        c.append(str(r))
    num = "".join(c[::-1])
    return (num)

def decitohexa(numero):
    c = []
    while numero > 1:
        resultado = numero/16
        d = int(numero%16)
        letras = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
        for t, x in letras.items():
            if t == d:
                c.append(str(x))
                print (c)
        c.append(str(d))
        numero = resultado

    r = int(numero)
    if r == 0:
        False
    else: 
        c.append(str(r))
    if "A" in c:
        c.remove("10")
    if "B" in c:
        c.remove("11")
    if "C" in c:
        c.remove("12")
    if "D" in c:
        c.remove("13")
    if "E" in c:
        c.remove("14")
    if "F" in c:
        c.remove("15")
    num = "".join(c[::-1])
    return num

def decitoocta(numero):
    c = []
    while numero > 1:
        resultado = numero/8
        d = int(numero%8)
        c.append(str(d))
        numero = resultado
    r = int(numero)
    if r == 0:
        False
    else:
        c.append(str(r))
    num = "".join(c[::-1])
    return (num)

if __name__ == "__main__":
    unittest.main()
