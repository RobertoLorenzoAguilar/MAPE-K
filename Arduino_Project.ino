#include <DHT.h>
#include <Wire.h>
#include <BH1750.h>


#define DHTPIN 2          // Pin where the DHT11 data line is connected
#define DHTTYPE DHT11     // Define the sensor type as DHT11

DHT dht(DHTPIN, DHTTYPE);  // Initialize the DHT sensor

void setup() {
  Serial.begin(9600);        // Start the serial communication
  dht.begin();               // Initialize the DHT sensor
}

void loop() {
  // Wait a few seconds between measurements.
  delay(500);  // Delay of 2 seconds

  // Read the humidity and temperature
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();  // For Celsius

  // Check if the readings failed
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Print the results to the Serial Monitor
  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.print("%  Temperature: ");
  Serial.print(temperature);
  Serial.println("C");
}
