# Entrenadores y sus pokemons
entrenadores = [
    ["Entrenador1", 5, 2, 10, [
        ["Charizard", 30, "Fuego", "None"],
        ["Blastoise", 25, "Agua", "Volador"],
    ]],
    ["Entrenador2", 7, 3, 15, [
        ["Venusaur", 40, "Planta", "None"],
        ["Arcanine", 35, "Fuego", "None"],
    ]],
    ["Entrenador3", 4, 1, 12, [
       ["Lapras", 32, "Agua", "None"],
       ["Flareon", 28, "Fuego", "None"],
    ]],
    ["Entrenador4", 6, 4, 8, [
        ["Vileplume", 38, "Planta", "None"],
        ["Pidgeot", 30, "Volador", "None"],
    ]],
     ["Entrenador5", 3, 2, 7, [
        ["Wingull", 22, "Agua", "Volador"],
    ]],
]
# A) Función para obtener la cantidad de Pokémon de un entrenador
def cantidad_de_pokemon(entrenador_nombre):
    for entrenador in entrenadores:
        if entrenador[0] == entrenador_nombre:
            return len(entrenador[4])
    return 0

# B) Función para listar entrenadores con más de tres torneos ganados 
def entrenadores_mas_de_tres_torneos():
    return [entrenador[0] for entrenador in entrenadores if entrenador[1] > 3]

# C) Función para encontrar el Pokémon de mayor nivel del entrenador con más torneos ganados
def pokemon_mayor_nivel_entrenador_mas_torneos():
    entrenador_mas_torneos = max(entrenadores, key=lambda x: x[1])
    pokemon_mayor_nivel = max(entrenador_mas_torneos[4], key=lambda x: x[1])
    return pokemon_mayor_nivel

# D) Función para mostrar todos los datos de un entrenador y sus Pokémon 
def mostrar_datos_entrenador(entrenador_nombre):
    for entrenador in entrenadores:
        if entrenador[0] == entrenador_nombre:
            return entrenador
    return None

# E) Función para mostrar entrenadores con un porcentaje de batallas ganadas mayor al 79% 
def entrenadores_porcentaje_ganadas_mayor_79():
    return [entrenador[0] for entrenador in entrenadores if (entrenador[3] / (entrenador[2] + entrenador[3])) > 0.79]

# F) Función para encontrar entrenadores con Pokémon de tipo fuego y planta o agua/volador 
def entrenadores_con_tipos_especificos():
    return [entrenador[0] for entrenador in entrenadores if any((pokemon[2] == "Fuego" and pokemon[3] == "Planta") or (pokemon[2] == "Agua" and pokemon[3] == "Volador") for pokemon in entrenador[4])]

# G) Función para calcular el promedio de nivel de los Pokémon de un entrenador 
def promedio_nivel_pokemon(entrenador_nombre):
    for entrenador in entrenadores:
        if entrenador[0] == entrenador_nombre:
            niveles = [pokemon[1] for pokemon in entrenador[4]]
            return sum(niveles) / len(niveles)
    return 0

# H) Función para contar cuántos entrenadores tienen un Pokémon específico 
def cantidad_entrenadores_con_pokemon(pokemon_nombre):
    return len([entrenador for entrenador in entrenadores if any(pokemon[0] == pokemon_nombre for pokemon in entrenador[4])])

# I) Función para encontrar entrenadores con Pokémon repetidos 
def entrenadores_con_pokemon_repetidos():
    entrenadores_con_repetidos = []
    for entrenador in entrenadores:
        pokemones = [pokemon[0] for pokemon in entrenador[4]]
        if len(pokemones) != len(set(pokemones)):
            entrenadores_con_repetidos.append(entrenador[0])
    return entrenadores_con_repetidos

# J) Función para encontrar entrenadores con ciertos Pokémon específicos 
def entrenadores_con_pokemones_especificos(pokemones_especificos):
    return [entrenador[0] for entrenador in entrenadores if any(pokemon[0] in pokemones_especificos for pokemon in entrenador[4])]

# K) Función para verificar si un entrenador tiene un Pokémon específico 
def entrenador_tiene_pokemon(entrenador_nombre, pokemon_nombre):
    for entrenador in entrenadores:
        if entrenador[0] == entrenador_nombre:
            return any(pokemon[0] == pokemon_nombre for pokemon in entrenador[4])
    return False

# Ejemplos de uso de las funciones
print("Cantidad de Pokémon de Entrenador1:", cantidad_de_pokemon("Entrenador1"))
print("Entrenadores con más de tres torneos ganados:", entrenadores_mas_de_tres_torneos())
print("Pokémon de mayor nivel del entrenador con más torneos ganados:", pokemon_mayor_nivel_entrenador_mas_torneos())
print("Datos de Entrenador2 y sus Pokémon:", mostrar_datos_entrenador("Entrenador2"))
print("Entrenadores con más del 79% de batallas ganadas:", entrenadores_porcentaje_ganadas_mayor_79())
print("Entrenadores con tipos específicos de Pokémon:", entrenadores_con_tipos_especificos())
print("Promedio de nivel de los Pokémon de Entrenador1:", promedio_nivel_pokemon("Entrenador1"))
print("Cantidad de entrenadores con Pokémon 'Charizard':", cantidad_entrenadores_con_pokemon("Pokemon1"))
print("Entrenadores con Pokémon repetidos:", entrenadores_con_pokemon_repetidos())
print("Entrenadores con Pokémon específicos:", entrenadores_con_pokemones_especificos(["Tyrantrum", "Terrakion", "Wingull"]))
print("¿Entrenador1 tiene a 'Charizard'?", entrenador_tiene_pokemon("Entrenador1", "Charizard"))