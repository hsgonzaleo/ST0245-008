# Programa que indica las posibilidades de empacar nuggets con paquetes de 6, 9 y 20.

class Posibility:  # Clase que ayuda a alamcenar las posibilidades.
    def __init__(self, six, nine, twenty):
        self.six = int(six)
        self.nine = int(nine)
        self.twenty = int(twenty)

    def __str__(self):
        return self.six, self.nine, self.twenty

def posibilidades(pos, nuggets, six = 0, nine = 0, twenty = 0):  # Función que busca las posibilidades de manera recursiva-
    if nuggets == 0:
        pos.add(Posibility(six, nine, twenty).__str__())
        return pos
    if nuggets < 0:
        return pos
    pos = posibilidades(pos, nuggets - 6, six + 1, nine, twenty)
    pos = posibilidades(pos, nuggets - 9, six, nine + 1, twenty)
    pos = posibilidades(pos, nuggets - 20, six, nine, twenty + 1)
    return pos

def print_posibilidades(pos, nuggets):
    if len(pos) == 0:
        print("Es imposible comprar %d nuggets" % nuggets)
    else:
        for posibilidad in pos:
            if posibilidad[0] != 0 and posibilidad[1] == 0 and posibilidad[2] == 0:
                print("Puede comprar %d paquetes de 6 nuggets" % posibilidad[0])
            elif posibilidad[0] == 0 and posibilidad[1] != 0 and posibilidad[2] == 0:
                print("Puede comprar %d paquetes de 9 nuggets" % posibilidad[1])
            elif posibilidad[0] == 0 and posibilidad[1] == 0 and posibilidad[2] != 0:
                print("Puede comprar %d paquetes de 20 nuggets" % posibilidad[2])
            elif posibilidad[0] != 0 and posibilidad[1] != 0 and posibilidad[2] == 0:
                print("Puede comprar %d paquetes de 6 nuggets y %d de 9 nuggets" % (posibilidad[0], posibilidad[1]))
            elif posibilidad[0] != 0 and posibilidad[1] == 0 and posibilidad[2] != 0:
                print("Puede comprar %d paquetes de 6 nuggets y %d de 20 nuggets" % (posibilidad[0], posibilidad[2]))
            elif posibilidad[0] == 0 and posibilidad[1] != 0 and posibilidad[2] != 0:
                print("Puede comprar %d paquetes de 9 nuggets y %d de 20 nuggets" % (posibilidad[1], posibilidad[2]))
            else:
                print("Puede comprar %d paquetes de 6 nuggets, %d de 9 nuggets y %d de 20 nuggets" % (posibilidad[0], posibilidad[1], posibilidad[2]))

pos = set()
nuggets = int(input("Ingrese el número de nuggets a comprar: "))
print()
pos = posibilidades(pos, nuggets)
print_posibilidades(pos, nuggets)