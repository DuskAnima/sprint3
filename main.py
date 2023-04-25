import random
import string

"""
#función para ingresar teléfono
def usernumber(u_num): 
    chara = len(u_num) #variable de longitud
    n = u_num.isdigit() #revisa si el input contiene solo numeros
    if n == False: #check de isdigit
        print("Por favor, solo ingrese numeros")
    if not chara == 8: 
        print("Por favor, ingrese 8 caracteres")
    if chara == 8 and n == True:
        return True #Verdadero si el tamaño es mayor a 5 y menor a 13
        


correcto = False
while correcto == False:
        numero_t = input("Ingrese su teléfono: ")
        if usernumber(numero_t) == True:
            print("Teléfono ingresado exitosamente")
            correcto=True

"""




#def password(passw_l):

done = True
while done == False:
    chara = list(string.ascii_letters) + list(string.digits)
    temp = [random.choice(chara) for i in range(10)]
    
    
    
    passw = "".join(temp)




"""

for i in range():
    temp = random.sample(chara)
    passw = temp
print(passw)


"""


"""


usuarios = []
contraseñas = []
telefono = []


correcto = False
while correcto == False:
        nombre = input("Ingrese nombre de usuario: ")
        if username(nombre) == True:
            print("Usuario creado exitosamente")
            correcto=True

while correcto == True:
    print(f"Su clave es: {password}")
    correcto = False

"""