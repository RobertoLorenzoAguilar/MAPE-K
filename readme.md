# MAPE-K: Cómputo Autónomo  
![image](https://github.com/user-attachments/assets/e2851249-8f92-46e3-9bec-997fe9972e65)

## Descripción  

Este sistema implementa el modelo **MAPE-K** para el monitoreo y control de la temperatura y humedad mediante un Arduino con un sensor **DHT11**. Su propósito es analizar las lecturas obtenidas, clasificarlas según reglas predefinidas y tomar decisiones en función de los resultados.  

## Funcionamiento  

### 1. Monitoreo  
- El sistema recibe datos a través del puerto serial desde un **Arduino** con un sensor **DHT11**.  
- Un módulo de **monitor** lee estas lecturas mediante un método específico del puerto serial.  

### 2. Análisis  
- Una clase de **análisis** procesa los datos obtenidos y los compara con reglas predefinidas en una base de conocimiento (**Knowledge**).  
- Estas reglas fueron inicialmente categorizadas en un archivo **Excel**, diferenciando datos normales y anormales.  
- Posteriormente, la información se importó a la herramienta de IA **Weka**, donde se aplicó el algoritmo **Naive Bayes**. Se eligió este método debido a la correlación entre temperatura y humedad, evitando la exclusión de variables que ocurre con algoritmos como **J48**.  

### 3. Planificación  
- El módulo de **planeación** consulta el analizador en busca de alertas basadas en el monitoreo y la base de conocimiento.  
- Si se detecta una anomalía, se envían los datos al **ejecutor**.  

### 4. Ejecución  
- El ejecutor realiza una consulta a **OpenAPI** para obtener recomendaciones sobre cómo mantener la temperatura en un rango óptimo.  
- Un caso hipotético sería la conservación de vacunas en condiciones ideales.  


