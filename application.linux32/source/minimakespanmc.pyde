from app import *
from Button import Button
from Mode import Mode

#3:10:10:1:10

mode = Mode("Main")

def setup() :
    size(400,600)
    Button(50,250,300,50, "From File", fromFiler)
    Button(50,325,300,50, "From Keyboard", lambda : mode.switch("fromKeyboard"))
    Button(50,400,300,50, "Random Generation", lambda : mode.switch("randomGen"))

def draw() :
    background(255)
    
    render()
    
    
def render() :
    mode.render()
    if(mode.getType()=="Main") :
        for b in Button.buttons :
            b.render()
            
def fromFiler() :
    if(mode.getType() == "Main") :
        selectInput("select a file to process","fileSelected")
    mode.switch("fromFile")

def fileSelected(selection) :
  if selection == None :
    print("Window was closed or the user hit cancel.")
  else :
    print("You selected " + selection.toString())
    reader = createReader(selection.toString())
    mode.fromKeyboard = reader.readLine()
    
    
    
def mousePressed() :
  if(mode.getType()=="Main") :
    for b in Button.buttons :
      if(mouseX>b.x and mouseY>b.y and mouseX<b.x+b.l and mouseY<b.y+b.h) :
        b.cb()
      
      
def keyPressed() :
    if(key == BACKSPACE) :
        mode.fromKeyboard = mode.fromKeyboard[:-1]
    else :
        if(mode.fromKeyboard != None and key == str(key)) :
            mode.fromKeyboard = mode.fromKeyboard+key
        if (key==RETURN or key==ENTER) :
            mode.call()