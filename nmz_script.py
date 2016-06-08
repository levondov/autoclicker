import subprocess
import time
import random

# autoclicker developed for NMZ zone prayer restore clicking
# runnable only on linux systems
# ----------------------
# Levon Dovlatyan
# version 0.1
# 8 June 2016
# ----------------------

random.seed() # initialize random seed generator - use current system time as the hashable object

while True:
	
	# move mouse over the correct point on the screen
	# use the 'xdotool getmouselocation' command in terminal to get coordinates for current location
	mouse_X = 618
	mouse_Y = 307
	subprocess.call(["xdotool", "mousemove", str(mouse_X), str(mouse_Y)])
	
	# press down on the mouse
	subprocess.call(["xdotool", "mousedown", "1"])
	
	# sleep for a random interval between 0.1-0.8 seconds
	upper_range = random.randint(50,80)
	lower_range = random.randint(10,30)
	time.sleep(random.randint(lower_range,upper_range) / 100.0)
	
	# release mouse click
	subprocess.call(["xdotool", "mouseup", "1"])
	
	# random delay before next click
	upper_range = random.randint(75,110)
	lower_range = random.randint(10,30)
	time.sleep(random.randint(lower_range,upper_range) / 100.0)
	
	# repeat to turn off prayer
	subprocess.call(["xdotool", "mousedown", "1"])
	upper_range = random.randint(50,80)
	lower_range = random.randint(10,30)
	time.sleep(random.randint(lower_range,upper_range))
	subprocess.call(["xdotool", "mouseup", "1"])
	
	#sleep for random interval between 20-55 seconds
	time.sleep(random.randint(15,55))