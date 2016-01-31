import requests 
#use the api of openweathermap to know the weather
def get_weather_forecast():
    #consume API
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Guadalajara,mx&units=metric&appid=81f527ece7b1f5d6b47c23d1d6767c3d'
    weather_json = requests.get(url).json()
    #parse json
    weather_description = weather_json['weather'][0]['description']
    max_temp = weather_json['main']['temp_max']
    min_temp = weather_json['main']['temp_min']
    #build string
    forecast = 'The Circus forecast for today is '
    forecast += weather_description + ' with a high of '
    forecast += str(max_temp) + ' and low of ' +  str(min_temp) + '.'

    return forecast
