
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 19:20:52 2022

@author: anamatias
"""

# define rooms and items



door_a = {
    "name": "door a",
    "type": "door",
}

door_b = {
    "name": "door b",
    "type": "door",
}

door_c = {
    "name": "door c",
    "type": "door",
}

door_d = {
    "name": "door d",
    "type": "door",
}

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}

key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}

doublebed = {
    "name": "double bed",
    "type": "furniture",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
}


diningtable = {
    "name": "dining table",
    "type": "furniture",
}
couch = {
    "name": "couch",
    "type": "furniture",
}

piano = {
    "name": "piano",
    "type": "furniture",
}

queenbed = {
    "name": "queen bed",
    "type": "furniture",
}

game_room = {
    "name": "game room",
    "type": "room",
}

bedroom1 = {
    "name": "bedroom 1",
    "type": "room",
}



bedroom2 = {
    "name": "bedroom 2",
    "type": "room",
}

livingroom = {
    "name": "living room",
    "type": "room",
}

outside = {
  "name": "outside"
}

all_rooms = [game_room, bedroom1, outside, livingroom, bedroom2]

all_doors = [door_a, door_b, door_c, door_d]


# define which items/rooms are related

object_relations = {
    "game room": [couch, piano, door_a],
    "piano": [key_a],
    "bedroom 1": [door_a, door_b, door_c, queenbed],
    "queen bed": [key_b],
    "bedroom 2": [door_b, dresser, doublebed],
    "double bed": [key_c],
    "dresser":[key_d],
    "living room": [door_c, door_d, diningtable],
    "outside": [door_d],
    "door a": [game_room, bedroom1],
    "door b": [bedroom1, bedroom2],
    "door c": [bedroom1, livingroom],
    "door d": [livingroom, outside],
}

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}







#PARA A INTERFACE:
    
import pygame
import sys   
pygame.font.init()

orange=(255,128,0)
green=(0,204,102)
blue=(51,153,255)
red=(255,255,51)

myfont = pygame.font.SysFont('Arial', 30)

screen=pygame.display.set_mode((1300,600))

#IMAGENS
img_door_a=pygame.image.load("/Users/anamatias/Desktop/IRONHACK/Project_week1/python-project/your-code/door_a.png")
img_door_a=pygame.transform.scale(img_door_a, (200,200))

img_piano=pygame.image.load("/Users/anamatias/Desktop/IRONHACK/Project_week1/python-project/your-code/piano.png")
img_piano=pygame.transform.scale(img_piano, (200,200))







# def wait(b):
#     #WAIT WHILE B IS TRUE
#     while b:
#         for event in pygame.event.get():
            
#             if event.type==pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()






def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    """
    Start the game
    """
    pygame.init()
    pygame.display.set_caption('Game Room')
    screen.fill(blue);
    pygame.display.flip()
    
    #POR INTERFACE A DIZER CLICK ANYWHERE TO CONTINUE!!
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                play_room(game_state["current_room"])
                
        
        

    
    
    #print("You wake up on a couch and find yourself in a strange house with no windows which you have never been to before. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!")
    #play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    
    #game_state["current_room"] = room
    
    
    
    
    screen.blit(img_door_a,(100,200))
    screen.blit(img_piano,(500,200))
    pygame.display.flip()
    
    
    
    
    
    
    
    
    
    # game_state["current_room"] = room
    # if(game_state["current_room"] == game_state["target_room"]):
    #     print("Congrats! You escaped the room!")
    # else:
    #     print("You are now in " + room["name"])
    #     intended_action = input("What would you like to do? Type 'explore' or 'examine'?").strip()
    #     if intended_action == "explore":
    #         explore_room(room)
    #         play_room(room)
    #     elif intended_action == "examine":
    #         examine_item(input("What would you like to examine?").strip())
    #     else:
    #         print("Not sure what you mean. Type 'explore' or 'examine'.")
    #         play_room(room)
    #     linebreak()







def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))

def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if(not current_room == room):
            return room

def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been 
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None
    
    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            output = "You examine " + item_name + ". "
            if(item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    output += "You unlock it with a key you have."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "It is locked but you don't have the key."
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                else:
                    output += "There isn't anything interesting about it."
            print(output)
            break

    if(output is None):
        print("The item you requested is not found in the current room.")
    
    if(next_room and input("Do you want to go to the next room? Enter 'yes' or 'no'").strip() == 'yes'):
        play_room(next_room)
    else:
        play_room(current_room)


game_state = INIT_GAME_STATE.copy()

start_game()