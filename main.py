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
    return ''.join(random.choice(string.hexdigits) for _ in range(10)) #contrasena hecha en base a numeros hexadecimales con un len de 10.

#lista de usuarios
usuarios = ["user1","user2","user3","user4","user5","user6","user7","user8","user9","user10"]
#listas que juntan los datos
contraseñas =[]
telefonos = []

#Loop con condicion basada en que el largo de la lista del telefono sea menor a 10. Si es falso termina el loop
while len(telefonos) < 10:
    correcto = False #Boton para terminar loop
    while correcto == False:
            numero_t = input("Ingrese su teléfono: ")
            if usernumber(numero_t) == True: #condicional para aceptar el input de numero basado en la funcion de usernumber
                telefonos.append(numero_t) #si la condicion es true, se agrega a la lista
                print("Teléfono ingresado exitosamente")
                correcto=True #termina este ciclo y pasa al siguiente 

    correcto = False #boton para terminar loop
    while correcto == False:
        contraseñas.append(password()) #contrasena aleatorea se agrega a la lista de contrasenas        
        correcto = True
    cuentas = list(zip(usuarios,contraseñas,telefonos)) #junta los diferentes elementos de la lista
    print(cuentas)
print("Usuarios registrados exitosamente") #Este mensaje saldra cuando esten los 10 usuarios registrados