import os
import requests
from pprint import pprint


api_key = os.environ.get('OWM_API_KEY')


def get_weather(city):
	'''
	Takes in a city and returns its weather
	'''

	base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}'
	weather_data = requests.get(base_url).json()


if __name__ == "__main__":

	print("\nWELCOME TO MY WEATHER APP")
	print("****************************\n")
	city = input("Enter your city to get weather details: ")

	# Call the weather function
	city_weather = get_weather(city)

	# Display in a friendly format with pprint
	print("\n")
	pprint(city_weather)
