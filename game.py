import random
import os

def opciones(usuario,pc):
    if usuario == pc:
        return None
    elif usuario == "piedra" and pc == "papel":
        return True
    elif usuario == "papel" and pc == "tijeras":
        return True
    elif usuario == "tijeras" and pc == "piedra":
        return True
    else:
        return False

def user_analiza(eleccion):
    choose =["piedra","papel","tijeras"]
    for n in choose:
        if eleccion == n:
            return random.choice(choose)
    return False
    
def run_game():
    contador = 0
    usr_count = 0
    pc_count = 0
     
    while(contador < 3):
        print("")
        usuario = input("Elige piedra, papel o tijeras: ")
        usuario = usuario.lower()
        pc = user_analiza(usuario)
        if pc != False:
            print(f"valor del Usuario: {usuario}, Valor de Pc: {pc}")
        if pc == False:
            continue
        else:
            print(f"Round {contador+1}")
            resultado = opciones(usuario,pc)
            if resultado == None:
                print("Empate")
            elif resultado == True:
                print(f"{pc} gana a {usuario}. Gana la pc")
                pc_count+=1
            else:
                print(f"{usuario} gana a la {pc}. Gana el usuario")
                usr_count+=1
            print("Marcador")
            print(f"Usuario: {usr_count}, Pc: {pc_count}")

        contador+=1
    print("")
    print("Resultado final: ")
    if usr_count > pc_count:
        print(f"Gano el usuario {usr_count} - {pc_count} a la pc")
    elif pc_count > usr_count:
        print(f"Gano la pc {pc_count} - {usr_count} al usuario")
    else:
        print("Empate entre la pc y el usuario")
        
            


run_game()






