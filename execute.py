import os
import openai

# Establecer la clave de API de OpenAI usando una variable de entorno
os.environ[
    "OPENAI_API_KEY"] = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
openai.api_key = os.getenv("OPENAI_API_KEY")

# Función para obtener la respuesta de OpenAI basada en una alerta
def get_chat_completion(user_prompt):
    # Use the Chat Completion API to generate a response

    client = openai.Client()  # Create a client
    response = client.chat.completions.create(
        # Specify the chat model engine to use
        model="gpt-4o-mini",
        # Provide the user prompt as a message
        messages=[{"role": "user", "content": user_prompt}]
    )
    # Extract and return the generated response
    return response.choices[0].message.content.strip()

# Función para ejecutar la acción relacionada con la alerta
def execute_action(alert_message):
    print(f"Mensaje recibido: {alert_message}")

    # Usar la API para obtener un consejo sobre cómo manejar la alerta
    user_prompt = f"¿Qué debo hacer si se presenta esta alerta: {alert_message}?"
    advice = get_chat_completion(user_prompt)

    # Mostrar el consejo de la API
    print(f"Consejo de OpenAI: {advice}")

    # Aquí podrías agregar código adicional para ejecutar acciones específicas dependiendo de la alerta
    if "Temperatura fuera de rango" in alert_message:
        print("Ejecutando acción para controlar la temperatura...")
        # Llama a un código que controle la temperatura del sistema, como apagar un ventilador
    elif "Humedad fuera de rango" in alert_message:
        print("Ejecutando acción para ajustar la humedad...")
        # Llama a un código que controle la humedad, como activar una válvula
    else:
        print("Ejecutando acción genérica...")



