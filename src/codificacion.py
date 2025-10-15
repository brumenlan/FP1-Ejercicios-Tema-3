ALFABETO = "abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"

def letra_a_posicion(caracter: str) -> int:
    if caracter not in ALFABETO:
        return None
    return ALFABETO.find(caracter)

def posicion_a_letra(posicion: int) -> str:
    if 0 <= posicion < len(ALFABETO):
        return ALFABETO[posicion]
    else:
        return None

def cifra_cesar(texto: str, clave: int) -> str:
    res = ""
    for c in texto:
        if c in ALFABETO:
            posicion = letra_a_posicion(c)
            posicion_codificada = (posicion + clave) % len(ALFABETO)
            c = posicion_a_letra(posicion_codificada)
        res += c
    return res

print(cifra_cesar("Este es un texto de prueba", 19))
print(cifra_cesar("WFGw wF Hü GwKGB vw CEHwts", -19))