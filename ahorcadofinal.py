import random

categorias={
    "animales": ['perro', 'gato', 'elefante', 'jirafa', 'leon', 'tigre', 'oso', 'cebra', 'rinoceronte', 'mono', 'tortuga', 'camello', 'rinoceronte', 'hipopotamo', 'cocodrilo', 'serpiente', 'aguila', 'pinguino', 'ballena', 'delfin', 'zorro', 'murcielago', 'castor', 'ardilla', 'marmota', 'armadillo', 'foca', 'orca', 'lagarto', 'iguana', 'pulpo', 'langosta', 'cangrejo', 'gallina', 'pavo', 'pato', 'cisne', 'buho', 'halcon', 'abeja', 'mosquito', 'mariposa', 'hormiga', 'escarabajo', 'saltamontes', 'araña', 'caracol', 'gusano', 'grillo'],
    "ciudades": ['mexico', 'tokio', 'paris', 'londres', 'roma', 'berlin', 'madrid', 'moscu', 'bangkok', 'shanghai', 'singapur', 'sydney', 'toronto', 'nueva york', 'los ángeles', 'chicago', 'francisco', 'amsterdam', 'seul', 'dubai', 'hong kong', 'osaka', 'brasilia', 'lima', 'buenos aires', 'santiago', 'caracas', 'limassol', 'doha', 'monaco', 'kuala lumpur', 'lisboa', 'praga', 'vienna', 'copenhague', 'varsovia', 'budapest', 'zagreb', 'belgrado', 'kiev', 'sofia', 'nicosia', 'tallin', 'vilnius', 'riga', 'zurich', 'ginebra', 'estocolmo', 'oslo'],
    "apellidos": ['sanchez', 'garcia', 'gonzzlez', 'rodriguez', 'perez', 'martinez', 'hernandez', 'lopez', 'diaz', 'flores', 'ramos', 'castro', 'alvarez', 'gomez', 'fernandez', 'navarro', 'mendoza', 'munoz', 'reyes', 'morales', 'gutierrez', 'chavez', 'chavez', 'herrera', 'vargas', 'aguilar', 'rivera', 'valdez', 'vazquez', 'delgado', 'medina', 'pacheco', 'cano', 'castillo', 'silva', 'campos', 'romero', 'ortiz', 'fuentes', 'mendez', 'vega', 'sosa', 'velazquez', 'castaneda', 'pardo', 'mata', 'camacho', 'solis', 'maldonado', 'mendoza'],
    "frutas": ['manzana', 'pera', 'limon', 'naranja', 'platano', 'kiwi', 'pina', 'mango', 'sandia', 'melon', 'pomelo', 'uva', 'fresa', 'frambuesa', 'arandano', 'granada', 'mandarina', 'albaricoque','cereza', 'ciruela', 'higo', 'melocoton', 'nectarina', 'lima', 'maracuya', 'guayaba', 'membrillo','coco', 'guanabana', 'papaya', 'tamarindo', 'toronja', 'zapote', 'caimito', 'guayote', 'tuna', 'chirimoya', 'granadilla', 'kiwano', 'mamey', 'mangostino', 'noni', 'pepino dulce', 'pomarrosa', 'tangelo', 'carambola', 'feijoa', 'huevo de dragon', 'longan'],
    "objetos": ['silla', 'mesa', 'sofa', 'televisor', 'lampara', 'ventilador', 'libro', 'cuaderno', 'boligrafo', 'computadora', 'telefono', 'tableta', 'reloj', 'anillo', 'collar', 'aretes', 'pulsera', 'sombrero','zapatos', 'camisa', 'pantalon', 'falda', 'vestido', 'chaqueta', 'abrigo', 'gorra', 'lentes','camara', 'bicicleta', 'coche', 'moto', 'avion', 'barco', 'tren', 'balon', 'raqueta', 'pelota', 'rompecabezas', 'ajedrez', 'domino', 'dados', 'tijeras', 'cepillo', 'peine', 'toalla', 'esponja', 'plato', 'taza', 'vaso', 'cuchillo', 'tenedor', 'cuchara']
}

