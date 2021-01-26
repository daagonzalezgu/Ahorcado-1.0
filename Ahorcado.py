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

