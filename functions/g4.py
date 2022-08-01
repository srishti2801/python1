import pgzrun

HEIGHT = 500
WIDTH = 500

p = Rect((40,40),(50,50))

def draw():
    screen.fill('white')
    screen.draw.filled_rect(p,'blue')

def update():
    control_player()
    if p.x > WIDTH:
        p.x = 0
    if p.x < 0:
        p.x = WIDTH
    if p.y > HEIGHT:
        p.y = 0
    if p.y < 0:
        p.y = HEIGHT

def control_player():
     if keyboard.RIGHT:
        p.x +=2
     if keyboard.LEFT:
        p.x += -2
     if keyboard.UP:
        p.y += -2
     if keyboard.DOWN:
        p.y += 2

pgzrun.go()