def invierte_cadena(cadena: str) -> str:
    '''
    Recibe una cadena y la devuelve invertida
    '''
    resultado = ""
    for caracter in cadena:
        resultado = caracter + resultado
    return resultado

print(invierte_cadena("Hola"))

def es_palindromo(cadena: str, ignora_espacios: bool, ignora_mayusculas: bool) -> bool:
    if ignora_espacios:
        cadena = cadena.replace(" ", "")
    if ignora_mayusculas:
        cadena = cadena.lower()
    inversa = invierte_cadena(cadena)
    return cadena == inversa

print(es_palindromo("Yo hago yoga hoy", True, True))

def estiliza_mensaje(cadena:str, alterna_may_min: bool = True) -> str:
    res = ""
    pos = 0
    for c in cadena:
        if alterna_may_min:
            if c.isalpha():
                if pos % 2 == 0:
                    c = c.upper()
                else:
                    c = c.lower()
                pos += 1
        res += c

def estiliza_mensaje2(cadena:str, alterna_may_min: bool = True) -> str: #, usa_dieresis: bool = False, sustituye_espacios: str = " "
    res = ""
    siguiente_mayuscula = True
    for c in cadena:
        if alterna_may_min:
            if c.isalpha():
                if siguiente_mayuscula:
                    c = c.upper()
                else:
                    c = c.lower()
                siguiente_mayuscula = not siguiente_mayuscula
        res += c