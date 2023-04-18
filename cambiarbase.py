import unittest

def binariodecimal(numero):
    lista = []
    posicion = len(numero) - 1
    for d in numero:
        lista.append(int(d) * 2**posicion)
        posicion -= 1
    resp = sum(lista)
    return (resp)

def decimalbinario(numero):
    c = []
    while numero > 1:
        resultado = numero/2
        d = int(numero%2)
        c.append(str(d))
        numero = resultado
    r = int(numero)
    c.append(str(r))
    num = "".join(c[::-1])
    return (num)



if __name__ == "__main__":
    unittest.main()
