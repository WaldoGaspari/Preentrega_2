def registrar_usuario(base_de_datos):
    while(True):
        usuario = input("Ingrese el usuario: ")
        contrasenia = input("Ingrese la contraseña: ")
        if(usuario == ""):
            print("El nombre de usuario no puede estar vacio.")
        elif(contrasenia == ""):
            print("La contraseña no puede ser vacia.")
        else:
            base_de_datos[usuario] = contrasenia
            print("Usuario registrado correctamente.")
            break

def leer_base_de_datos(base_de_datos):
    print("La información almacenada en la base de datos es la siguiente:")
    if(len(base_de_datos) == 0):
        print("No hay información cargada en la base de datos. Se encuentra vacia.")
    else:
        for clave, valor in base_de_datos.items():
            print("Usuario:", clave)
            print("Contraseña:", valor)
            print("--------------------------")

def loguearse(base_de_datos):
    while(True):
        usuario = input("Ingrese su usuario: ")
        if(usuario in base_de_datos.keys()):
            contrasenia = input("Ingrese su contraseña: ")
            if(contrasenia in base_de_datos.values()):
                print("Has iniciado sesión correctamente.")
                break
            else:
                print("Contraseña incorrecta. Intente de nuevo.")
        else:
            print("Usuario incorrecto. Intente de nuevo.")

def guardar_archivo(base_de_datos):
    ruta = "C:/Users/Equipo/Desktop"
    archivo = open(ruta + "/base_de_datos.txt", "w")
    for clave in base_de_datos.keys():
        archivo.write("Usuario: " + clave + ", " + "Contraseña: " + base_de_datos[clave] + "\n")
    archivo.close()