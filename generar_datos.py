import random
import csv

# Generar 120 valores normales de temperatura (entre 2°C y 8°C)
normales_temperaturas = [round(random.uniform(2, 8), 2) for _ in range(120)]

# Generar 120 valores anormales de temperatura (mayores a 10°C)
anormales_temperaturas = [round(random.uniform(10.1, 15.0), 2) for _ in range(120)]

# Combinar las listas y mezclarlas
temperaturas = normales_temperaturas + anormales_temperaturas
random.shuffle(temperaturas)

# Generar 120 valores de humedad en el rango de 50% a 80%
normales_humedades = [round(random.uniform(50, 80), 2) for _ in range(120)]

# Generar 120 valores anormales de humedad en el rango de 80% a 100%
anormales_humedades = [round(random.uniform(80.1, 100), 2) for _ in range(120)]

# Combinar las listas de humedad y mezclarlas
humedades = normales_humedades + anormales_humedades
random.shuffle(humedades)

# Guardar en un archivo CSV
with open('temperaturas_y_humedades.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Temperatura", "Tipo Temperatura", "Humedad", "Tipo Humedad"])  # Escribir el encabezado
    for temp, humedad in zip(temperaturas, humedades):
        # Determinar el tipo de temperatura
        if temp <= 8:
            tipo_temperatura = "Normal"
        else:
            tipo_temperatura = "Anormal"

        # Determinar el tipo de humedad
        if humedad <= 80:
            tipo_humedad = "Normal"
        else:
            tipo_humedad = "Anormal"

        # Escribir los datos
        writer.writerow([f"{temp:.2f}", tipo_temperatura, f"{humedad:.2f}", tipo_humedad])
