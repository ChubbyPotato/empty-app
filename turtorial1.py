from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x0ff000, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(10, black)
# A graphics asset that represents a rectangle
rectangle = RectangleAsset(100, 200, thinline, red)
circle= CircleAsset(90, thinline, green)


# Now display a rectangle
Sprite(rectangle, (200,60))
Sprite(circle, (200,50))



myapp = App()
myapp.run()