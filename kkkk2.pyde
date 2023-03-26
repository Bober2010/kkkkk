z =1
x =1
c =1
def setup():
    size(1000,1000)
    background(100)
def draw():
    global z,x,c

    ellipse(z,x,c,z)
    push()
    background(255,255,255)
    img = loadImage("hhhh.jpg")
    image(img,mouseX ,mouseY, 300, 200 )
    print("%d : %d" % (mouseX, pmouseY))
    pop()
    push()
    strokeWeight(10)
    point(random(0,1000),random(0,1000))
    pop()
     
    z +=1
    x -=1
    c +=1
