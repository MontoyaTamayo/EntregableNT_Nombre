#Calcular el diametro de una circunferencia
pi = 3.1416
circunferencia = 100
diametro = circunferencia / pi
print(diametro)
radio = circunferencia/(2*pi)
print(f"El radio de un circulo con circunferencia{circunferencia} es {radio}")
circunferencia2 = 103
es_mayor = circunferencia2 >= circunferencia
print(type(es_mayor))
print(es_mayor)
es_mayor = radio > diametro
print(es_mayor)
son_grandes = (circunferencia and circunferencia2) >= 200
print(son_grandes)
son_grandes = (circunferencia or circunferencia2) <= 100
print(son_grandes)

#Operdadres de asignación
salario = 1300000
aux_transporte = 160200
salario = salario + aux_transporte 
salario += aux_transporte 
lado = 20
def calcular_area(lado):
 lado *= 4
 return lado
area = calcular_area(lado) 
print(area)