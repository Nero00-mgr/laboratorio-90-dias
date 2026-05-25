#Pídele al usuario su nombre y su edad, luego imprime:
#Hola Nero, tienes 23 años y en 10 años tendrás 33 años.

print("¿Cuál es tu Nombre?: ")
mi_nombre = input(">")
print("¿Cuántos años tienes?: ")
mi_edad = input(">")
print("Hola " + mi_nombre + ", tienes " + str(int(mi_edad)) + " años y en 10 años tendrás " + str(int(mi_edad) + 10) + " años")
