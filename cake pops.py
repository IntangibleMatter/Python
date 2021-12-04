pops = 1
time = 19.0

while time <= 24.0:
	pops = pops / 2
	time = time + 0.5

while time >= 0:
	print("At " + str(time) + " O'clock Cadence may have " + str(pops) + "cake pops.")
	time = time - 0.5
	pops = pops * 2	
	
input("Press enter to close")