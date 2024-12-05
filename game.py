import random


def opciones(usuario,pc):
    print(f"usuario: {usuario}, pc: {pc}")
    if usuario == pc:
        print("Empate")
    elif usuario == "piedra" and pc == "papel":
        print(f"{pc} gana a {usuario}. Gana la pc")
    elif usuario == "papel" and pc == "tijeras":
        print(f"{pc} gana a {usuario}. Gana la pc")
    elif usuario == "tijeras" and pc == "piedra":
        print(f"{pc} gana a {usuario}. Gana la pc")
    else:
        print(f"{usuario} gana a {pc}. Gana el usuario")

def pc_analiza(eleccion):
    choose =["piedra","papel","tijeras"]
    for n in choose:
        if eleccion == n:
            return random.choice(choose)
    return False
    
def run_game():
    contador = 0
    usr_count = 0#
    pc_count = 0# busca añadir un contador para visualizar al final quien gano, ademas podriamos programar que se este borrando y limpiando la pantalla cada vez
     
    while(contador < 3):
        eleccion = input("Elige piedra, papel o tijeras: ")
        eleccion = eleccion.lower()
        pc = pc_analiza(eleccion)
        if pc == False:
            continue
        else:
            print("")
            print(f"Round {contador+1}")
            opciones(eleccion,pc)
            contador+=1
        
        
            


run_game()






