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
        
    
    def step(self):
        """
        Every now and then a bunny hops...
        """
        if randint(0,100) == 0:
            self.x += randint(-50,50)
            self.y += randint(-50,50)
        
    def mousedown(self, event):
        
        
        
class DemoApp(App):
    
    def __init__(self):
        super().__init__(self, 500, 500)
        
    def step(self):
        """
        Override step to perform action on each frame update
        """
        for bunny in bunnies:
            bunny.step()



# Create the app, with a 500x500 pixel stage
app = App(500,500)  
# Create an image asset for the app
grass = ImageAsset(app, "ggame/bunny.png")
# Create a displayed object using the asset
Sprite(grass, (100,100))
# Run the app
app.run()
