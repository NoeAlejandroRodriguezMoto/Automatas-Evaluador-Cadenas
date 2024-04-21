# Noé Alejandro Rodríguez Moto - 221219 - Automata de cadenas - 7 - "A"

import re

DIGITO = "[0-9]"
OPERADOR = "(\+|\-|\*|\/)"
TABLA_TRANSICIONES = [[1,"E","E"],[1,2,"E"],[3,"E","E"],[3,2,"A"]]
FIN = ""

def clasificar_caracter(character):
    if(re.match(DIGITO, character)):
        return 0, "Digito"
    elif(re.match(OPERADOR, character)):
        return 1, "Operador"
    elif(character == FIN):
        return 2, "FND"
    else:
        print(f"Error el {character} no es valido")
        exit()

def imprimir_encabezado():
    print("|  Edo. Actual | Caracter |  Simbolo  |Edo. Siguiente |")
    imprimir_linea()

def imprimir_contenido(estadosig, character, simbolo, estado):
    print("|     {0:2}       |    {1:1}     | {2:<7}   |     {3:2}       |".format(estadosig, character, simbolo, estado))
    imprimir_linea()

def imprimir_linea():
    print("+--------------+----------+-----------+---------------+")

# MAIN
estado = 0

print ("""+---------------------------------------+
|    Introduce una cadena a evaluar:    |
+---------------------------------------+""")
cadena = input()
imprimir_linea()
imprimir_encabezado()

for character in cadena:
    estadosig = estado
    charcaracter, simbolo = clasificar_caracter(character)
    estado = TABLA_TRANSICIONES[estado][charcaracter]

    if (estado == "E"):
        imprimir_contenido(estadosig, character, simbolo, estado)
        print("""|              Cadena No Valida                       |
+-----------------------------------------------------+""")
        exit()
    imprimir_contenido(estadosig, character, simbolo, estado)

if(estado != 3):
    print("""|              Cadena No Valida                       |
+-----------------------------------------------------+""")
elif(estado == 3):
    imprimir_contenido(estado, ' ', 'FND', ' ')
    print("""|                Cadena Valida                        |
+-----------------------------------------------------+""")
    
# Cadenas probadas: validas: 12*3/4-5 y 6/3*2-1 no validas: 12++3 y 4/3--3