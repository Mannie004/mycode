#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  take [weapon] 
''')
#added a new move "take"

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  # print the current weapon
  print('Weapons : ' + str(weapons))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  if "weapon" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['weapon'])
  
  print("---------------------------")

#an inventory, which is initially empty
inventory = []
weapons = []
#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key',
                  'weapon' : 'm4'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                  'weapon' : 'fist'
                },

            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
                  'north' : 'Pantry',
                  'east' : 'Lobby'
               },
            'Garden' : {
                  'north' : 'Dining Room',
                  'weapon' : 'ar50'
                
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie',
            },
            # added additional room
              'Lobby' : {
                  'west' : 'Dining Room',
                  'item' : 'potion', 
                  'weapon' : 'fireball'
            },
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

   #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

       # if monster is in the room, use weapon and if they type 'take' as first command
  if move[0] == 'take' :
    # if the room contains an item and also contains a monster, use a weapon
       #add the item to their inventory
    if 'weapon' in rooms[currentRoom] and move[1] == rooms[currentRoom]['weapon']:
      print('You picked up the ' + move[1])
      weapons.append(move[1])
      del rooms[currentRoom]['weapon']
    
 
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory :
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break
  # Create a scenario to kill monster
  elif currentRoom == 'Lobby' and 'monster' in inventory :
    print('The monsters flee in terror at the sight of your trophy... YOU WIN!')
    break
  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    if weapons: 
      print (' You killed a monster')
    else: 
      print('A monster has got you... GAME OVER!')
      break
