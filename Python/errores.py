aprendices = []

numeroPersona = int(input("Ingrese el numero de personas: ")) 
for i in range(numeroPersona):
    nombre = input("Introduce un nombre: ")
    edad = int(input(f"Introduce la edad de {nombre}: "))
    aprendices.append(nombre + " " + (edad)) 

print("Lista de Aprendices:", aprendices) 

nombre=None
mayorEdad = 0  
aprendizMayorEdad = "" 
for i in aprendices:  
        nombre= i.split()[0]
        edad = int(i.split()[-1])  
        if edad > mayorEdad:  
            mayorEdad = edad 
            aprendizMayorEdad = nombre 

print(f"Aprendiz con la mayor edad: {aprendizMayorEdad}\n")

nombreInstructora = input("Ingrese el nombre de la instructora: ")
aprendices.insert(1, nombreInstructora)
print(f"La instructora {nombreInstructora} ha sido agregada a la lista en la posición 1.")



contador= 0 
for i in aprendices:  
    if i.split()[-1] == 18: 
        contador += 1  


aprendices.append("Maria Alejandra 19 \n")


if nombreInstructora in aprendices: 
    aprendices.remove(nombreInstructora) 



dato = input("\nIngrese un dato para buscar en la lista de aprendices: ")


for i in aprendices:
    if dato in i:
        print(f"El dato {i} está presente en la lista de aprendices.")



print("\nLos primeros 10 aprendices de la lista:")
for i in range(min(10, len(aprendices))): 
    print(aprendices[i])


print("\nLos ultimos 10 aprendices de la lista:")
for i in range(max(0, len(aprendices) - 10), len(aprendices)):  
    print(aprendices[i])



print("\nLos aprendices del elemento 10 al elemento 20:")
for i in range(min(10, (aprendices)), min(20, (aprendices))):  
    print(aprendices[i])