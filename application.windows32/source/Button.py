class Button :
  buttons = set()
  
  def __init__(self, x, y, l, h, title, callback, c=color(0,128,128), txtsize=28) :
    self.c = c
    self.txs = txtsize
    self.x = x
    self.y = y
    self.h = h
    self.l = l
    self.title = title
    self.memorycb = callback
    self.cb = callback
    Button.buttons.add(self)
    
  def render(self) :
      stroke(0)
      fill(self.c)
      rect(self.x, self.y, self.l, self.h)
      textSize(self.txs)
      fill(0)
      text(self.title, self.x+5,self.y+10, 350,200)