from Tkinter import *
window = Tk()
window.title("Fish in a Tank")
import random


sameerLeft = PhotoImage(file="sameerLeft.gif")
sameerRight = PhotoImage(file="sameerRight.gif")
aayushLeft = PhotoImage(file="aayushLeft.gif")
aayushRight = PhotoImage(file="aayushRight.gif")

leftArray = [sameerLeft, aayushLeft]
rightArray = [sameerRight, aayushRight]
    
Background = PhotoImage(file="tank.gif")

windowWidth = 700
windowHeight= 525

canvas = Canvas(window, width = windowWidth, height = windowHeight)
canvas.grid(row = 0, column = 0, columnspan=3)
canvas.create_image(windowWidth/2,windowHeight/2, image = Background)

def updateFish(x,y,dx,dy,left,right):
    y += dy
    x += dx
    if dx < 0:
        canvas.coords(left, x, y)
        canvas.coords(right,-1000,-1000)
    else:
        canvas.coords(right,x,y)
        canvas.coords(left,-1000,-1000)
    if x >=700:
        dx=-dx
        x+=dx
    if x <=0:
        dx=-dx
        x+=dx
    if y >=525:
        dy=-dy
        y+=dy
    if y <=0:
        dy=-dy
        y+=dy   
    canvas.after(100, updateFish,x,y,dx,dy,left,right) #1/10 of a sec, 100ms

def createFish():
    if random.randrange(-2,2) >= 0:
        fishLeft = leftArray[0] 
        fishRight = rightArray[0]
    else:
       fishLeft = leftArray[1] 
       fishRight = rightArray[1]
    x = random.randrange(0,700)
    y = random.randrange(0,525)
    dx = random.randrange(-3,3)
    dy = random.randrange(-3,3)
    left = canvas.create_image(x,y,image = fishLeft)
    right = canvas.create_image(x,y,image = fishRight)
    updateFish(x,y,dx,dy,left,right)

        
AddNewFish = Button(window, text = "Add New Fish", command=createFish)
AddNewFish.grid(row=1, column=1, sticky ="EW")

window.mainloop()
