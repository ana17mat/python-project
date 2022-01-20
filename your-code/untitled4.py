#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 01:24:03 2022

@author: anamatias
"""


# import pygame

# pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize

# pygame.init()



# #soundObj = pygame.mixer.Sound("/Users/anamatias/Desktop/IRONHACK/Project_week1/python-project/your-code/unlock.mp3")

# soundObj = pygame.mixer.Sound("unlock.mp3")
# soundObj.play()

# import pygame, sys, time
# from pygame.locals import*

# pygame.init()
# # DISPLAYSURF = pygame.display.set_mode((400, 300))
# # pygame.display.set_caption("Sound!!")

# soundObj = pygame.mixer.Sound('unlock.wav')
# soundObj.play()





import pygame
pygame.mixer.init()
pygame.mixer.music.load('unlock.mp3')
pygame.mixer.music.play()