from Button import Button
from app import *

class Mode :
    
    def __init__(self, fromSomething) :
        self.switch(fromSomething)
        
    def getType(self) :
        return self.type
    
    def switch (self, fromSomething) :
        
        self.type = fromSomething
        if (self.type == "Main") :
            self.txt = "this programm computes results for the min-makespan problem, running different algorithms against each other. please select a method of input"
            self.fromKeyboard = None
        
        if(self.type == "fromFile") :
            self.txt = "the content of your file will apppear below when loaded, press enter then, to compute"
            self.fromKeyboard = ""
        if (self.type == "fromKeyboard") :
            self.txt ="please enter your instance with format  ''m:n:d1:d2:d3:...''"
            self.fromKeyboard = ""
        if (self.type == "randomGen") :
            self.txt ="you may enter your random generation specification in format ''m:n:k:min:max:output''"
            self.fromKeyboard = ""
            
    def call(self) :
        if (self.type == "fromKeyboard" or self.type == "fromFile") :
            self.txt = fromString(self.fromKeyboard)
            
        if (self.type == "randomGen") :
            tmp = self.fromKeyboard.split(":")
            m = int(tmp[0])
            n = int(tmp[1])
            k = int(tmp[2])
            mini = int(tmp[3])
            maxi = int(tmp[4])
            o = tmp[5].split("\n")[0]
            fromGeneration(m,n,k,mini,maxi,o)
            self.txt = "your generation is complete, check the project folder to find the results"
            
        if (self.type=="results") :
            self.switch("Main")
        
        if(self.type != "Main") :    
            self.fromKeyboard = ""
            self.switch("results")
    
    def render(self) :
        stroke(0)
        fill(255)
        rect(25,25,350,200)
        textSize(20)
        fill(0)
        text(self.txt, 30, 35, 350,200)
        if (self.type == "fromKeyboard" or self.type == "fromFile") :
            textSize(30)
            text(self.fromKeyboard, 30, 250, 350,200)
        if (self.type == "randomGen") :
            textSize(30)
            text(self.fromKeyboard, 30, 250, 350,200)