from primer_paquete.modulo1 import Cliente
from primer_paquete.modulo2 import *

cliente = Cliente("Juan", "Perez", 30, "juan_perez@mail.com", ["Tecnología", "Música"])
print(cliente)
cliente.comprar("Auriculares", "Fravega")
cliente.comprar("Televisor SMART 29'' ", "Musimundo")
cliente.comprar("Heladera Patrick No frost", "Fravega")
cliente.mostrar_productos()

print("-----------------------------------------")

cliente2 = Cliente("Laura", "Gimenez", 45, "lau_03@mail.com", ["Hogar", "Jardin", "Muebles"])
print(cliente2)
cliente2.mostrar_productos()

print("-----------------------------------------")

# Uso del modulo2
# 1) Se crea una base de datos.
# 2) Se registran 3 usuarios.
# 3) Se muestran los datos que tiene la base de datos.
# 4) Se loguea un usuario registrado.
# 5) Se guarda la informacion de la base de datos en un archico .txt (Tiene como ruta el Escritorio)

base_de_datos = {}

registrar_usuario(base_de_datos)
registrar_usuario(base_de_datos)
registrar_usuario(base_de_datos)

leer_base_de_datos(base_de_datos)

loguearse(base_de_datos)

guardar_archivo(base_de_datos)