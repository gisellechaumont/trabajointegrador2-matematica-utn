etiquetas= ["primer", "segundo", "tercer"]
dnis= []

#Ingreso de los tres dnis
for i in range (3):
    dni=int(input(f"Ingrese el {etiquetas[i]} DNI: "))
    dnis.append(str(dni))
    
#Crear conjutnos de digitos unicos
conjuntos= [set(dni) for dni in dnis]

# Mostrar dígitos únicos ordenados
print("\nDígitos unicos de cada DNI:")
for i in range(3):
    ordenados = sorted(int(d) for d in conjuntos[i])
    print(f"{etiquetas[i].capitalize()} DNI ({dnis[i]}): {ordenados}")
    
#Operaciones entre los tres conjuntos
a, b, c= conjuntos 
print("\nOperaciones entre los conjuntos:")
print("Union:", sorted(map(int, a | b | c)))
print("Interseccion:", sorted(map(int, a & b & c)))
print("Diferencia primer y segundo conjunto", sorted(map(int, a - b)))
print("Diferencia segundo y primer conjunto", sorted(map(int, b - a)))
print("Diferencia primer y tercer conjunto", sorted(map(int, a- c)))
print("Diferencia tercer y primer conjunto", sorted(map(int, c - a)))
print("Diferencia segundo y tercer conjunto", sorted(map(int, b - c)))
print("Diferencia tercer y segundo conjunto", sorted(map(int, c - b)))
print("Diferencia simetrica primer y segundo conjunto", sorted(map(int, a ^ b)))
print("Diferencia simetrica primer y tercer conjunto", sorted (map(int, a ^ c)))
print("Diferencia simetrica segundo y tercer conjunto", sorted(map(int, b ^ c)))

#Conteo de frecuencia
print("\nFrecuencia de cada digito en cada DNI:")
for i in range(3):
    frecuencia = {}  # diccionario vacío
    for digito in dnis[i]:
        if digito in frecuencia:
            frecuencia[digito] += 1
        else:
            frecuencia[digito] = 1
    print(f"\n{etiquetas[i].capitalize()} DNI ({dnis[i]}):")
    for digito in sorted(frecuencia):
        print(f"Digito {digito}: {frecuencia[digito]} veces")

#Suma total de los digitos de cada DNI
print("\nSuma total de los digitos de cada DNI")
for i in range(3):
    suma=0
    for digito in dnis[i]:
        suma += int(digito)
    print(f"{etiquetas[i].capitalize()} DNI ({dnis[i]}): suma = {suma}")

#Evaluacion de condiciones
print("\n Evaluacion de condiciones:")

#Si algún dígito aparece en los 3 conjuntos
interseccion= a & b & c
if interseccion:
    print(f"Digitos compartidos en los 3 DNIs: {sorted(interseccion)} → Digito compartido")
else:
     print("No hay ningun digito compartido en los 3 DNIs")
     
#Verificar diversidad numérica en cada conjunto
for i in range(3):
    cantidad=len(conjuntos[i])
    if cantidad > 6:
        print(f"{etiquetas[i].capitalize()} DNI ({dnis[i]}): {cantidad} digitos unicos → Diversidad numerica alta")
    else:
        print(f"{etiquetas[i].capitalize()} DNI ({dnis[i]}): {cantidad} digitos unicos")

#Conjunto par completo
digitos_pares = {0, 2, 4, 6, 8}
encontrado = False

for i in range(3):
    no_pares = 0
    for digito in conjuntos[i]:
        if digito not in digitos_pares:
            no_pares += 1
    if no_pares == 0:
        print(f"{etiquetas[i].capitalize()} DNI ({dnis[i]}): Conjunto par completo")
        encontrado = True

if not encontrado:
    print("Ningun conjunto es par completo.")