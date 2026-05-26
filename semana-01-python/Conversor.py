#Pídele al usuario una temperatura en Celsius e imprímela convertida a Fahrenheit. La fórmula es:
#F = (C × 9/5) + 32 

celcius = float(input("Ingresa Temperatura en °C: "))
conversion = (celcius * 9/5) + 32
print(f"{celcius}°C equivalen a {conversion}°F")