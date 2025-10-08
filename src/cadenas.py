def invierte_cadena(cadena: str) -> str:
    '''
    Recibe una cadena y la devuelve invertida
    '''
    resultado = ""
    for caracter in cadena:
        resultado = caracter + resultado
    return resultado

print(invierte_cadena("Hola"))