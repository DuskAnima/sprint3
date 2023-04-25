import random
import string

#función para ingresar teléfono
def usernumber(u_num): 
    chara = len(u_num) #variable de longitud
    n = u_num.isdigit() #revisa si el input contiene solo numeros
    if n == False: #check de isdigit
        print("Por favor, solo ingrese numeros")
    elif not chara == 8: 
        print("Por favor, ingrese 8 caracteres")
    elif chara == 8 and n == True:
        return True #Verdadero si el tamaño es mayor a 5 y menor a 13

#función para contraseñas aleatorias
def password():
    return ''.join(random.choice(string.hexdigits) for _ in range(10))

#listas que juntan los datos
usuarios = ["user1","user2","user3","user4","user5","user6","user7","user8","user9","user10"]
contraseñas =[]
telefonos = []

while len(telefonos) < 10:
    correcto = False
    while correcto == False:
            numero_t = input("Ingrese su teléfono: ")
            if usernumber(numero_t) == True:
                telefonos.append(numero_t)
                print("Teléfono ingresado exitosamente")
                correcto=True

    correcto = True
    while correcto == True:
        contraseñas.append(password())
        print(password())
        correcto = False
    cuentas = list(zip(usuarios,contraseñas,telefonos))
    print(cuentas)
print("Usuarios registrados exitosamente")