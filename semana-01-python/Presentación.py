#Pídele al usuario: nombre, ciudad donde vive y su trabajo o carrera. Luego imprime una presentación completa en un solo párrafo usando f-strings. Algo como:
#Me llamo Nero, soy Ingeniero en Redes y vivo en Santiago.

nombre = str(input("Ingresa tu Nombre: "))
ciudad = str(input("Ingresa tu Ciudad: "))
trabajo = str(input("Trabajo o Carrera: "))

print(f"Me Llamo", nombre, ", soy ", trabajo, " y vivo en ", ciudad)