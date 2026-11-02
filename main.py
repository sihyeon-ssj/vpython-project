Web VPython 3.2
stickman_body = cylinder(pos=vec(0, 0, 0), axis=vec(0, 2, 0), radius=0.1, color=color.white)
stickman_top = sphere(pos=vec(0, 2, 0), axis=vec(0, 5, 0), radius=0.3, color=color.white)

stickman_legL = cylinder(pos=vec(-0.2, 0.5, 0), axis=vec(0, -2, 0), radius=0.1, color=vec(0.6,0.6,0.6))
stickman_legR = cylinder(pos=vec(0.2, 0.5, 0), axis=vec(0, -2, 0), radius=0.1, color=vec(0.6,0.6,0.6))

stickman_armL = cylinder(pos=vec(-0.2, 3, 0), axis=vec(0, -2, 0), radius=0.1, color=vec(0.6,0.6,0.6))
stickman_armR= cylinder(pos=vec(0.2, 3, 0), axis=vec(0, -2, 0), radius=0.1, color=vec(0.6,0.6,0.6))

stickman = compound([stickman_body, stickman_top, stickman_legL, stickman_legR, stickman_armL, stickman_armR])

while True :
    rate(10000000)
    k = keysdown()
    if 'left' in k :
        rocket.pos.x = rocket.pos.x - 0.1
    if 'right' in k :
        rocket.pos.x = rocket.pos.x + 0.1
