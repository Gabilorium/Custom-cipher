import random
import string

## CONSTANTES:
SIMBOLOS = ['$', '<', '-', '>', '&']
SEED = 42
CANTIDAD_SIMBOLOS_LETRA = 3
CANT_CARACTERES_A_CONVERTIR = len(string.ascii_lowercase)

random.seed(SEED)
diccionario = {}


for i in range (CANT_CARACTERES_A_CONVERTIR):
    letra_a_codificar = string.ascii_lowercase[i]
    letra_codificada = ""
    print("Letra = %a" %(letra_a_codificar))
    for j in range(CANTIDAD_SIMBOLOS_LETRA):
        letra_codificada = letra_codificada + random.choice(SIMBOLOS)
        diccionario[letra_a_codificar] = letra_codificada
        


for clave, valor in diccionario.items():
    print(clave, valor)