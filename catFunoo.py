import runWorld as rw
import drawWorld as dw
import pygame as pg

from random import randint

gameState = 0
counter = 0

name = "The Kevin Sullivan Game!"
width = 600
height = 600
rw.newDisplay(width, height, name)

myImage = dw.loadImage("sullivan_kevin.bmp")

class State:
	def __init__(self, img, xpos, xvel, ypos, yvel):
		self.img = img
		self.xpos = xpos
		self.xvel = xvel
		self.ypos = ypos
		self.yvel = yvel
        
ourState = State(myImage, 100, 1, 100, 1)

def updateDisplay(state):
	dw.fill((100, 0, 70))
	dw.draw(state.img, (state.xpos, state.ypos))
	dw.draw(dw.makeLabel("Click to Survive! Score: " + str(counter), "Vendera", 25, dw.red), (12, 12))

def updateState(state):
	state.xpos = state.xpos+state.xvel
	state.xvel = state.xvel
	state.ypos = state.ypos+state.yvel
	state.yvel = state.yvel
	return(state)

def handleEvent(state, event):  
	if (event.type == pg.MOUSEBUTTONDOWN):
		if (gameState == 0):
			global counter
			counter += 1
		if (state.xvel) > 0 and (state.yvel) > 0:
			state.xvel = ((state.xvel*(-1))-1)
			state.yvel = (state.yvel)
			return state
		elif (state.xvel) < 0 and (state.yvel) > 0:
			state.xvel = (state.xvel)
			state.yvel = ((-1*state.yvel)-1)
			return state
		elif (state.xvel) < 0 and (state.yvel) < 0:
			state.xvel = (-1*state.xvel+1)
			state.yvel = (state.yvel)
			return state
		else:
			state.xvel = (state.xvel)
			state.yvel = (-1*state.yvel+1)
		return(state)
	else:
		return(state)

def endState(state):
	if (state.xpos > 423 or state.xpos < 0 or state.ypos > 362 or state.ypos < 0):
		return True
	else:
		return False

frameRate = 60

rw.runWorld(ourState, updateDisplay, updateState, handleEvent, endState, frameRate)
