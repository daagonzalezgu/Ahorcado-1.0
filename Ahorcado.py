import random

#Dibujos del tablero
tablero =[ """
    +---+
    |   |
        |
        |
        |
        |
   ======== """, """
   +---+
    |   |
    O   |
        |
        |
        |
   ======== """, """
    +---+
    |   |
    O   |
    |   |
        |
        |
   ======== """, """
    +---+
    |   |
    O   |
   /|   |
        |
        |
   ======== """, """
   +---+
    |   |
    O   |
   /|\  |
        |
        |
   ======== """, """
   +---+
    |   |
    O   |
   /|\  |
   /    |
        |
   ======== """, """
   +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
   ======== """
]

#Lista de palabras
palabras = ('azul', 'loza', 'amargo', 'calabaza', 'amorcito', 'pescado', 'elefante')

def seleccionar_palabra(palabras):
     palabra = random.randint(0,len(palabras)-1)
     return palabras[palabra]

#Dibujar tablero
def display(tablero,palabra_secreta, letra_correcta, letra_incorrecta):
     #Muestra el tablero con el ahorcado
     print(tablero[len(letra_incorrecta)])
     #Muestra las letras incorrectas hasta el momento
     print('Letras incorrectas: ', ' ')
     for letra in letra_incorrecta:
          print(letra,' ')
     


palabra_secreta = seleccionar_palabra(palabras)
letra_correcta = []
letra_incorrecta = ['a','b','c','d']
display(tablero,palabra_secreta,letra_correcta,letra_incorrecta)

#pedir una letra 
def dar_letra():
     letra = str(input())
#buscar la letra
#reemplazar en el tablero 
print(seleccionar_palabra(palabras))
#print(tablero[3])

#Bienvenida
     intro = """
     Ahorcado 1.0
     Bienvenid@ al menu principal
     ¿Estás list@ para empezar?
     """
#Seleccionar palabra
palabra_secreta = seleccionar_palabra(palabras)
letras_correctas = []
letras_incorrectas = []
while True:
     #dibujar tablero
     display(tablero, palabra_secreta, letra_correcta, letra_incorrecta)
     
     #Pedir letra
     #Buscar letra
          
     #Fin del juego ?
     #Preguntar si jugar de nuevo
