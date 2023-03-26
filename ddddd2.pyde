def setup():
    size(600,600)
def draw():

    if mousePressed and (mouseButton == LEFT):
        img = loadImage("hhhh.jpg")
        image(img,0,0,600,600)
    elif mousePressed and (mouseButton == RIGHT):
        img = loadImage("llll.jpg")
        image(img,0,0,600,600)
