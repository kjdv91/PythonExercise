import random


def run():
    numeroAleatorio = random.randint(1, 50)
    numeroIngresado = int(input('Ingresa un numero del 1 al 50'))

    while numeroAleatorio != numeroIngresado:
        if numeroIngresado < numeroAleatorio:
            print('Busca un numero mas grande')
        else: 
            print('Busca un numero mas bajo')
        numeroIngresado = int(input('Ingresa otro numero'))

        print('Numero ganador ganastes')


    if __name__ == '__main__':
        run() 