productos = []
producto1 = []
campos = 5
i = 0
while i < campos:
    valor = input("Ingrese campo", (i +1))
    producto1.append(valor)
    i+=1
    productos.append(producto1)
    
for item in producto1:
    print(item)    
    
encabezados = ("Id", "Nombre", "Precio", "Cantidad", "Categoria")
for encabezado in encabezados:
    print(encabezado, end="\t")
print()    
    
for item in producto1:   
    for tag in encabezados:
        print(item, end="\t") 
        
producto2 = []
campos = 5
i = 0
while i < campos:
    valor = input("Ingrese campo", (i +1))
    producto2.append(valor)
    i+=1
    productos.append(producto2)
    
for item in producto2:
    print(item)    
    
encabezados = ("Id", "Nombre", "Precio", "Cantidad", "Categoria")
for encabezado in encabezados:
    print(encabezado, end="\t")
print()    
    
for item in producto2:   
    for tag in encabezados:
        print(item, end="\t")       
        
producto3 = []
campos = 5
i = 0
while i < campos:
    valor = input("Ingrese campo", (i +1))
    producto3.append(valor)
    i+=1
    productos.append(producto3)
    
for item in producto3:
    print(item)    
    
encabezados = ("Id", "Nombre", "Precio", "Cantidad", "Categoria")
for encabezado in encabezados:
    print(encabezado, end="\t")
print()    
    
for item in producto3:   
    for tag in encabezados:
        print(item, end="\t")         
        
producto4 = []
campos = 5
i = 0
while i < campos:
    valor = input("Ingrese campo", (i +1))
    producto4.append(valor)
    i+=1
    productos.append(producto4)
    
for item in producto4:
    print(item)    
    
encabezados = ("Id", "Nombre", "Precio", "Cantidad", "Categoria")
for encabezado in encabezados:
    print(encabezado, end="\t")
print()    
    
for item in producto4:   
    for tag in encabezados:
        print(item, end="\t")         
        
producto5 = []
campos = 5
i = 0
while i < campos:
    valor = input("Ingrese campo", (i +1))
    producto5.append(valor)
    i+=1
    productos.append(producto5)
    
for item in producto5:
    print(item)    
    
encabezados = ("Id", "Nombre", "Precio", "Cantidad", "Categoria")
for encabezado in encabezados:
    print(encabezado, end="\t")
print()    
    
for item in producto5:   
    for tag in encabezados:
        print(item, end="\t")        