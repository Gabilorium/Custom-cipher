import random
import string

SIMBOLOS = ['$', '<', '-', '>', '&']
SEED = 42
CANTIDAD_SIMBOLOS_LETRA = 3
random.seed(SEED)


print('Letras de %s simbolos'%(CANTIDAD_SIMBOLOS_LETRA))
letra_nueva = ""
for i in range(CANTIDAD_SIMBOLOS_LETRA):
    letra_nueva = letra_nueva + random.choice(SIMBOLOS)

print("Letra = %a" %(letra_nueva))