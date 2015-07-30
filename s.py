from ggame import App, ImageAsset, Sprite

# Create the app, with a 500x500 pixel stage
app = App(500,500)  
# Create an image asset for the app
grass = ImageAsset(app, "ggame/bunny.png")
# Create a displayed object using the asset
Sprite(grass, (100,100))
# Run the app
app.run()