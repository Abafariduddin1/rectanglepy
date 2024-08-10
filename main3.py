import pgzrun
WIDTH=505
HEIGHT=605
TITLE="Main game"

def draw():
    w=150
    h=250
    for i in range(20):
        squ=Rect(200,200,w,h)
        squ.center=200,200
        screen.draw.rect(squ,"purple")
        w=w+10
        h=h-10



pgzrun.go()