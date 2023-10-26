aprendices = []

numeroPersona = int(input("Ingrese el numero de personas: "))  #Aca estara el numero de personas que ingresaremos
for i in range(numeroPersona): #Iterar sobre el rango de valores de 0 a numeroPersona
    nombre = input("Introduce un nombre: ")
    edad = int(input(f"Introduce la edad de {nombre}: "))
    aprendices.append(nombre + " " + str(edad))  #Agregar el nombre y la edad a la lista "aprendices" en forma de cadena-.append agrega a la lista

print("Lista de Aprendices:", aprendices) #Imprimir la lista de aprendices

# Muestre el aprendiz con la mayor edad
nombre=None #Inicia la variable "nombre" con el valor None
mayorEdad = 0  #Inicia la variable "mayorEdad" en 0
aprendizMayorEdad = "" # Inicia la variable "aprendizMayorEdad" como una cadena vacia
for i in aprendices:  # Iterar sobre cada aprendiz en la lista
        nombre= i.split()[0] # Divide cada elemento de la lista aprendices en nombre y edad utilizando el metodo split()
        edad = int(i.split()[-1])  
        if edad > mayorEdad:  # Comparar la edad actual con la mayor edad registrada
            mayorEdad = edad #Actualizar la variable "mayorEdad" si la edad actual es mayor que la anterior
            aprendizMayorEdad = nombre #Asignar el nombre correspondiente a la mayor edad a la variable "aprendizMayorEdad"

print(f"Aprendiz con la mayor edad: {aprendizMayorEdad}\n")
#Inserte el nombre de la instructora en la posición 1
nombreInstructora = input("Ingrese el nombre de la instructora: ")
aprendices.insert(1, nombreInstructora)
print(f"La instructora {nombreInstructora} ha sido agregada a la lista en la posición 1.")


#Cuente cuantos aprendices tienen 18 años
contador= 0  # Inicializar el contador de 18 años

# Iterar sobre cada aprendiz en la lista "aprendices"
for i in aprendices:
    # Dividir cada elemento en nombre y edad utilizando el metodo split() y convertir la edad a un entero
    if i.split()[-1] == "18":  # Verificar si la edad es 18
        contador += 1  # Incrementar el contador si la edad es 18

# Imprimir el número de aprendices con 18 años
print(f"Número de aprendices con 18 años: {contador}")

#Agregue un aprendiz x al final de la lista

aprendices.append("Maria Alejandra 19 \n")

#Borrar el nombre de la instructora
if nombreInstructora in aprendices:  # Verifica si el nombre de la instructora está en la lista
    aprendices.remove(nombreInstructora) # Elimina el nombre de la instructora de la lista


# Solicitar al usuario que ingrese un dato para buscar en la lista
dato = input("\nIngrese un dato para buscar en la lista de aprendices: ")

# Verificar si el dato está presente en la lista de aprendices
for i in aprendices:
    if dato in i:
        print(f"El dato {i} está presente en la lista de aprendices.")


# Mostrar los primeros 10 aprendices de la lista
print("\nLos primeros 10 aprendices de la lista:")
for i in range(min(10, len(aprendices))):  # Iterar sobre los primeros 10 elementos o el número total de elementos si es menor que 10
    print(aprendices[i])

#Muestre los 10 ultimos aprendices de la lista
print("\nLos ultimos 10 aprendices de la lista:")
for i in range(max(0, len(aprendices) - 10), len(aprendices)):  # Iterar sobre los últimos 10 elementos o todos los elementos si hay menos de 10
    print(aprendices[i])


#Muestre del elemento 10 al elemento 20
print("\nLos aprendices del elemento 10 al elemento 20:")
for i in range(min(10, len(aprendices)), min(20, len(aprendices))):  # Iterar sobre los elementos del 10 al 20 o todos los elementos si hay menos de 20
    print(aprendices[i])
