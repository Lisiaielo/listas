# Definir una lista de superhéroes como diccionarios
superheroes = [
    {
       'nombre': 'Capitana Marvel',
        'año_aparicion': 1968,
        'casa_comic': 'Marvel',
        'biografia': 'usa un traje'
    },
    {
       'nombre': 'Mujer Maravilla',
        'año_aparicion': 1941,
        'casa_comic': 'DC',
        'biografia': 'usa armadura'
    },
    {
        'nombre': 'Linterna Verde',
        'año_aparicion': 1940,
        'casa_comic': 'DC',
        'biografia': 'usa un traje'
    },
    {
        'nombre': 'Wolverine',
        'año_aparicion': 1974,
        'casa_comic': 'Marvel',
        'biografia': 'usa un traje'
    },
    {
        'nombre': 'Dr. Strange',
        'año_aparicion': 1963,
        'casa_comic': 'Marvel',
        'biografia': 'usa un traje'
    },
    {
        'nombre': 'Flash',
        'año_aparicion': 1930,
        'casa_comic': 'DC',
        'biografia': 'usa un traje'
    },
    {
        'nombre': 'Star-Lord',
        'año_aparicion': 1976,
        'casa_comic': 'Marvel',
        'biografia': 'usa armadura'
    }
]

# a. Eliminar el nodo que contiene la información de Linterna Verde
for superhero in superheroes:
    if superhero['nombre'] == 'Linterna Verde':
        superheroes.remove(superhero)
        break

# b. Mostrar el año de aparición de Wolverine
for superhero in superheroes:
    if superhero['nombre'] == 'Wolverine':
        print(f"Año de aparición de Wolverine: {superhero['año_aparicion']}")
        break

# c. Cambiar la casa de Dr. Strange a Marvel
for superhero in superheroes:
    if superhero['nombre'] == 'Dr. Strange':
        superhero['casa_comic'] = 'Marvel'
        break

# d. Mostrar el nombre de superhéroes con "traje" o "armadura" en su biografía
for superhero in superheroes:
    if 'armadura' in superhero['biografia']:
        print(f"Superhéroe con armadura: {superhero['nombre']}")
    if 'traje' in superhero['biografia']:
        print(f"Superhéroe con traje: {superhero['nombre']}")

# e. Mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963
for superhero in superheroes:
    if superhero['año_aparicion'] < 1963:
        print(f"Superhéroes anteriores a 1963: ")
        print(f"Nombre: {superhero['nombre']}, Casa de cómic: {superhero['casa_comic']}")

                 

# f. Mostrar la casa de Capitana Marvel y Mujer Maravilla
for superhero in superheroes:
    if superhero['nombre'] == 'Capitana Marvel' or superhero['nombre'] == 'Mujer Maravilla':
        print(f"Casa de {superhero['nombre']}: {superhero['casa_comic']}")

# g. Mostrar toda la información de Flash y Star-Lord
superheroes_buscados = ['Flash', 'Star-Lord']

for superhero in superheroes:
    if superhero['nombre'] in superheroes_buscados:
        print(f"Información de {superhero['nombre']}:")
        for key, value in superhero.items():
            print(f"{key}: {value}")
        print()
        
# h. Listar los superhéroes que comienzan con la letra B, M y S
letras = ['B', 'M', 'S']
for superhero in superheroes:
    if superhero['nombre'][0] in letras:
        print(f"Superhéroe que comienza con {superhero['nombre'][0]}: {superhero['nombre']}")

# i. Determinar cuántos superhéroes hay de cada casa de cómic
marvel_count = sum(1 for superhero in superheroes if superhero['casa_comic'] == 'Marvel')
dc_count = sum(1 for superhero in superheroes if superhero['casa_comic'] == 'DC')

print(f"Número de superhéroes de Marvel: {marvel_count}")
print(f"Número de superhéroes de DC: {dc_count}")