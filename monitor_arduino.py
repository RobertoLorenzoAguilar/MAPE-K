# monitor_arduino.py
import serial
import time

class SerialMonitor:
    def __init__(self, port='/dev/cu.usbmodem1112401', baudrate=9600, timeout=1):
        self.ser = serial.Serial(port, baudrate, timeout=timeout)

    def get_data(self):
        if self.ser.in_waiting > 0:
            line = self.ser.readline().decode('utf-8').strip()
            print(f"Datos recibidos: {line}")  # Imprime los datos para depuración
            try:
                # Dividir la línea en "Humidity" y "Temperature"
                if 'Humidity' in line and 'Temperature' in line:
                    humidity_part, temperature_part = line.split('  ')  # Separar por dos espacios
                    # Ahora procesamos cada parte individualmente
                    humidity = humidity_part.split(':')[1].strip()  # Humidity value
                    temperature = temperature_part.split(':')[1].strip()  # Temperature value
                    return humidity, temperature  # Retorna ambos valores
                else:
                    print(f"Error: los datos no contienen 'Humidity' o 'Temperature' correctamente: {line}")
                    return None, None  # Retorna None si no están bien formateados
            except ValueError:
                print(f"Error: la línea no tiene el formato esperado: {line}")
                return None, None  # Retorna None si no se puede dividir correctamente
        return None, None

    def close(self):
        self.ser.close()

# Monitoreo continuo
if __name__ == "__main__":
    monitor = SerialMonitor()

    try:
        while True:
            humidity, temperature = monitor.get_data()
            if humidity and temperature:
                print(f"Lectura en tiempo real: Humedad = {humidity}%, Temperatura = {temperature}°C")
            time.sleep(1)  # Espera de 1 segundo entre lecturas
    except KeyboardInterrupt:
        print("\nCerrando conexión...")
        monitor.close()
