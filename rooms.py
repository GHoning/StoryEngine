import room
import json
from pathlib import Path

#Load in one batch for now. Later we can add support for on the fly loading. Saves on memory cost.
rooms = []
roomFolder = Path('example')

roomm = room.room();

#create an array long enough.
for i in roomFolder.iterdir():
	rooms.append(room.room())

#fill the rooms
for roomFile in roomFolder.iterdir():
	with open(str(roomFile)) as json_file:
		data = json.load(json_file)
		curI = data["id"]
		rooms[curI].id = curI
		rooms[curI].description = data["description"]
		rooms[curI].options = []

		for p in data['options']:
			rooms[data["id"]].options.append(room.action(p['description'], p['goto']))

currentRoom = rooms[0]
running = True

#main loop.
while (running):
	#display user stuff
	print(currentRoom.description)

	prefix = 1

	for o in currentRoom.options :
		print(str(prefix)+". "+o.description)
		prefix = prefix + 1

	inp = input()
	print()

	if(inp == "0" or inp == "exit") :
		running = False
	elif(inp.isdigit()) :
		if(int(inp) <= len(currentRoom.options)) :
			val = currentRoom.options[int(inp) -1].goto
			currentRoom = rooms[val]
		else :
			print("invalid input")
	else :
		print("invalid input")
