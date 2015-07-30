from ggame import App, ImageAsset, Sprite, MouseEvent
from random import randint
from math import abs

class Bunny(Sprite):
    
    def __init__(self, asset, position):
        super().__init__(self, asset, position)
        # register mouse events
        self.app.listenMouseEvent(MouseEvent.mousedown, self.mousedown)
        self.app.listenMouseEvent(MouseEvent.mouseup, self.mouseup)
        self.app.listenMouseEvent(MouseEvent.mousemove, self.mousemove)
        self.dragging = False

    
    def step(self):
        """
        Every now and then a bunny hops...
        """
        if randint(0,100) == 0:
            self.x += randint(-50,50)
            self.y += randint(-50,50)
        
    def mousedown(self, event):
        # capture any mouse down within 50 pixels
        self.deltax = self.x - event.x 
        self.deltay = self.y - event.y
        if abs(self.deltax) < 50 and abs(self.deltay) < 50:
            self.dragging = True
            event.consumed = True
            
    def mousemove(self, event):
        if self.dragging:
            self.x = event.x + self.deltax
            self.y = event.y + self.deltay
            event.consumed = True
            
    def mouseup(self, event):
        if self.dragging:
            self.dragging = False
            event.consumed = True
            
        
class DemoApp(App):
    
    def __init__(self):
        super().__init__(self, 500, 500)
        # Create an image asset for the app
        bunny = ImageAsset(self, "ggame/bunny.png")
        # Create several bunnies
        for i in range(10):
            Bunny(bunny, (randint(50,450),randint(50,450)))
        
    def step(self):
        """
        Override step to perform action on each frame update
        """
        for bunny in bunnies:
            bunny.step()



# Create the app, with a 500x500 pixel stage
app = DemoApp(500,500)  
# Run the app
app.run()
