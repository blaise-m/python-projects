import os
from PIL import Image
from pathlib import Path
from pyzbar.pyzbar import decode


def decoder(qr_image):
	'''
	Takes in an image qrcode and returns the decoded data
	on the qr image
	'''

	open_image = Image.open(qr_image)
	return decode(open_image)


if __name__ == "__main__":

	base_path = Path().absolute()
	file_path = os.path.join(base_path, 'images')
	filename = 'blaise.png'
	
	data = decoder(os.path.join(file_path, filename))
	print(data)
