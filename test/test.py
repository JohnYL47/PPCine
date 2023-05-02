nameUsers = []
emailUsers = []
passwordUsers = []

def loginUser(menu):
    if menu == 1:
        loginIn(input("| Login |\nIngrese su nombre e usuario: "),input("Ingrese su email: "),input("Ingrese su contraseña: "))
    elif menu == 2:
        RegisterUser(input("| Registro |\nIngrese un nombre de usuario: "),input("Ingrese su email de usuario: "),input("Ingrese una contraseña para el usuario: "))
    elif menu == 3:
        print("Leave >")
    else:
        print("Error.\nIngrese correctamente los datos\n")
        loginUser(int(input("\n|| Login ||\n1. Iniciar sesion\n2. Registrarse\n3. Salir\nOpcion: ")))        

def loginIn(name,email,password):
    return
    

def RegisterUser(name,email,password):
    
    confirm = input("\n| Desea guardar usuario? (y/n): ")
    if confirm == "y":
        nameUser = name
        emailUser = email
        passwordUser = password
        nameUsers.append(nameUser), emailUsers.append(emailUser), passwordUsers.append(passwordUser)
    else:
        print("OK")
        loginUser(int(input("\n|| Login ||\n1. Iniciar sesion\n2. Registrarse\n3. Salir\nOpcion: ")))


loginUser(int(input("\n|| Login ||\n1. Iniciar sesion\n2. Registrarse\n3. Salir\nOpcion: ")))

print(f"\nInformacion de las tablas\nUsuario:\n{nameUsers}\nEmails:\n{emailUsers}\nPassword:\n{passwordUsers}")


'''def suma(a,b):
    retorna la suma de a y b
    > suma(10,10)
    20
    
    return print(a + b)

suma(int(input("Ingrese un numero: ")),int(input("Ingrese otro numero: ")))'''
import doctest
doctest.testmod()