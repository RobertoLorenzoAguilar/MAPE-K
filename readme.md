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


primero se guardan los datos obtenidos para posteriormente categorizar
normal- temperatura
anormal- temperatura
normal- humedad
anormal- humedad

![image](https://github.com/user-attachments/assets/b284def0-41b4-4c13-b788-9b0ec9ba1b37)


Se importa  a Weka

![image](https://github.com/user-attachments/assets/037987a4-b77c-41ac-af3f-c9ae4107a429)


Mediante  OpenFile
asegurate de selecionar el formato debido como .csv en este caso


![image](https://github.com/user-attachments/assets/a0539c85-df19-4da1-92c0-f830d1568f54)


Asegurate de que todo este bien, que los datos esten en su formato

![image](https://github.com/user-attachments/assets/442e2577-39fb-4681-99f7-b3d56ad2fa6d)

Despues seleccionar el clasificador la pestaña
![image](https://github.com/user-attachments/assets/83f23267-de84-4834-8dcf-277388df7881)


Despues señeccionarel tipo de clasificador 
![image](https://github.com/user-attachments/assets/90a4649d-f45d-4f3e-9c73-65ffab18f5a2)


Al darle start te generara el conocimiento

![image](https://github.com/user-attachments/assets/96aec125-cc4d-45fb-aa7d-b2edd41e0ab2)

para analizar tus limites por variable temperatura, humedad

en base  a ello puedes generar tu umbral de tolerancia 

![image](https://github.com/user-attachments/assets/c7807ed6-3a12-4191-ae06-08b818af9eff)


esto es lo que llama el analizador para considerar si alerta o no



este es el codigo de Arduino para imprimir el valor del sensor en serial

![image](https://github.com/user-attachments/assets/65360efe-dd43-470b-bc8d-dd293168a292)














