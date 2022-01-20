#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 19:20:52 2022

@author: anamatias
"""





#PARA A INTERFACE:
    
import pygame
import sys   








pygame.font.init()

orange=(197,90,17)
green=(0,128,0)
blue1=(30,144,255)
blue2=(65,105,225)
blue3=(0,65,106)
red=(255,255,51)
yellow=(255,255,0)
white=(255,255,255)
grey=(70,70,70)

myfont = pygame.font.SysFont('Arial', 30)

myfont_1 = pygame.font.SysFont('Arial', 20)

screen=pygame.display.set_mode((1270,600))











#IMAGENS



img_start=pygame.image.load("start.png")
img_start=pygame.transform.scale(img_start, (1270,600))




img_end=pygame.image.load("end.png")
img_end=pygame.transform.scale(img_end, (1270,600))




img_key_a=pygame.image.load("key_a.png")
img_key_a=pygame.transform.scale(img_key_a, (60,60))


img_key_b=pygame.image.load("key_b.png")
img_key_b=pygame.transform.scale(img_key_b,(60,60))

img_key_c=pygame.image.load("key_c.png")
img_key_c=pygame.transform.scale(img_key_c, (60,60))

img_key_d=pygame.image.load("key_d.png")
img_key_d=pygame.transform.scale(img_key_d, (60,60))






img_door_a=pygame.image.load("door_a.png")
img_door_a=pygame.transform.scale(img_door_a, (200,200))

img_door_b=pygame.image.load("door_b.png")
img_door_b=pygame.transform.scale(img_door_b, (200,200))

img_door_c=pygame.image.load("door_c.png")
img_door_c=pygame.transform.scale(img_door_c, (200,200))

img_door_d=pygame.image.load("door_d.png")
img_door_d=pygame.transform.scale(img_door_d, (200,200))





img_piano=pygame.image.load("piano.png")
img_piano=pygame.transform.scale(img_piano, (200,200))

img_couch=pygame.image.load("couch.png")
img_couch=pygame.transform.scale(img_couch, (200,200))

img_dresser=pygame.image.load("dresser.png")
img_dresser=pygame.transform.scale(img_dresser, (200,200))

img_bed=pygame.image.load("bed.png")
img_bed=pygame.transform.scale(img_bed, (200,200))

img_table=pygame.image.load("table.png")
img_table=pygame.transform.scale(img_table, (200,200))




# define rooms and items



door_a = {
    "name": "door a",
    "type": "door",
    "image":img_door_a,
}

door_b = {
    "name": "door b",
    "type": "door",
    "image":img_door_b,
}

door_c = {
    "name": "door c",
    "type": "door",
    "image":img_door_c,
}

door_d = {
    "name": "door d",
    "type": "door",
    "image":img_door_d,
}

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
    "image":img_key_a,
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
    "image":img_key_b,
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
    "image":img_key_c,
}

key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
    "image":img_key_d,
}

doublebed = {
    "name": "double bed",
    "type": "furniture",
    "image":img_bed,
}

dresser = {
    "name": "dresser",
    "type": "furniture",
    "image":img_dresser,
}


diningtable = {
    "name": "dining table",
    "type": "furniture",
    "image":img_table,
}
couch = {
    "name": "couch",
    "type": "furniture",
    "image":img_couch,
}

piano = {
    "name": "piano",
    "type": "furniture",
    "image":img_piano,
}

queenbed = {
    "name": "queen bed",
    "type": "furniture",
    "image":img_bed,
}






game_room = {
    "name": "game room",
    "type": "room",
    "color": blue1,
}

bedroom1 = {
    "name": "bedroom 1",
    "type": "room",
    "color": green,
}
bedroom2 = {
    "name": "bedroom 2",
    "type": "room",
    "color": blue2,
}

livingroom = {
    "name": "living room",
    "type": "room",
    "color": blue3,
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








def show_keys(list_keys):
    
    if list_keys:
        
        screen.blit(myfont_1.render('keys you have:', False, white),(15,500))
        
        
        p=60
        for k in list_keys:
            screen.blit(k["image"],(p,530))
            p+=60
            
        pygame.display.update()






def start_game():
    """
    Start the game
    """
    pygame.init()
    pygame.display.set_caption('Start')
    
    screen.blit(img_start,(0,0))
    
    pygame.display.flip()
    
    
    
    b=True
    while b:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type==pygame.KEYDOWN:    
                if event.key == pygame.K_RETURN: 
                    play_room(game_state["current_room"])
                    b=False    
            
 
    
 
    
 
    
 

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    
    game_state["current_room"] = room
    
    
    if(game_state["current_room"] == game_state["target_room"]):
        
        pygame.mixer.init()
        pygame.mixer.music.load('yay.mp3')
        pygame.mixer.music.play()
        
        while True:
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.set_caption('Congrats! You escaped the room!')
            screen.blit(img_end,(0,0))
            pygame.display.flip()
        
        
        
        
        
        
        
    else:
        
       
        pygame.display.set_caption(room['name'].upper())
        screen.fill(room['color'])
        screen.blit(myfont.render(room['name'].upper(), False, white),(50,80))
        
        show_keys(game_state['keys_collected']) 
        
        #pygame.display.flip()
        items1=explore_room(room)
        
        b=True
        while b:
            
            for event in pygame.event.get():
                
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                
                if event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                   
                    
                    if 200<y<400:
                        
                        if 100<x<300:
                            examine_item(items1[0])
                            
                            
                        elif 400<x<600:
                            examine_item(items1[1])
                        elif 700<x<900:
                            examine_item(items1[2])
                        elif len(items1)>3 and 1000<x<1200:
                            examine_item(items1[3])
                             
                         
                    
                    
            
    
    





def explore_room(room):
    
    
    """
    Explore a room. List all items belonging to this room.
    """
    #items = [i["name"] for i in object_relations[room["name"]]]
    
    #print(items)
    
    p=100
    items=[]
    for obj in object_relations[room["name"]]:
        screen.blit(obj["image"],(p,200))
        items.append(obj["name"])
        p+=300
    
    pygame.display.flip()
    
    return items














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
                    
                    pygame.mixer.init()
                    pygame.mixer.music.load('unlock.mp3')
                    pygame.mixer.music.play()
                    
                    
                    
                    next_room = get_next_room_of_door(item, current_room)
                    
                    
                else:
                    output += "It is locked but you don't have the key."
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                    
                    pygame.mixer.init()
                    pygame.mixer.music.load('key.mp3')
                    pygame.mixer.music.play()
                    
                else:
                    output += "There isn't anything interesting about it."
             
            break
        
        
        
        
        
        
        
        
        
        
        
        
            
    screen.fill(current_room['color'])
    screen.blit(myfont.render(output, False, white),(50,100))
    
    #screen.blit(myfont.render('Press anywhere to continue', False, white),(50,300))
    
    show_keys(game_state['keys_collected']) 
    
    

        
                

    # if(output is None):
    #     print("The item you requested is not found in the current room.")
   
   
    if next_room:
        
        screen.blit(myfont.render('Press ENTER to go to the next room.', False, white),(50,300))
        screen.blit(myfont.render('Press BACKSPACE stay in the same room', False, white),(50,350))
        pygame.display.flip()
        
        
        b=True
        while b:




            
            for event in pygame.event.get():
                
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                
                # elif event.type == pygame.MOUSEBUTTONUP:
                #     play_room(current_room)
                #     b=False
                    
                elif event.type==pygame.KEYDOWN:    
                    if event.key == pygame.K_BACKSPACE: 
                        play_room(current_room)
                        b=False
                    if event.key == pygame.K_RETURN:
                        play_room(next_room)
                        b=False
        
       
    else:
        
        screen.blit(myfont.render('Press ENTER to continue', False, white),(50,300))
        pygame.display.flip()
        
        b=True
        while b:
            
            for event in pygame.event.get():
                
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                
                elif event.type==pygame.KEYDOWN:    
                    if event.key == pygame.K_RETURN: 
                        play_room(current_room)
                        b=False
              
        














game_state = INIT_GAME_STATE.copy()

start_game()
