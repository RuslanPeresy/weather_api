import json
import requests

def get_forecast(cityname, apikey):

	url = 'http://api.openweathermap.org/data/2.5/weather'
	r = requests.get(url, params=dict(q=cityname, APPID=apikey))
	weather_data = json.loads(r.content)
	if r.status_code == 200:

		# Переводим температуру из градусов Кельвина в градусы Цельсия
		tempK = weather_data['main']['temp']
		tempC = tempK - 273
		tempC = f"{tempC:.{2}f}"	
	
		result = {
			'status': True,
			'desc': 'Forecast is obtained',
			'main': weather_data['weather'][0]['main'],
			'temp': tempC,
			'pressure': weather_data['main']['pressure'],
			'humidity': weather_data['main']['humidity'],
			'wind': weather_data['wind']['speed'],
			'error_code': 0
		}
	else:
		result = {
			'status': False,
			'desc': weather_data['message'],
			'error_code': r.status_code
		}

	return result

