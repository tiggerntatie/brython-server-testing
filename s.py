from ggame import App, ImageAsset, Sprite, MouseEvent
from random import random, randint

class Bunny(Sprite):
    
    asset = ImageAsset("ggame/bunny.png")
    
    def __init__(self, app, position):
        super().__init__(app, Bunny.asset, position)
        # register mouse events
        self.app.listenMouseEvent(MouseEvent.mousedown, self.mousedown)
        self.app.listenMouseEvent(MouseEvent.mouseup, self.mouseup)
        self.app.listenMouseEvent(MouseEvent.mousemove, self.mousemove)
        self.dragging = False

    
    def step(self):
        """
        Every now and then a bunny hops...
        """
        if random() < 0.001:
            self.x += randint(-50,50)
            self.y += randint(-50,50)
        
    def mousedown(self, event):
        # capture any mouse down within 50 pixels
        self.deltax = event.x - (self.x + self.width//2) 
        self.deltay = event.y - (self.y + self.height//2)
        if abs(self.deltax) < 50 and abs(self.deltay) < 50:
            self.dragging = True
            # only drag one bunny at a time - consume the event
            event.consumed = True
            
    def mousemove(self, event):
        if self.dragging:
            self.x = event.x - self.deltax - self.width//2
            self.y = event.y - self.deltay - self.height//2
            event.consumed = True
            
    def mouseup(self, event):
        if self.dragging:
            self.dragging = False
            event.consumed = True
            
        
class DemoApp(App):
    
    def __init__(self):
        super().__init__(500, 500)
        for i in range(10):
            Bunny(bunny, (randint(50,450),randint(50,450)))
        
    def step(self):
        """
        Override step to perform action on each frame update
        """
        for bunny in self.spritelist:
            bunny.step()



# Create the app
app = DemoApp()  
# Run the app
app.run()
