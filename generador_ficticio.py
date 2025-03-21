import random
import csv

# Generar 120 valores normales (entre 0 y 7 grados)
normales = [round(random.uniform(0, 7), 2) for _ in range(120)]

# Generar 120 valores anormales (mayores a 10 grados)
anormales = [round(random.uniform(10.1, 15.0), 2) for _ in range(120)]

# Combinar las listas y mezclarlas
temperaturas = normales + anormales
random.shuffle(temperaturas)

# Guardar en un archivo CSV
with open('temperaturas.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Temperatura", "Tipo"])  # Escribir el encabezado
    for temp in temperaturas:
        if temp <= 7:
            writer.writerow([f"{temp:.2f}", "Normal"])
        else:
            writer.writerow([f"{temp:.2f}", "Anormal"])