import os
import qrcode
from pathlib import Path


data = {
	'name': 'blaise',
	'age': 30
}


base_dir = Path().absolute()
file_path = os.path.join(base_dir, 'images')


def encoder(data):
	'''
	Takes in a data objects and encodes it into a qrcode
	'''

	img = qrcode.make(data)
	img.save(os.path.join(file_path, 'blaise.png'))


if __name__ == "__main__":
	# Call function if module is run directly
	encoder(data)
