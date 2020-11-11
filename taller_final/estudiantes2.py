  
class Alumno:
    def __init__(self, nombre, edad, info):
        self.nombre = nombre
        self.edad = edad
        self.info = info
    def __str__(self):
       return self.nombre+' - '+str(self.edad)+' años - '+str(self.info)

class Nodo:
    def __init__(self, datos):
        self.datos = datos
        self.siguiente = None

### Optimización del algoritmo.
primero = None
lista_alumnos = [Alumno('Daniel García Salcedo', 18, "Monteriano. Tiene gusto por los videojuegos, el freestyle, la música, la comida y las series."),
Alumno('Daniel González Bernal', 29, "De Medellín. Estudia ingeniería de sistemas. Trabaja en sura. Tiene gusto por las motos, la cocina, hacer viajes, los videojuegos y las series. Calvo. "),
Alumno('Diego Velásquez Varela', 17, 'De Sabaneta. Estudia ingeniería matemática. Tiene 3 hermanas. Tiene gusto por la música, las series, las matemáticas y el estudio.'),
Alumno('Harold Steven González Ossa', 17, 'De Medellín. Estudiante de ingeniería matemática. Tiene gusto por la música, la lectura, los videojuegos, las películas, los rompecabezas y los doritos.'),
Alumno('Jayder Ochoa Carvajal', 'No se sabe cuántos', 'Estudiante de ingeniería de sistemas. Autodenominado simple. Tiene gusto por el anime. Intenta aprender cosas nuevas.'),
Alumno('Juan Felipe Agudelo Vélez', 17, 'De Envigado. Estudiante de ingeniería matemática. Tiene una hermana. Tiene gusto por la música, las matemáticas, la historia y la cazuela paisa. No le gusta el mondongo.'),
Alumno('Juan Felipe Martínez Bedoya', 20, 'De Envigado. Tiene un hermano y una hermana. Tiene gusto por la lectura, los videojuegos, las películas, la música, el gimnasio, el fútbol, los perros y la cerveza. Es curioso con la impresión 3D.'),
Alumno('Juan Manuel Múñoz Arias', 'No se sabe cuántos', 'Estudiante de ingeniería de sistemas. Tiene gusto por la música, los videojuegos y los estudios.'),
Alumno('Dónovan Castrillón Franco', 18, 'Estudiante de ingeniería de sistemas. Tiene gusto por los videojuegos, las series, el baloncesto, los gatos, la comida, la música y trasnochar. No le gusta la yuca.'),
Alumno('José Miguel Vélez Blanco', 17, 'Estudiante de ingeniería de sistemas. Tiene gusto por la música y los videojuegos.'),
Alumno('José Manuel Ramírez', 17, 'De Marinilla. Estudiante de ingeniería matemática. Tiene gusto por el anime, la música (es creador), los videojuegos y las matemátcias.'),
Alumno('Myllee Sarleth Mosquera Rivas', 17, 'Estudiante de ingeniería matemática. Tiene gusto por la música, el baile, el dibujo, la lectura y las matemáticas.'),
Alumno('Daniel Andrés Hernández Oyola', 17, 'Estudiante de ingeniería de sistemas. Tiene gusto por el deporte, los videojuegos, la comida y la música.'),
Alumno('Julián Andrés Mazo Z.', 17, 'Estudiante de ingeniería de sistemas. Tiene gusto por la música, los videojuegos, el dibujo, la lectura y estudiar. No le gusta la apatía.'),
Alumno('Santiago Parra Mejía', 16, 'De Sabaneta. Estudiante de ingeniería matemática. Tiene gusto por la música, la iglesia, la cocina, las matemáticas y las películas.'),
Alumno('Salomón Vélez Pérez', 17, 'Estudiante de ingeniería matemática. Tiene gusto por los videojuegos, la lectura, la escritura y la música.'),
Alumno('Simón Gómez Arango', 17, 'De Medellín. Estudiante de ingeniería de sistemas. Tiene gusto la lectura, las películas, las series, los videojuegos, el campo, la meditación y lo paranormal. Tiene mala memoria y odia el calor.'),
Alumno('Cristian Camilo Zapata García', 18, 'De Carmen de Viboral. Estudia ingeniería de sistemas. Tiene gusto por la comida, la música, los viajes y los videojuegos. Quiere viajar por el mundo.')]
for alumno in lista_alumnos:
    nodo = Nodo(alumno)
    nodo.siguiente = primero
    primero = nodo
n = primero
while n != None:
 print(n.datos)
 n = n.siguiente