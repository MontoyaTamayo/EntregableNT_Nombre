usuarios = []

for _ in range(5):
    usuario = []
    nombre = input("Ingrese el nombre del usuario:")
    usuario.append(nombre)
    apellido = input("Ingrese el apellido del usuario:")
    usuario.append(apellido)
    telefono = input("Ingrese el teléfono del usuario:")
    usuario.append(telefono)
    correo = input("Ingrese el correo del usuario:")
    usuario.append(correo)
    clave = input("Ingrese la clave del usuario:")
    usuario.append(clave)
    usuarios.append(usuario)

for usuario in usuarios:
    print("Nombre:", usuario[0])
    print("Apellido:", usuario[1])
    print("Teléfono:", usuario[2])
    print("Correo:", usuario[3])
    print("Clave:", usuario[4])