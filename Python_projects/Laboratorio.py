clientes = {}

# Funciones para  el cliente
def registrar_cliente(id_cliente, nombre, email, password):
    clientes[id_cliente] = {'nombre': nombre, 'email': email, 'password': password}
    print(f"Cliente {nombre} registrado, ¡Bienvenido!")

def modificar_cliente(id_cliente, nombre=None, email=None, password=None):
    if id_cliente in clientes:
        if nombre:
            clientes[id_cliente]['nombre'] = nombre
        if email:
            clientes[id_cliente]['email'] = email
        if password:
            clientes[id_cliente]['password'] = password
        print(f"Cliente {id_cliente} modificado con éxito")
    else:
        print("Cliente no encontrado")

def consultar_cliente(id_cliente):
    cliente = clientes.get(id_cliente)
    if cliente:
        print(f"Cliente {id_cliente}: {cliente}")
    else:
        print("Cliente no encontrado")

def eliminar_cliente(id_cliente):
    if id_cliente in clientes:
        del clientes[id_cliente]
        print(f"Cliente {id_cliente} eliminado con éxito")
    else:
        print("Cliente no encontrado")

# Menú de gestión para el cliente
def menu_gestion_clientes():
    while True:
        print("\nGestión de Clientes")
        print("1.Registrar cliente")
        print("2.Modificar cliente")
        print("3.Consultar cliente") 
        print("4.Eliminar cliente")
        print("5.Volver al menú principal")
        opcion = input("Seleccione una opción:")
        
        if opcion == "1":
            id_cliente = input("ID del cliente:")
            nombre = input("Nombre del cliente:")
            email = input("Email del cliente:")
            password = input("Password del cliente:")
            registrar_cliente(id_cliente, nombre, email, password)
        elif opcion == "2":
            id_cliente = input("ID del cliente:")
            nombre = input("Nombre del cliente:")
            email = input("Email del cliente:")
            password = input("Password del cliente:")
            modificar_cliente(id_cliente, nombre if nombre else None, email if email else None, password if password else None)
        elif opcion == "3":
            id_cliente = input("ID del cliente:")
            consultar_cliente(id_cliente)
        elif opcion == "4":
            id_cliente = input("ID del cliente:")
            eliminar_cliente(id_cliente)
        elif opcion == "5":
            break
        else:
            print("Opción no válida")

menu_gestion_clientes()

productos = {}

# Funciones para los productos
def agregar_producto(id_producto, nombre, cantidad, precio):
    productos[id_producto] = {'nombre': nombre, 'cantidad': cantidad, 'precio': precio}
    print(f"Producto {nombre} agregado con éxito")

def modificar_producto(id_producto, nombre=None, cantidad=None, precio=None):
    if id_producto in productos:
        if nombre:
            productos[id_producto]['nombre'] = nombre
        if cantidad is not None:
            productos[id_producto]['cantidad'] = cantidad
        if precio is not None:
            productos[id_producto]['precio'] = precio
        print(f"Producto {id_producto} modificado con éxito")
    else:
        print("Producto no encontrado")

def consultar_producto(id_producto):
    producto = productos.get(id_producto)
    if producto:
        print(f"Producto {id_producto}: {producto}")
    else:
        print("Producto no encontrado")

def eliminar_producto(id_producto):
    if id_producto in productos:
        del productos[id_producto]
        print(f"Producto {id_producto} eliminado con éxito")
    else:
        print("Producto no encontrado")

# Menú de gestión para productos
def menu_gestion_productos():
    while True:
        print("\nGestión de Productos")
        print("1.Agregar producto")
        print("2.Modificar producto")
        print("3.Consultar producto")
        print("4.Eliminar producto")
        print("5.Volver al menú principal")
        opcion = input("Seleccione una opción:")

        if opcion == "1":
            id_producto = input("ID del producto:")
            nombre = input("Nombre del producto:")
            cantidad = int(input("Cantidad del producto:"))
            precio = float(input("Precio del producto:"))
            agregar_producto(id_producto, nombre, cantidad, precio)
        elif opcion == "2":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto:")
            cantidad = input("Cantidad del producto:")
            precio = input("Precio del producto:")
            modificar_producto(id_producto, nombre if nombre else None, int(cantidad) if cantidad else None, float(precio) if precio else None)
        elif opcion == "3":
            id_producto = input("ID del producto:")
            consultar_producto(id_producto)
        elif opcion == "4":
            id_producto = input("ID del producto:")
            eliminar_producto(id_producto)
        elif opcion == "5":
            break
        else:
            print("Opción no válida")

menu_gestion_productos()

ventas = {}

# Funciones para las ventas
def iniciar_sesion(id_cliente, password):
    cliente = clientes.get(id_cliente)
    if cliente and cliente['password'] == password:
        return True
    return False

def realizar_venta(id_cliente, id_producto, cantidad):
    if id_cliente in clientes and id_producto in productos:
        producto = productos[id_producto]
        if producto['cantidad'] >= cantidad:
            producto['cantidad'] -= cantidad
            ventas.append({'id_cliente': id_cliente, 'id_producto': id_producto, 'cantidad': cantidad, 'precio_total': producto['precio'] * cantidad})
            print("Venta realizada con éxito")
        else:
            print("Cantidad insuficiente")
    else:
        print("Cliente o producto no encontrado")

# Menú de compras
def menu_compras():
    id_cliente = input("ID del cliente:")
    password = input("Password:")
    if iniciar_sesion(id_cliente, password):
        while True:
            print("\nMenú de Compras")
            print("1.Realizar compra")
            print("2.Volver al menú principal")
            opcion = input("Seleccione una opción:")

            if opcion == "1":
                id_producto = input("ID del producto:")
                cantidad = int(input("Cantidad a comprar:"))
                realizar_venta(id_cliente, id_producto, cantidad)
            elif opcion == "2":
                break
            else:
                print("Opción no válida")
    else:
        print("Credenciales incorrectas")

menu_compras()

def menu_principal():
    while True:
        print("\nMenú Principal")
        print("1.Gestión de Clientes")
        print("2.Gestión de Productos")
        print("3.Iniciar sesión para comprar")
        print("4.Salir")
        opcion = input("Seleccione una opción:")

        if opcion == "1":
            menu_gestion_clientes()
        elif opcion == "2":
            menu_gestion_productos()
        elif opcion == "3":
            menu_compras()
        elif opcion == "4":
            break
        else:
            print("Opción no válida")

menu_principal()