import tkinter as tk
import requests

def get_weather(city):
    api_key = "69892efc962ef52ab1f15456659595c3"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric", # Para obtener la temperatura en Celsius
        "lang": "es"      # Para obtener la descripción en español
    }
    try:
        response = requests.get(base_url, params=params)
        weather_data = response.json()

        if weather_data["cod"] == 200:
            temp = weather_data["main"]["temp"]
            humidity = weather_data["main"]["humidity"]
            description = weather_data["weather"][0]["description"]
            
            result_label.config(text=f"Temperatura: {temp}°C\nHumedad: {humidity}%\nDescripción: {description.capitalize()}")
        else:
            result_label.config(text=f"Error: {weather_data['message']}")
    except requests.exceptions.ConnectionError:
        result_label.config(text="Error: No se pudo conectar al servidor.")
    except Exception as e:
        result_label.config(text=f"Ocurrió un error: {e}")

# --- Configuración de la Interfaz Gráfica ---
app = tk.Tk()
app.title("App del Clima")
app.geometry("400x300")

# Estilo
app.configure(bg="#f0f0f0")
font_style = ("Arial", 12)
label_font_style = ("Arial", 14, "bold")

# Widgets
frame = tk.Frame(app, bg="#f0f0f0")
frame.pack(pady=20, padx=20, fill="both", expand=True)

city_label = tk.Label(frame, text="Ingresa una ciudad:", font=font_style, bg="#f0f0f0")
city_label.pack(pady=5)

city_entry = tk.Entry(frame, font=font_style, width=25)
city_entry.pack(pady=5)
city_entry.focus()

search_button = tk.Button(
    frame, 
    text="Consultar Clima", 
    font=font_style, 
    command=lambda: get_weather(city_entry.get()),
    bg="#4CAF50",
    fg="white",
    relief="flat"
)
search_button.pack(pady=10)

result_label = tk.Label(frame, text="", font=label_font_style, bg="#f0f0f0", justify="left", wraplength=350)
result_label.pack(pady=20)

# Iniciar la aplicación
app.mainloop()
