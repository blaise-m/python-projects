import os
from pathlib import Path


def main():
	
	# Get the filepath
	base_dir = Path().absolute()
	file_path = os.path.join(base_dir, 'files')
	file_list = os.listdir(file_path)

	for index, file_name in enumerate(file_list):
		new_name = "Bond_Indeture_" + str(index) + ".pdf"

		source_path = os.path.join(file_path, file_name)
		destination_path = os.path.join(file_path, new_name)

		os.rename(source_path, destination_path)


if __name__ == '__main__':
	# Run the main function if module
	# is run directly
	main()
