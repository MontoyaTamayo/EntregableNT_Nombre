#Repetición entregable dedido a que se borro
usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")
telefono = input("Ingrese su número de teléfono: ")

# Supongamos solo que tienes un usuario permitido
usuario_permitido = ["Am@mail.com"]
contraseña = {"1208"}
telefono = {"3196320618"}

if usuario in usuario_permitido:
    if contraseña == contraseña[1208] and telefono == telefono[319632618]:
        print("Inicio de sesión exitoso")
    else:
        print("La contraseña o el número de teléfono es incorrecto")
else:
    print("El usuario no está permitido")