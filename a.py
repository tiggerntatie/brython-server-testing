from ggame import *

class bunnySprite(Sprite):

    def __init__(self, *assets, pos = (0,0)):
        super().__init__(*assets, pos=pos)
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
        self.xcenter = 0.5
        self.ycenter = 0.5
        self.count = 0
        #self.scale = 0.5
        #self.circularCollisionModel()

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
    
    def checkCollide(self):
        if self.collidingWithSprites(bunnySprite):
            self.app.springsound.play()
        
    def leftKey(self, event):
        self.vx = -1
        event.consumed = True
        self.checkCollide()

    def rightKey(self, event):
        self.vx = 1
        event.consumed = True
        self.checkCollide()
        
    def upKey(self, event):
        self.vy = -1
        event.consumed = True
        self.checkCollide()
    
    def downKey(self, event):
        self.vy = 1
        event.consumed = True
        self.checkCollide()
        
    def horizUp(self, event):
        self.vx = 0
        event.consumed = True
        
    def vertUp(self, event):
        self.vy = 0
        event.consumed = True
    
    def spaceKey(self, event):
        pass
    
    def step(self):
        self.count += 1
        self.x += self.vx*2
        self.y += self.vy*2
        if self.count % 10 == 0:
            pass
            self.nextImage(True)
        
class myApp(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        grassurl = "ggame/grass_texture239.jpg"
        grass = ImageAsset(grassurl)
        Sprite(grass, (0,0))
        
        self.bunnies = []
        bunnyurl = "ggame/bunny.png"
        bunny = ImageAsset(bunnyurl)
        
        bunniesurl = "ggame/bunnysheet5.png"
        bunniesframe = Frame(178,217,30,29)
        # this gives us a series of frames from a sprite sheet
        # the frame (above) defines the size and location of the first
        # image. The ImageAsset call (below) says how many frames there
        # will be, in what direction from the first, and how many pixels
        # separate each frame
        bunnies = ImageAsset(bunniesurl, bunniesframe, 4, 'horizontal', 2)

        fcolor = Color(0x5050ff, 0.8)
        lcolor = Color(0, 1)
        linesty = LineStyle(3, lcolor)
        rect = RectangleAsset(100, 150, linesty, fcolor)
        circ = CircleAsset(50, linesty, fcolor)
        poly = PolygonAsset([(0,0), (50,50), (50,100), (0,0)], linesty, fcolor)
        line = LineAsset(-50, 75, linesty)
        ell = EllipseAsset(50, 75, linesty, fcolor)
        text = TextAsset("what up? big long text string!")
        
        
        for x in range(50,500,150):
            for y in range(50,500,150):
                #self.bunnies.append(bunnySprite(text, pos=(x,y)))
                self.bunnies.append(bunnySprite(bunnies, pos=(x,y)))
        self.spring = SoundAsset("ggame/spring.wav")
        self.springsound =Sound(self.spring)
        #self.springsound.loop()


    def step(self):
        for s in self.bunnies:
            s.step()

        #for s in self.bunnies:
        #    s.x += self.direction
        #self.direction *= -1

app = myApp(500, 400)

app.run()
