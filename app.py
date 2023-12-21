
'''
here is my origal app where I created the code to gather information from
Openweather using an API key.

I made this wanting to create a weather app for myself to find specific
weather information regarding ski conditions for myself to improve my
safety of terrain and areas

'''


import requests

api_key = 'bc4265dff9e2574698625dc68e768f5c'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

print(weather_data.json()) # returns a bunch of data about the location given

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['description'] #taking the weather out of the array
    temp = weather_data.json()['main']['temp'] # taking the temp out of the array
    feels_like = weather_data.json()['main']['feels_like'] # getting what the weather 'feels like'
    temp_min = weather_data.json()['main']['temp_min'] # getting max temperature
    temp_max = weather_data.json()['main']['temp_max'] # getting min temperature

    wind = weather_data.json()['wind']['speed'] # getting wind speed
    deg_num = weather_data.json()['wind']['deg'] # Turning degree into caridnal direction
    if 348.75 <= deg_num <= 360 or 0 <= deg_num < 11.25:
        deg = 'North'
    elif 11.25 <= deg_num < 33.75:
        deg = 'North-Northeast'
    elif 33.75 <= deg_num < 56.25:
        deg = 'Northeast'
    elif 56.25 <= deg_num < 78.75:
        deg = 'East Northeast'
    elif 78.75 <= deg_num < 101.25:
        deg = 'East'
    elif 101.25 <= deg_num < 123.75:
        deg = 'East Southeast'
    elif 123.75 <= deg_num < 146.25:
        deg = 'Southeast'
    elif 146.25 <= deg_num < 168.75:
        deg = 'South Southeast'
    elif 168.75 <= deg_num < 191.25:
        deg = 'South'
    elif 191.25 <= deg_num < 213.75:
        deg = 'South Southwest'
    elif 213.75 <= deg_num < 236.25:
        deg = 'Southwest'
    elif 236.25 <= deg_num < 258.75:
        deg = 'West Southwest'
    elif 258.75 <= deg_num < 281.25:
        deg = 'West'
    elif 281.25 <= deg_num < 303.75:
        deg = 'West Northwest'
    elif 303.75 <= deg_num < 326.25:
        deg = 'Northwest'
    elif 326.25 <= deg_num < 348.25:
        deg = 'North Northwest'
    else:
        deg = 'Invalid degree value'


    print(f"The weather in {user_input} right now is : {weather}.")
    print(f"With a low of {temp_min}°F and a high of {temp_max}°F")
    print(f"The temp in {user_input} is: {temp}°F, feels like {feels_like}°F")
    print(f"the wind speed is {wind} mph, going {deg}")
    try:
        gust = weather_data.json()['wind']['gust']
        print(f"with gusts of {gust}mph")
    except KeyError:
        print("Gust information not available.")





