import random

def generar_pass():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'ñ','o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z' ]
    numeros = ['1','2','3','4','5','6','7','8',9,'0']
    simbolos = ['!','@','|', '·',',','#','$','~','%','½','&','/','{','(','[',')',']','=','<','>',';',':','*','*','^','+']
    
    caracteres = mayusculas + minusculas + numeros + simbolos
    password = [] 
    for i in range(16):
        caracteresRandom = random.choice(caracteres)
        password.append(caracteresRandom)
    password = "".join(password)
    return password
def run():
    

    password = generar_pass()
    print('Tu nueva contrasena es ' + password)

if __name__ == '__main__':
    run()

