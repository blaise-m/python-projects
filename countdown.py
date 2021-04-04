import time


def countdown(time_in_seconds):
	'''
	Takes in time in seconds
	And prints the formatted time counting down
	'''

	seconds_per_minute = 60
	print("\n")

	while time_in_seconds:
		# divmod retuns a tuple with the quotient and divisor
		# if argument1 is divided by argument2

		mins, secs = divmod(time_in_seconds, seconds_per_minute)
		timer = f'{mins:02d}:{secs:02d}'
		
		# "\r" puts the cursor at the beginning of the line
		# and continues printing the output as usual
		# in our case, the new value for timer replaces the previous
		# value in every iteration

		print(timer, end="\r")
		time.sleep(1)

		time_in_seconds -= 1

	print("\n\nCountdown complete!!!!")


if __name__ == "__main__":

	print("\nWELCOME TO APP COUNTDOWN")
	print("**************************\n\n")

	time_to_countdown = int(input("Enter the seconds to countdown: "))
	
	# Call function
	countdown(time_to_countdown)