def elegir_palabra(categoria):
    if categoria == "animales":
        palabras = ['perro', 'gato', 'elefante', 'jirafa', 'leon', 'tigre', 'oso', 'cebra', 'rinoceronte', 'mono', 'tortuga', 'camello', 'rinoceronte', 'hipopotamo', 'cocodrilo', 'serpiente', 'aguila', 'pinguino', 'ballena', 'delfin', 'zorro', 'murcielago', 'castor', 'ardilla', 'marmota', 'armadillo', 'foca', 'orca', 'lagarto', 'iguana', 'pulpo', 'langosta', 'cangrejo', 'gallina', 'pavo', 'pato', 'cisne', 'buho', 'halcon', 'abeja', 'mosquito', 'mariposa', 'hormiga', 'escarabajo', 'saltamontes', 'araña', 'caracol', 'gusano', 'grillo']
    elif categoria == "ciudades":
        palabras = ['mexico', 'tokio', 'paris', 'londres', 'roma', 'berlin', 'madrid', 'moscu', 'bangkok', 'shanghai', 'singapur', 'sydney', 'toronto', 'nueva york', 'los ángeles', 'chicago', 'francisco', 'amsterdam', 'seul', 'dubai', 'hong kong', 'osaka', 'brasilia', 'lima', 'buenos aires', 'santiago', 'caracas', 'limassol', 'doha', 'monaco', 'kuala lumpur', 'lisboa', 'praga', 'vienna', 'copenhague', 'varsovia', 'budapest', 'zagreb', 'belgrado', 'kiev', 'sofia', 'nicosia', 'tallin', 'vilnius', 'riga', 'zurich', 'ginebra', 'estocolmo', 'oslo']
    elif categoria == "apellidos":
        palabras = ['sanchez', 'garcia', 'gonzalez', 'rodriguez', 'perez', 'martinez', 'hernandez', 'lopez', 'diaz', 'flores', 'ramos', 'castro', 'alvarez', 'gomez', 'fernandez', 'navarro', 'mendoza', 'munoz', 'reyes', 'morales', 'gutierrez', 'chavez', 'chavez', 'herrera', 'vargas', 'aguilar', 'rivera', 'valdez', 'vazquez', 'delgado', 'medina', 'pacheco', 'cano', 'castillo', 'silva', 'campos', 'romero', 'ortiz', 'fuentes', 'mendez', 'vega', 'sosa', 'velazquez', 'castaneda', 'pardo', 'mata', 'camacho', 'solis', 'maldonado', 'mendoza']
    elif categoria == "frutas":
        palabras = ['manzana', 'pera', 'limon', 'naranja', 'platano', 'kiwi', 'pina', 'mango', 'sandia', 'melon', 'pomelo', 'uva', 'fresa', 'frambuesa', 'arandano', 'granada', 'mandarina', 'albaricoque','cereza', 'ciruela', 'higo', 'melocoton', 'nectarina', 'lima', 'maracuya', 'guayaba', 'membrillo','coco', 'guanabana', 'papaya', 'tamarindo', 'toronja', 'zapote', 'caimito', 'guayote', 'tuna', 'chirimoya', 'granadilla', 'kiwano', 'mamey', 'mangostino', 'noni', 'pepino dulce', 'pomarrosa', 'tangelo', 'carambola', 'feijoa', 'huevo de dragon', 'longan']
    elif categoria == "objetos":
        palabras = ['silla', 'mesa', 'sofa', 'televisor', 'lampara', 'ventilador', 'libro', 'cuaderno', 'boligrafo', 'computadora', 'telefono', 'tableta', 'reloj', 'anillo', 'collar', 'aretes', 'pulsera', 'sombrero','zapatos', 'camisa', 'pantalon', 'falda', 'vestido', 'chaqueta', 'abrigo', 'gorra', 'lentes','camara', 'bicicleta', 'coche', 'moto', 'avion', 'barco', 'tren', 'balon', 'raqueta', 'pelota', 'rompecabezas', 'ajedrez', 'domino', 'dados', 'tijeras', 'cepillo', 'peine', 'toalla', 'esponja', 'plato', 'taza', 'vaso', 'cuchillo', 'tenedor', 'cuchara']
    else:
        print("categoria no valida, ingrese categoria valida (animales, ciudades, apellidos, frutas, objetos): ")
        return None
    return random.choice(palabras) #sirve para devolver una palabra aleatoria de la lista de palabras que se le pasa como argumento a la funcion

def obtener_palabra(categoria):
    if categoria not in categorias: #si la categoria no esta en las categorias
      print("Categoria no valida")
    return random.choice(categorias[categoria]) #devuelve una palabra aleatoria de la categoria elegida por el usuario, que luego se utiliza en el juego del ahorcado.

