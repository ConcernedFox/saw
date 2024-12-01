import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600

Satalite = []
Lines =[]
Next_Satalite = 0

Start_Time = 0
Total_Time = 0
End_Time = 0

Number_Of_Satalites = 8

def create_Satalites():
    global Start_Time
    for count in range (0,Number_Of_Satalites):
        Space_Craft = Actor("Satalite.png")
        Space_Craft.pos = randint(40,WIDTH - 40), randint(40,HEIGHT - 40)
        Satalite.append(Space_Craft)
    Start_Time = time()

def draw():
    global Total_Time
    screen.blit("Space.png",(0,0))
    Number = 1
    for Space_Craft in Satalite:
        Screen.draw.text(str(Number),(Space_Craft.pos[0],Space_Craft.pos[1]+20))
        Number = Number+1
    for Line in Lines:
        screen.draw.line(Line[0],Line[1]"white")
        if Next_Satalite<Number_Of_Satalites:
            Total_Time = time - Start_Time
            screen.draw.text(str(round(Total_Time,1)),(10,10), fontsize=30)
        else:
            screen.draw.text(str(round(Total_Time,1)),(10,10), fontsize=30)