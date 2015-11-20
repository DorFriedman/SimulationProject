import runWorld as rw
import drawWorld as dw
import pygame as pg

from random import randint

name = "The Kevin Sullivan Game!"
width = 600
height = 600
rw.newDisplay(width, height, name)

myimage = dw.loadImage("sullivan_kevin.bmp")

def updateDisplay(state):
    dw.fill((100, 0, 70))
    dw.draw(myimage, (state[0], state[2]))

def updateState(state):
    return((state[0]+state[1],state[1],state[2]+state[3],state[3]))

def endState(state):
    if (state[0] > 423 or state[0] < 0 or state[2] > 362 or state[2] < 0):
        return True
    else:
        return False

def handleEvent(state, event):  
    if (event.type == pg.MOUSEBUTTONDOWN):
        if (state[1]) > 0 and (state[3]) > 0:
            newState1 = ((state[1]*(-1))-1)
            newState2 = (state[3])
        elif (state[1]) < 0 and (state[3]) > 0:
            newState1 = (state[1])
            newState2 = ((-1*state[3])-1)
        elif (state[1]) < 0 and (state[3]) < 0:
            newState1 = (-1*state[1]+1)
            newState2 = (state[3])
        else:
            newState1 =(state[1])
            newState2 = (-1*state[3]+1)
        return((state[0],newState1,state[2],newState2))
    else:
        return(state)

initState = (100,1,100,1)

frameRate = 60

rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
