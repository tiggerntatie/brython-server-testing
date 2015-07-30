from ggame import *

class bunnySprite(Sprite):

    def __init__(self, asset, position = (0,0), frame = False):
        super().__init__(asset, position, frame)
        self.app.listenKeyEvent(KeyEvent.keydown, "space", self.spaceKey)
        self.app.listenKeyEvent(KeyEvent.keydown, "left arrow", self.leftKey)
        self.app.listenKeyEvent(KeyEvent.keydown, "right arrow", self.rightKey)
        self.app.listenKeyEvent(KeyEvent.keydown, "up arrow", self.upKey)
        self.app.listenKeyEvent(KeyEvent.keydown, "down arrow", self.downKey)
        self.app.listenKeyEvent(KeyEvent.keyup, "left arrow", self.horizUp)
        self.app.listenKeyEvent(KeyEvent.keyup, "right arrow", self.horizUp)
        self.app.listenKeyEvent(KeyEvent.keyup, "up arrow", self.vertUp)
        self.app.listenKeyEvent(KeyEvent.keyup, "down arrow", self.vertUp)
        self.app.listenMouseEvent(MouseEvent.mousewheel, self.mouse)
        self.app.listenMouseEvent(MouseEvent.click, self.mouseclick)
        self.app.listenMouseEvent(MouseEvent.dblclick, self.doubleclick)
        self.app.listenMouseEvent(MouseEvent.mousemove, self.mousemove)
        self.vx = 0
        self.vy = 0
        
    def mouse(self, event):
        if event.wheelDelta > 0:
            self.spring1.play()
        elif event.wheelDelta < 0:
            self.spring2.play()
        event.consumed = True
        
    def mouseclick(self, event):
        event.consumed = True
        
    def doubleclick(self, event):
        event.consumed = True
        
    def mousemove(self, event):
        event.consumed = True
    
    def leftKey(self, event):
        self.vx = -1
        event.consumed = True

    def rightKey(self, event):
        self.vx = 1
        event.consumed = True
        
    def upKey(self, event):
        self.vy = -1
        event.consumed = True
    
    def downKey(self, event):
        self.vy = 1
        event.consumed = True
        
    def horizUp(self, event):
        self.vx = 0
        event.consumed = True
        
    def vertUp(self, event):
        self.vy = 0
        event.consumed = True
    
    def spaceKey(self, event):
        pass
    
    def step(self):
        self.x += self.vx*2
        self.y += self.vy*2

class myApp(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        grassurl = "ggame/grass_texture239.jpg"
        grass = ImageAsset(self, grassurl)
        Sprite(grass, (0,0))
        
        self.bunnies = []
        bunnyurl = "ggame/bunny.png"
        bunny = ImageAsset(self, bunnyurl)
        
        fcolor = Color(0x5050ff, 0.8)
        lcolor = Color(0, 1)
        line = LineStyle(3, lcolor)
        #rect = RectangleAsset(self, 100, 150, line, fcolor)
        #circ = CircleAsset(self, 50, line, fcolor)
        #ell = EllipseAsset(self, 50, 75, line, fcolor)
        #poly = PolygonAsset(self, [(0,0), (50,50), (50,100), (0,0)], line, fcolor)
        #line = LineAsset(self, -50, 75, line)
        text = TextAsset(self, "what up? big long text string!")
        
        
        for x in range(50,500,150):
            for y in range(50,500,150):
                self.bunnies.append(bunnySprite(text, (x,y)))
        self.direction = 5
        self.spring = SoundAsset(self, "ggame/spring.wav")
        self.springsound =Sound(self.spring)
        self.springsound.loop()
        

    def step(self):
        for s in self.bunnies:
            s.step()

        #for s in self.bunnies:
        #    s.x += self.direction
        #self.direction *= -1

app = myApp(500, 400)


app.run()
