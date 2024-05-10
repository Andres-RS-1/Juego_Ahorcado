import random

categorias = {
    "animales": ['perro', 'gato', 'elefante', 'jirafa', 'leon', 'tigre', 'oso', 'cebra', 'rinoceronte', 'mono', 'tortuga', 'camello', 'rinoceronte', 'hipopotamo', 'cocodrilo', 'serpiente', 'aguila', 'pinguino', 'ballena', 'delfin', 'zorro', 'murcielago', 'castor', 'ardilla', 'marmota', 'armadillo', 'foca', 'orca', 'lagarto', 'iguana', 'pulpo', 'langosta', 'cangrejo', 'gallina', 'pavo', 'pato', 'cisne', 'buho', 'halcon', 'abeja', 'mosquito', 'mariposa', 'hormiga', 'escarabajo', 'saltamontes', 'araña', 'caracol', 'gusano', 'grillo'],
    "ciudades": ['mexico', 'tokio', 'paris', 'londres', 'roma', 'berlin', 'madrid', 'moscu', 'bangkok', 'shanghai', 'singapur', 'sydney', 'toronto', 'nueva york', 'los angeles', 'chicago', 'san francisco', 'amsterdam', 'seul', 'dubai', 'hong kong', 'osaka', 'brasilia', 'lima', 'buenos aires', 'santiago', 'caracas', 'limassol', 'doha', 'monaco', 'kuala lumpur', 'lisboa', 'praga', 'vienna', 'copenhague', 'varsovia', 'budapest', 'zagreb', 'belgrado', 'kiev', 'sofia', 'nicosia', 'tallin', 'vilnius', 'riga', 'zurich', 'ginebra', 'estocolmo', 'oslo'],
    "apellidos": ['sanchez', 'garcia', 'gonzales', 'rodriguez', 'perez', 'martinez', 'hernandez', 'lopez', 'diaz', 'flores', 'ramos', 'castro', 'alvarez', 'gomez', 'fernandez', 'navarro', 'mendoza', 'munoz', 'reyes', 'morales', 'gutierrez', 'chavez', 'chavez', 'herrera', 'vargas', 'aguilar', 'rivera', 'valdez', 'vazquez', 'delgado', 'medina', 'pacheco', 'cano', 'castillo', 'silva', 'campos', 'romero', 'ortiz', 'fuentes', 'mendez', 'vega', 'sosa', 'velazquez', 'castaneda', 'pardo', 'mata', 'camacho', 'solis', 'maldonado', 'mendoza'],
    "frutas": ['manzana', 'pera', 'limon', 'naranja', 'platano', 'kiwi', 'pina', 'mango', 'sandia', 'melon', 'pomelo', 'uva', 'fresa', 'frambuesa', 'arandano', 'granada', 'mandarina', 'albaricoque', 'cereza', 'ciruela', 'higo', 'melocoton', 'nectarina', 'lima', 'maracuya', 'guayaba', 'membrillo', 'coco', 'guanabana', 'papaya', 'tamarindo', 'toronja', 'zapote', 'caimito', 'guayote', 'tuna', 'chirimoya', 'granadilla', 'kiwano', 'mamey', 'mangostino', 'noni', 'pepino dulce', 'pomarrosa', 'tangelo', 'carambola', 'feijoa', 'huevo de dragon', 'longan'],
    "objetos": ['silla', 'mesa', 'sofa', 'televisor', 'lampara', 'ventilador', 'libro', 'cuaderno', 'boligrafo', 'computadora', 'telefono', 'tableta', 'reloj', 'anillo', 'collar', 'aretes', 'pulsera', 'sombrero', 'zapatos', 'camisa', 'pantalon', 'falda', 'vestido', 'chaqueta', 'abrigo', 'gorra', 'lentes', 'camara', 'bicicleta', 'coche', 'moto', 'avion', 'barco', 'tren', 'balon', 'raqueta', 'pelota', 'rompecabezas', 'ajedrez', 'domino', 'dados', 'tijeras', 'cepillo', 'peine', 'toalla', 'esponja', 'plato', 'taza', 'vaso', 'cuchillo', 'tenedor', 'cuchara']
}

