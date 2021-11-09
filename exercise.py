
try:
    num1 = int(input("Ingresa el primer numero \n"))
    num2 = int(input("Ingresa el segundo numero \n"))
    op = input("Ingresa la operacion")

    if op == "+":
        print("El resultado de la suma es ", + num1+num2)
    elif op == "-":
        print("El resultado de la resta es", + num1-num2)
    elif op == "*":
        print("El resulatdo de la multiplicacion es", + num1*num2)
    elif op == "/":
        print("El resultado de la division es ", + abs(num1/num2))
except ValueError:
    print("El valor no es un entero")

print("Create account now")

username = input("ingresa tu usuario")
password = input("Ingresa tu password")

print("Tu cuenta ha sido creada correctamente")
print("Login Now")

username2 = input("Ingresa tu usuario")
password2 = input("ingresa tu password")

if username == username2 and password == password2:
    print("Login correcto")
else:
    print("Credenciales invàlidas")
