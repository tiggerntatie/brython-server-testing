from ggame import App, ImageAsset, Sprite

# Create a displayed object using an image asset
Sprite(ImageAsset("ggame/bunny.png"), (100,100))
# Create the app, with a 500x500 pixel stage
app = App(500,500)  
# Run the app
app.run()
