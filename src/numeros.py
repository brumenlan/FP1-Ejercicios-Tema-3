def invierte_numero(n: int) -> int:
    res = 0
    negativo = n < 0
    n = abs(n)
    while n != 0:
        res = res * 10 + n%10
        n = n // 10
    if negativo:
        return -res
    else:
        return res
    
def convierte_binario(n: int) -> str:
    res = ""
    if n == 0:
        return "0"
    while n > 0:
        res = str(n % 2) + res
        n //= 2
    return res

def sumar_divisores_propios(n:int) -> int:
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

def clasifica_numero(n: int) -> str:
    suma = sumar_divisores_propios(n)
    if n == suma:
        return "Perfecto"
    elif n < suma:
        return "Abundante"
    else:
        return "Deficiente"

def clasifica_rango(n: int) -> None:
    for i in range(1, n+1):
        print(f"{i} : {clasifica_numero(i)}")

def busca_perfecto(n: int) -> int:
    '''Devuelve el número perfecto n-ésimo, siendo el 1 el primero'''
    numero = 0
    contador = 0

    while contador < n:
        numero += 1
        if clasifica_numero(numero) == "Perfecto": #sumar_divisores(numero) == n
            contador +=1
    return numero