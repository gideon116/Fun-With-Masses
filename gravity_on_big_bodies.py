from vpython import *


# set scene width
scene.width = 1650
scene.height = 500
scene.range = 500

# parameters for bigger mass
xgiant = -(scene.width-50)
ygiant = 0
mgiant = 2e15

rgiant = 50
nucleus = sphere(pos=vec(xgiant, ygiant, 0),
                 radius=rgiant, color=color.blue,
                 make_trail=False, trail_type='points',
                 interval=10, retain=1)

# parameters for smaller mass
x = (scene.width-50)
y = 0
m = 1e15

r = 30
alpha = sphere(pos=vec(x, y, 0), radius=r,
               color=color.red, make_trail=False,
               trail_type='points', interval=10, retain=1)

G = 6.7e-11  # Newton gravitational constant

running = False


# slider to adjust separation distance in calculations
def setb(s):
    global dist, wt
    dist = s.value
    wt.text = '{:1.0f}'.format(sl.value)+'00 kilometers'


sl = slider(min=0, max=1000, value=16, step=1, length=1000, bind=setb)
wt = wtext(text='{:1.0f}'.format(sl.value)+'00 kilometers')


# run button
def Run(b):
    global running
    if running:
        running = False
        b.text = 'Run'
    else:
        running = True
        b.text = 'Pause'


b = button(text="Run", bind=Run)
scene.append_to_caption('\n\n')

t = 0  # initial time
dt = 1  # change in time
tt = t + dt

massgiant = wtext(text="The mass of the bigger body = "+str(mgiant)+" kg"+'\n')  # display mass
mass = wtext(text="The mass of the smaller body is = "+str(m)+" kg"+'\n')  # display mass

while True:
    rate(1000)

    if running:

        # get the separation distance the user input
        clac_x = (sl.value / 2) * 100
        clac_xgiant = -(sl.value / 2) * 100

        # update the position of masses
        alpha.pos = vec(x, y, 0)
        nucleus.pos = vec(xgiant, ygiant, 0)

        # update time
        t = t + dt
        tt = t + dt

        # define parameters for t + dt
        future_x = x - (G * mgiant * tt/((clac_x + abs(clac_xgiant))**2))
        future_xgiant = xgiant + (G * m * tt/((clac_x + abs(clac_xgiant))**2))

        # update position
        if future_x > future_xgiant:
            x = x - (G * mgiant * t/((clac_x + abs(clac_xgiant))**2))
            xgiant = xgiant + (G * m * t/((clac_x + abs(clac_xgiant))**2))

        else: 
            running = False
            time = wtext(text="Time of collision = "+str(t)+" seconds")
