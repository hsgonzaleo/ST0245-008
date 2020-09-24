# Programa que devuelve la información del mes número n.

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", 
        "Octubre", "Noviembre", "Diciembre"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    mes = int(input("Ingrese el número del mes cuya información quiere obtener: "))
    if mes >= 1 and mes <= 12:
        print("El mes número {} es {} y tiene {} días.".format(mes, meses[mes - 1], dias[mes - 1]))
        break
    else:
        print("Error: mes incorrecto. Por favor inténtelo de nuevo")
    