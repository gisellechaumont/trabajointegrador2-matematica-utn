# Definimos la función para verificar si un año es bisiesto
def es_bisiesto(anio):
    """
    Verifica si un año es bisiesto según las reglas:
    - Divisible por 4
    - No divisible por 100, a menos que también sea divisible por 400
    """
    if anio % 4 != 0:
        return False
    elif anio % 100 != 0:
        return True
    else:
        return anio % 400 == 0

# Lista de integrantes ordenados por DNI (menor a mayor)
integrantes = [
    {"nombre": "Stefan", "dni": "35820520"},
    {"nombre": "Giselle", "dni": "38016241"},
    {"nombre": "Mathias", "dni": "47782618"}
]

# Lista para almacenar los años de nacimiento
años_nacimiento = []

# Solicitamos los años de nacimiento para cada integrante
print("Ingrese los años de nacimiento de cada integrante:")

for persona in integrantes:
    while True:
        try:
            año = int(input(f"{persona['nombre']} ({persona['dni']}): "))
            if año < 1900 or año > 2023:
                print("Por favor ingrese un año entre 1900 y 2023.")
                continue
            if año in años_nacimiento:
                print("Este año ya fue ingresado. Por favor ingrese un año diferente.")
                continue
            años_nacimiento.append(año)
            break
        except ValueError:
            print("Debe ingresar un número válido para el año.")

# Inicializamos contadores
pares = 0
impares = 0
años_bisiestos = []

# Recorremos los años para contar pares/impares y detectar bisiestos
for año in años_nacimiento:
    if año % 2 == 0:
        pares += 1
    else:
        impares += 1
    if es_bisiesto(año):
        años_bisiestos.append(año)

# Calcular edades actuales
edades = [2023 - año for año in años_nacimiento]

# Mostrar resultados
print("\n=== RESULTADOS ===")
print(f"\nTotal de integrantes: {len(integrantes)}")
print(f"Nacidos en años pares: {pares}")
print(f"Nacidos en años impares: {impares}")

# Condiciones especiales
if all(año > 2000 for año in años_nacimiento):
    print("\n¡Grupo Z (todos nacieron después del 2000)!")

if años_bisiestos:
    print(f"\n¡Tenemos un año especial! Años bisiestos encontrados: {años_bisiestos}")
else:
    print("\nNo se encontraron años bisiestos en el grupo.")

# Mostrar edades
print("\nEdades actuales (2023):")
for i, persona in enumerate(integrantes):
    print(f"{persona['nombre']}: {edades[i]} años")

# Mostrar producto cartesiano
print("\nProducto cartesiano (año de nacimiento × edad actual):")
for i in range(len(integrantes)):
    print(f"({años_nacimiento[i]}, {edades[i]})", end=" ")
print()
