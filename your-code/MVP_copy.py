#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 19:20:52 2022

@author: anamatias
"""





#PARA A INTERFACE:
    
import pygame
import sys   
import time



pygame.font.init()

orange=(197,90,17)
green=(102,124,38)
blue1=(30,144,255)
blue2=(65,105,225)
blue3=(0,65,106)
red=(255,255,51)
yellow=(255,255,0)
white=(255,255,255)
grey=(142,142,142)

myfont = pygame.font.SysFont('Arial', 30)

myfont_1 = pygame.font.SysFont('Arial', 20)

screen=pygame.display.set_mode((1270,600))







#IMAGENS



img_start=pygame.image.load("start.png")
img_start=pygame.transform.scale(img_start, (1270,600))


img_over=pygame.image.load("over.png")
img_over=pygame.transform.scale(img_over, (1270,600))

img_end=pygame.image.load("end.png")
img_end=pygame.transform.scale(img_end, (1270,600))




img_en_g=pygame.image.load("en_g.png")
img_en_g=pygame.transform.scale(img_en_g, (10,60))

img_en_y=pygame.image.load("en_y.png")
img_en_y=pygame.transform.scale(img_en_y, (10,60))

img_en_r=pygame.image.load("en_r.png")
img_en_r=pygame.transform.scale(img_en_r, (10,60))





img_key_a=pygame.image.load("key_a.png")
img_key_a=pygame.transform.scale(img_key_a, (60,60))


img_key_b=pygame.image.load("key_b.png")
img_key_b=pygame.transform.scale(img_key_b,(60,60))

img_key_c=pygame.image.load("key_c.png")
img_key_c=pygame.transform.scale(img_key_c, (60,60))

img_key_d=pygame.image.load("key_d.png")
img_key_d=pygame.transform.scale(img_key_d, (60,60))





img_potion=pygame.image.load("potion.png")
img_potion=pygame.transform.scale(img_potion, (200,200))




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

img_table=pygame.image.load("crown.png")
img_table=pygame.transform.scale(img_table, (200,200))

img_shield=pygame.image.load("shield.png")
img_shield=pygame.transform.scale(img_shield, (200,200))

img_painting=pygame.image.load("painting.png")
img_painting=pygame.transform.scale(img_painting, (200,200))



# define rooms and items


potion = {
    "name": "potion",
    "type": "potion",
    "image":img_potion,
}






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
    "name": "Diana Painting",
    "type": "furniture",
    "image":img_painting,
}

dresser = {
    "name": "dresser",
    "type": "furniture",
    "image":img_dresser,
}


diningtable = {
    "name": "Queen's Crown",
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
    "name": "William's bed",
    "type": "furniture",
    "image":img_bed,
}

shield = {
    "name": "shield",
    "type": "furniture",
    "image":img_shield,
}




game_room = {
    "name": "Entry Hall",
    "type": "room",
    "color": blue1,
}

bedroom1 = {
    "name": "William's Bedroom",
    "type": "room",
    "color": green,
}
bedroom2 = {
    "name": "Harry's Bedroom",
    "type": "room",
    "color": blue2,
}

livingroom = {
    "name": "Queen's Bedroom",
    "type": "room",
    "color": blue3,
}


outside = {
  "name": "outside"

}






all_rooms = [game_room, bedroom1, outside, livingroom, bedroom2]

all_doors = [door_a, door_b, door_c, door_d]

max_en=35

max_time=100


start_time=0



# define which items/rooms are related

object_relations = {
    "Entry Hall": [door_a, piano, door_c, potion],
    "piano": [key_a],
    "William's Bedroom": [door_a, queenbed, door_b, shield],
    "William's bed": [key_b],
    "shield": [key_c],
    "Harry's Bedroom": [door_b, dresser, doublebed],
    "Queen's Bedroom": [door_c, diningtable, door_d],
    "Queen's Crown": [key_d],
    "outside": [door_d],
    "door a": [game_room, bedroom1],
    "door b": [bedroom1, bedroom2],
    "door c": [game_room, livingroom],
    "door d": [livingroom, outside],
}

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside,
    "energy": max_en,
}




# def game_over():
    

    
#     #GAMEOVER
    
#     pygame.display.set_caption('GAME OVER')
#     screen.blit(img_over,(0,0))
#     pygame.display.flip()
            
    
#     # pygame.mixer.init()
#     # pygame.mixer.music.load('yay.mp3')
#     # pygame.mixer.music.play()
    
    
 
#     b=True
#     while b:
        
        

        
#         for event in pygame.event.get():
#             if event.type==pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
                
#             elif event.type==pygame.KEYDOWN:    
#                 if event.key == pygame.K_RETURN: 
#                     game_state = INIT_GAME_STATE.copy()
#                     start_game()
#                     return game_state
#                     b=False
                  

    


def game_over():
    pygame.display.set_caption('GAME OVER')
    screen.blit(img_over,(0,0))
    pygame.display.flip()

 
    b=True
    while b:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
    




def show_keys(list_keys, en):
    
    
    
    if en<=0:
        game_over()
        

        
    else:
        
        if en>(2*max_en)/3:
            img_en=img_en_g
        elif en>max_en/3:
            img_en=img_en_y
        else:
            img_en=img_en_r
            
        
        screen.blit(myfont_1.render('energy:', False, white),(15,500))
        
        p=60
        for i in range(0,en):
            screen.blit(img_en,(p,530))
            p+=14
        
        
        
        
        
    
    if list_keys:
        
        screen.blit(myfont_1.render('keys you have:', False, white),(600,500))
        
        
        p=660
        for k in list_keys:
            screen.blit(k["image"],(p,530))
            p+=60
            
    pygame.display.update()






def start_game():
    """
    Start the game
    """
    
    
    # global nome
    # nome=''

    # while nome=='':

    #     nome=input('What is your name').strip()
        
        
        
        
        
    # global nome
    # nome=input('What is your name').strip()
    
    
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
                    
                    
                    
                    global start_time
                    
                    start_time=time.time()
                    
                    # f=open('resultados.txt',w+)
                    # f.write('Resultados')
                    # f.close()
                    
                    
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
        
        end_time=time.time()
        
        
        
        
        pygame.display.set_caption('Congrats!')
        screen.blit(img_end,(0,0))
        screen.blit(myfont.render("Your time was "+str(int(round((end_time - start_time),0)))+" seconds.", False, (47,85,151)),(300,125))
        
        
        
        pygame.display.flip()
    
        
        while True:
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            
        
        
            #round((time.time() - start_time),1)
        
        
        
    else:
        
        
      
        pygame.display.set_caption(room['name'])
        screen.fill(room['color'])
        screen.blit(myfont.render(room['name'], False, white),(50,80))
        
        show_keys(game_state['keys_collected'],game_state['energy']) 
        
        
        #pygame.display.flip()
        items1=explore_room(room)
        
        b=True
        while b:
            
            
            
            temp_surface = pygame.Surface((195,40))
            temp_surface.fill((grey))
            #temp_surface.blit(text, (0, 0))
            screen.blit(temp_surface, (1060,10))
            
            
            
            screen.blit(myfont_1.render('Remaining time: '+str(100-int(round((time.time()- start_time),0))), False, white),(1070,20)) #contartempo
            
            
            if int(round((time.time()- start_time),0))>max_time: game_over()
            
            
            pygame.display.flip()
            
            
            
            
            
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
    
    game_state['energy']-=1 
    
    current_room = game_state["current_room"]
    next_room = ""
    output = None
    
    for item in object_relations[current_room["name"]]:
        
        if(item["type"] == "potion"):
            
            
            
            
            # print(max_en)
            # print(game_state['energy'])
            # print(game_state['energy']<max_en-1)
            
            if game_state['energy']+1>=max_en/3:
    
    
                output='You examine this bottle and realize it is an energy potion.' #'You are afraid of possible side effects so you put it back.'
                output2='You are afraid of possible side effects so you put it back.'
                #screen.blit(myfont.render('You are afraid of possible side effects so you put it back.', False, white),(50,300))
                
                
              
            else:
                
                print(current_room["name"])
                print(item["type"])
                print(item)
              
                
                game_state['energy']=max_en


                output='You examine this bottle and realize it is an energy potion.' #You are feeling really tired so you drink it out of desperation and feel energized.'
                output2='You are feeling really tired so you drink it out of desperation and feel energized.'
                #screen.blit(myfont.render('You are feeling really tired so you drink it out of desperation and feel energized.', False, white),(50,300))
               
                
        
        
        
        
        
        elif(item["name"] == item_name):
            
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
    if(item["type"] == "potion"): screen.blit(myfont.render(output2, False, white),(50,150))
        
    
    
    
    
    
    #screen.blit(myfont.render('Press anywhere to continue', False, white),(50,300))
    
    show_keys(game_state['keys_collected'],game_state['energy']) 
    
    
    

        
                

    # if(output is None):
    #     print("The item you requested is not found in the current room.")
   
   
    if next_room:
        
        screen.blit(myfont.render('Press ENTER to go to the next room.', False, white),(50,300))
        screen.blit(myfont.render('Press BACKSPACE stay in the same room', False, white),(50,350))
        pygame.display.flip()
        
        
        b=True
        while b:
            
            temp_surface = pygame.Surface((195,40))
            temp_surface.fill((grey))
            #temp_surface.blit(text, (0, 0))
            screen.blit(temp_surface, (1060,10))
            
            
            
            screen.blit(myfont_1.render('Remaining time: '+str(100-int(round((time.time()- start_time),0))), False, white),(1070,20)) #contartempo
            
            
            if int(round((time.time()- start_time),0))>max_time: game_over()
            
            
            pygame.display.flip()

            
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

                       
                        game_state['energy']-=2  #testing
                     


                        play_room(next_room)
                        b=False
        
       
    else:
        
        screen.blit(myfont.render('Press ENTER to continue', False, white),(50,300))
        pygame.display.flip()
        
        b=True
        while b:
            
            temp_surface = pygame.Surface((195,40))
            temp_surface.fill((grey))
            #temp_surface.blit(text, (0, 0))
            screen.blit(temp_surface, (1060,10))
            
            
            
            screen.blit(myfont_1.render('Remaining time: '+str(100-int(round((time.time()- start_time),0))), False, white),(1070,20)) #contartempo
            
            
            if int(round((time.time()- start_time),0))>max_time: game_over()
            
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                
                elif event.type==pygame.KEYDOWN:    
                    if event.key == pygame.K_RETURN: 
                        play_room(current_room)
                        b=False
              
        








# nome=''

# while nome=='':

#     nome=input('What is your name').strip()




game_state = INIT_GAME_STATE.copy()

start_game()