def obtener_palabra(categoria):
    if categoria not in categorias:
        raise ValueError("Categoría no válida")
    return random.choice(categorias[categoria])

def mostrar_palabra(palabra, letras_adivinadas):
    palabra_oculta = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_oculta += letra + " "
        else:
            palabra_oculta += "_ "
    print("Palabra:", palabra_oculta.strip())

def mostrar_ahorcado(intentos_restantes):
    partes_ahorcado = [
        """
             ______
            |      |
            |
            |
            |
            |
            |____________
        """,
        """
             ______
            |      |
            |      O
            |
            |
            |
            |___________
        """,
        """
             ______
            |      |
            |      O
            |      |
            |
            |
            |____________
        """,
        """
             ______
            |      |
            |      O
            |     /|
            |
            |
            |_____________
        """,
        """
             ______
            |      |
            |      O
            |     /|/
            |
            |
            |____________
        """,
        """
             ______
            |      |
            |      O
            |     /|/
            |     /
            |
            |__________
        """,
        """
             ______
            |      |
            |      O
            |     /|/
            |     / /
            |
            |__________
        """
    ]

    if intentos_restantes <= 0:
        print(partes_ahorcado[-1])
    else:
        print(partes_ahorcado[6 - intentos_restantes])

def jugar_ahorcado():
    intentos_maximos = 6

    print('=' * 32)
    print("Bienvenido al juego del ahorcado")
    print('=' * 32)
    print("\nDentro del juego las palabras no contienen tildes (á, é, í, ó, ú), ni dieresis (ü) y tampoco virgulillas (ñ)")
    print("Tiene 3 pistas, que debe escribir para tener parte de la palabra")
    print("NO LE VA A QUITAR INTENTOS DISPONIBLES")

    # Selección de categoría
    while True:
        categoria = input("\nElige una categoría (animales, ciudades, apellidos, frutas u objetos): ").lower()
        if categoria in categorias:
            break
        else:
            print("Categoría no válida. Por favor, elige una categoría válida.")

    print("\nLa categoría de la palabra es:", categoria.upper())
    palabra = obtener_palabra(categoria)
    print("La palabra tiene", len(palabra), "letras")

    pistas_restantes = 3
    letras_adivinadas = []

    while True:
        # Mostrar estado actual del juego
        mostrar_palabra(palabra, letras_adivinadas)
        mostrar_ahorcado(intentos_maximos)
        print("Pistas gratis restantes:", pistas_restantes)

        # Obtener entrada del usuario
        letra_introducida = input("Introduce una letra o 'p' para pedir una pista: ")

        if letra_introducida == 'p':
            if pistas_restantes > 0:
                # Mostrar pista
                letra_pista = random.choice([letra for letra in palabra if letra not in letras_adivinadas])
                print("Pista:", letra_pista)
                pistas_restantes -= 1
            else:
                print("Ya no tienes pistas restantes.")
        elif letra_introducida in letras_adivinadas:
            print("Ya has adivinado esa letra.")
        elif letra_introducida in palabra:
            letras_adivinadas.append(letra_introducida)
            if set(letras_adivinadas) == set(palabra):
                print("Has adivinado la palabra!")
                print("La palabra era:", palabra.upper())
                print('=' * 21)
                print("Gracias por jugar!")
                print('=' * 21)
                break
        else:
            print("Letra incorrecta.")
            intentos_maximos -= 1
            if intentos_maximos == 0:
                print("Te has quedado sin intentos :(")
                print("La palabra era:", palabra.upper())
                print('=' * 21)
                print("Gracias por jugar!")
                print('=' * 21)
                break
jugar_ahorcado()