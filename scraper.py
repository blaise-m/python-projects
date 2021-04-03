import requests
from bs4 import BeautifulSoup as bs
from PIL import Image


def format_response(response):
	'''
	Takes in a response and uses bs4 to extract the required html
	And returns it
	'''

	soup = bs(response.content, 'html.parser')
	div_tag = soup.find('div', {'class': ['h-card']})
	img_tag = div_tag.find('img', {'class': ['avatar', 'avatar-user']})
	img_url = img_tag['src']
	
	return img_url


def return_github_img(username):
	'''
	Takes in a github username and returns the url
	of the github image
	'''
 
	base_url = 'https://github.com/'
	user_url = base_url + username
	
	response = requests.get(user_url)
	img_url = format_response(response)

	return img_url


def display_img(img_url):
	'''
	Takes in an image url
	Makes a get request to retrive the image
	Opens the image in the default image viewer
	'''

	response = requests.get(img_url, stream=True).raw
	img = Image.open(response)
	img.show()


if __name__ == '__main__':

	# Welcome message
	print("\nVIEW YOUR GITHUB PIC APP")
	print("*************************\n\n")

	# Request user for github username
	username = input("Enter your github username: ")

	# Call the function with the username
	img_url = return_github_img(username)

	display_img(img_url)
