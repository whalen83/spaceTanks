from rect import *
from pygame import image
from background import Background
import numpy as np
from math import cos, sin


background = pygame.image.load('background.png')
#soundfx = pygame.mixer.Sound("soundfx.wav")
img0 = pygame.image.load('circleTank.png')
img0.set_colorkey((0,0,0))
img0.convert()
img = img0
img.convert()
img.set_colorkey((0,0,0))
rect0 = img0.get_rect()
rect0.center = width/2, height/2
rect = rect0.copy()
score = 0
rotation = 0
timer = pygame.time.get_ticks() 

BackGround = Background('background.png', [0,0])

v = np.array([3, 0])

speed = 1
dots = 1

projectileVel = [1,1]

points = random_points(dots)

particles =[]
projectiles = []
stars = []

pygame.init()
while running:
    pygame.key.set_repeat(100,100)
    seconds=100-(pygame.time.get_ticks()-timer)/1000 #calculate how many seconds
    if seconds<0: # if more than 10 seconds close the game
        break
    for event in pygame.event.get():
        if event.type == QUIT: 
            running = False
            if event.key == K_r:
                points = random_points(2000)
        keys = pygame.key.get_pressed()
    if len(points) == 0:
        dots +=1
        points = random_points(dots)
        speed += 1
        timer = pygame.time.get_ticks() 
    if keys[K_LEFT]:
        #pygame.key.set_repeat(10)
        rotation +=5
        img = pygame.transform.rotozoom(img0, rotation,1)
    if keys[K_RIGHT]:
        #pygame.key.set_repeat(10)   
        rotation -=5
        img = pygame.transform.rotozoom(img0, rotation,1)
    if keys[K_SPACE]:
        pygame.key.set_repeat(10)
        theta = -rotation *3.14159 / 180
        rot = np.array([[cos(theta), -sin(theta)], [sin(theta), cos(theta)]])
        v2 = np.dot(rot, v)
        tempProjectile = particle(15,[width/2,height/2],v2,7)
        projectiles.append(tempProjectile)
        img = pygame.transform.rotozoom(img0, rotation,1)

    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)
    
    
    for i in range(1,3):
        tempParticle = particle(float(randint(1,2)),[randint(0,width),randint(0,height)],[randint(1,2)*0.01,randint(1,2)*0.01],6)
        stars.append(tempParticle) #def __init__(self,circleRadius, position,velocity):

    for tempParticle in stars:        
        tempParticle.circleRadius += -.004
        tempParticle.position[0] = tempParticle.position[0] + tempParticle.velocity[0]
        tempParticle.position[1] = tempParticle.position[1] + tempParticle.velocity[1]
        if tempParticle.circleRadius <= 0:
            stars.remove(tempParticle)
        
        pygame.draw.circle(screen,tempParticle.color,tempParticle.position,tempParticle.circleRadius)  


    for projectile in projectiles:        
        projectile.circleRadius += -.01
        projectile.position[0] = projectile.position[0] + projectile.velocity[0]
        projectile.position[1] = projectile.position[1] + projectile.velocity[1]
        if projectile.circleRadius <= 0:
            projectiles.remove(projectile)
            
        pygame.draw.circle(screen,projectile.color,projectile.position,projectile.circleRadius)   
    screen.blit(img, (int(width / 2 - img.get_width() / 2), int(height / 2 - img.get_height() / 2)))    
    # display score
    draw_text("SCORE", [25,25])
    draw_text(str(score), [25,50])
    draw_text("TIMER", [100,25])
    draw_text(str(round(seconds)), [100,50])

    p_list = []
    for p in points:
        for projectile in projectiles:
            if abs(projectile.position[0] - p[0]) <= 10:
                if abs(projectile.position[1] - p[1]) <= 10:
                    if p not in p_list:
                        p_list.append(p)
                    score += 1
            
                    #pygame.mixer.Sound.play(soundfx)
            else:
                pygame.draw.circle(screen,PINK,p,4)
                
    for p in p_list:
        points.remove(p)
        
    pygame.display.flip()

pygame.quit()

