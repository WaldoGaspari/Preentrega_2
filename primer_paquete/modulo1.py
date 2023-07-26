class Cliente:

    def __init__(self, nombre, apellido, edad, mail, intereses):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.mail = mail
        self.intereses = intereses
        self.productos = {}
    
    def __str__(self):
        return f"Los datos del cliente son: \n Nombre: {self.nombre} \n Apellido: {self.apellido} \n Edad: {self.edad} \n Mail: {self.mail} \n Intereses: {self.intereses}"

    def comprar(self, producto, local):
        self.productos.update({producto: local})
        print(f"El cliente {self.nombre} {self.apellido}  ha comprado el siguiente producto: '{producto}' en la tienda {local}. \nSe le ha enviado un correo con su factura a {self.mail}.")
    
    def mostrar_productos(self):
        if(len(self.productos) == 0):
            print(f"El cliente {self.nombre} {self.apellido} no ha comprado ningún producto por el momento.")
        else:
            print(f"El cliente {self.nombre} {self.apellido} ha comprado los siguientes productos:")
            for producto, local in self.productos.items():
                print(f"{producto} comprado en {local}")
    