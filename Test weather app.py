'''

Here is the unofficial official "Asher's weather app"
I used Tkinter to create a weather app poop up that takes in
a city and spits out
What the weather is like currently,
High and Low temperature on the day,
Current temperature,
Wind speed and direction,
And if there is gust information, the gust information.

'''



import tkinter as tk
from tkinter import messagebox
import requests



def get_weather():
	city = city_entry.get()

	api_key = 'bc4265dff9e2574698625dc68e768f5c'
	weather_data = requests.get(
		f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

	if weather_data.status_code == 404:
		messagebox.showerror("Error", "City not found")
	else:
		weather = weather_data.json()['weather'][0]['description']
		temp = weather_data.json()['main']['temp']
		feels_like = weather_data.json()['main']['feels_like']
		temp_min = weather_data.json()['main']['temp_min']
		temp_max = weather_data.json()['main']['temp_max']
		wind = weather_data.json()['wind']['speed']
		deg_num = weather_data.json()['wind']['deg']

		# Convert degree to cardinal direction
		cardinal_directions = ['North', 'North-Northeast', 'Northeast', 'East Northeast', 'East', 'East Southeast',
		                       'Southeast', 'South Southeast', 'South', 'South Southwest', 'Southwest',
		                       'West Southwest', 'West', 'West Northwest', 'Northwest', 'North Northwest']
		index = round(deg_num / 22.5) % 16
		deg = cardinal_directions[index] # Gets cardinal direction from array

		weather_info = ( # Presenting weather information
			f"The weather in {city} right now is: {weather}.\n"
			f"With a low of {temp_min}°F and a high of {temp_max}°F.\n"
			f"The temperature in {city} is: {temp}°F, feels like {feels_like}°F.\n"
			f"The wind speed is {wind} mph, going {deg}."
		)

		try:
			gust = weather_data.json()['wind']['gust']
			weather_info += f"\nWith gusts of {gust} mph."
		except KeyError:
			weather_info += "\nGust information not available."

		result_label.config(text=weather_info)

'''def set_background_color(weather_description):
	# Define background colors based on weather description
	color_mapping = {
	'clear sky' : 'skyblue',
	'few clouds': 'lightblue',
	'scattered clouds': 'gray',
	'broken clouds': 'darkgray',
	'shower rain': 'lightgray',
	'rain': 'steelblue',
	'thunderstorm': 'darkblue',
	'snow': 'snow',
	'mist': 'lightgray',
	}

	color = color_mapping.get(weather_description.lower(),'white')
	root.configure(background=color) '''


# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("800x600")

# Create entry widget for city input
city_entry = tk.Entry(root)
city_entry.pack(pady=20)

# Create button to get weather
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=20)

# Create label to display result
result_label = tk.Label(root, text="")
result_label.pack(pady=25)

# Start the main event loop
root.mainloop()
