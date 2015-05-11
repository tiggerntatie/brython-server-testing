from browser import window, document
from random import randint
from javascript import JSObject, JSConstructor


PIXI = JSObject(window.PIXI)
Stage = JSConstructor(window.PIXI.Stage)
Sprite = JSConstructor(window.PIXI.Sprite)
GRAPHICS = JSConstructor(window.PIXI.Graphics)

interactive = True
stage = Stage(0xF0F0F0, interactive)
renderer = PIXI.autoDetectRenderer(1000, 650)
#print(dir(document.body.append))
document.body.appendChild(renderer.view)

def animate(arg1):
  window.requestAnimFrame(animate)
  for s in sprites:
    s.poll()
  renderer.render(stage)

window.requestAnimFrame(animate)

class BunnySprite(object):
    def __init__(self, stage, x, y):
        self.sprite = Sprite(PIXI.Texture.fromImage("bunny.png"))
        self.sprite.interactive = True
        self.sprite.anchor.x = 0.5
        self.sprite.anchor.y = 0.5
        self.sprite.position.x = x
        self.sprite.position.y = y
        self.sprite.click = self.click
        self.speed = (3,0)
        stage.addChild(self.sprite)
        
    def click(self, interactionData):
        print("click")
        
    def mouseover(self, interactionData):
        print(dir(interactionData))
    
    def poll(self):
        self.speed[1] += 1
        self.sprite.position.x += self.speed[0]
        self.sprite.position.y += self.speed[1]
        self.speed[1] *= 0.9999
        if self.sprite.x > 950 or self.sprite.x < 50:
            self.speed[0] *= -1
            self.sprite.x += self.speed[0]
        if self.sprite.y > 600:
            self.speed[1] *= -1
            self.sprite.y += self.speed[1]

class CircleSprite(BunnySprite):
    def __init__(self, stage, x, y):
        Graphics = GRAPHICS()
        Graphics.lineStyle(5, randint(0,255)*0x10000+randint(0,255)*0x100+randint(0,255), 1)
        circle = Graphics.drawCircle(0,0,25)
        self.sprite = Sprite(circle.generateTexture())
        self.sprite.interactive = True
        self.sprite.anchor.x = 0.5
        self.sprite.anchor.y = 0.5
        self.sprite.position.x = x
        self.sprite.position.y = y
        self.sprite.click = self.click
        self.sprite.mouseover = self.mouseover
        self.speed = (3,0)
        stage.addChild(self.sprite)

def keyCode(ev):
    print(ev.keyCode)
    

# document['body'].bind('keydown', keyCode)


def onload(window):
    canvas = window.document.createElement('canvas')
    canvas.setAttribute('width','800')
    canvas.setAttribute('height','500')
    canvas.setAttribute('style','border:1px solid #000000;')
    window.document.body.appendChild(canvas)
    

w = window.open("", "")
w.onload = onload(w)

# make a bunch of bunnies
staticsprites = [sprites.CircleSprite(stage, randint(50,950),randint(50,600)) for x in range(200)]
sprites = [sprites.CircleSprite(stage, 50+(x*15)%100,(20+x*2)%30) for x in range(5)]


print("Testing Graphics")