def mostrar_palabra(palabra, letras_adivinadas):
    palabra_oculta = ""
    for letra in palabra: #para cada letra en la palabra a adivinar
        if letra in letras_adivinadas: #verifica si la letra actual esta en la lista de letras adivinadas
            palabra_oculta += letra + " " # si la letra esta en la lista de letras adivinadas, se agrega a la cadena palabra_oculta seguida de un espacio en blanco
        else:
            palabra_oculta += "_ " #se agrega un guion bajo "_" seguido de un espacio en blanco a la cadena palabra_oculta para indicar que esa letra aun no se ha adivinado
    print("Palabra:", palabra_oculta.strip()) #muestra la cadena palabra_oculta sin los espacios en blanco al inicio o al final de la cadena usando metodo strip()

def mostrar_pistas(letra, palabra):
    indices_pistas = list(range(len(palabra))) #posiciones donde los indices que se utilizaran para mostrar las pistas en la palabra sean aleatorios
    pistas = ""
    for i, letra_palabra in enumerate(palabra): #recorre cada letra de la palabra y su indice, enumerate sirve para dar la posicion de cada letra y la letra
        if i in indices_pistas: #si el índice actual se encuentra en la lista de índices de pistas
            pistas += letra_palabra #agrega la letra correspondiente a la variable pistas
        else:
            pistas += "_" #no hay pista en esa posicion
    print("Pistas:", pistas)

def mostrar_ahorcado(intentos_restantes):
    if intentos_restantes == 6:
        print("""
             ______
            |      |
            |
            |
            |
            |
            |____________
            """)
    elif intentos_restantes == 5:
        print("""
             ______
            |      |
            |      O
            |
            |
            |
            |___________
            """)
    elif intentos_restantes == 4:
        print("""
             ______
            |      |
            |      O
            |      |
            |
            |
            |____________
            """)
    elif intentos_restantes == 3:
        print("""
             ______
            |      |
            |      O
            |     /|
            |
            |
            |_____________
            """)
    elif intentos_restantes == 2:
        print("""
             ______
            |      |
            |      O
            |     /|\
            |
            |
            |____________
            """)
    elif intentos_restantes == 1:
        print("""
             ______
            |      |
            |      O
            |     /|\
            |     /
            |
            |__________
            """)
    else:
        print("""
             ______
            |      |
            |      O
            |     /|\
            |     / \
            |
            |__________
            """)

intentos_maximos = 6

print('=' * 32)
print("Bienvenido al juego del ahorcado")
print('=' * 32)
print("\nDentro del juego las palabras no contienen tildes (á, é, í, ó, ú), ni dieresis (ü) y tampoco virgulillas (ñ)")
print("Tiene 3 pistas, que debe escribir para tener parte de la palabra")
print("NO LE VA A QUITAR INTENTOS DISPONIBLES")
print("""
             ______
            |      |
            |      |
            |      |
            |      O
            |
            |____________
            """)
categoria = input("\nElige una categoría (animales, ciudades, apellidos, frutas u objetos):")
print("\nLa cateoria de la palabra es:", categoria.upper()) #upper sirve para convertir todas las letras a mayusculas
palabra = obtener_palabra(categoria)
print("La palabra tiene", len(palabra), "letras")
pistas_restantes = 3
letras_adivinadas = []

while True:
    mostrar_palabra(palabra, letras_adivinadas)
    mostrar_ahorcado(intentos_maximos)
    print("pistas gratis restantes:", pistas_restantes)
    if pistas_restantes > 0:
        letra_pista = random.choice([letra for letra in palabra if letra not in letras_adivinadas])
        #crear una lista llamada letra, para cada letra en palabra si la letra no está en la lista "letras_adivinadas", agregar la letra a la lista "letra".
        #seleccionar una letra aleatoria de la lista "letra" y asignarla a la variable "letra_pista"
        print("pista:", letra_pista)
        pistas_restantes -= 1 #se van restando las 3 ayudas al jugador
    letra_introducida = input("introduce una letra: ")
    if letra_introducida in letras_adivinadas:
        print("ya has adivinado esa letra")
    elif letra_introducida in palabra:
        letras_adivinadas.append(letra_introducida)
        if len(set(letras_adivinadas)) == len(set(palabra)): #evalua si se han adivinado todas las letras, set sirve para rectificar que sean las mismas letras
          print("has adivinado la palabra")
          print("\n")
          print(palabra.upper()) #pasar las caracteres a mayusculas
          print("")
          print('=' * 21)
          print("Gracias por jugar! :)")
          print('=' * 21)
          break
    elif letra_introducida in letras_adivinadas and not letra_introducida:
        print("\nya introdujiste esa letra, pero la letra no esta en la palabra. intente de nuevo")
        mostrar_ahorcado(intentos_maximos) #muestra al ahorcado

        if intentos_maximos == 0:
            print("\nTe has quedado sin intentos :(, la palabra era:", palabra)
            break