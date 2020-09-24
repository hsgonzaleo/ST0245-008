# Programa que crea quinielas.

class Quiniela:
    def __init__(self, equipos, resultados):
        self.equipos = equipos
        self.resultados = resultados
    def __str__(self):
        rep = "QUINIELA\n"
        for equipo in range(1, 16):
            rep = rep + "\nPARTIDO %d\n" % equipo + equipos[equipo - 1][0] + " - " + equipos[equipo - 1][1] + "\n" + str(resultados[equipo - 1][0]) + " - " + str(resultados[equipo - 1][1])
        return rep

equipos = []
resultados = []
for partido in range(1, 16):
    equipo = []
    resultado = []
    equipo.append(str(input("Ingrese el nombre del primer equipo del partido %d: " % partido)))
    resultado.append(int(input("Ingrese el número de goles que anotó el primer equipo: ")))
    equipo.append(str(input("Ingrese el nombre del segundo equipo del partido %d: " % partido)))
    resultado.append(int(input("Ingrese el número de goles que anotó el segundo equipo: ")))
    equipos.append(equipo)
    resultados.append(resultado)

quiniela = Quiniela(equipos, resultados)

print(quiniela)