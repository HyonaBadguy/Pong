import pygame
import random

pygame.init()

#initials
WIDTH, HIGH = 1000, 600
wn = pygame.display.set_mode((WIDTH, HIGH))
pygame.display.set_caption('Super Pong 64')
run = True

direction = [0,1]
angle = [0,1,2]

#colors 
WHITE = (255, 255, 255)

#bola
radius = 15
bola_x,bola_y = WIDTH/2 - radius, HIGH/2 - radius

bola_vel_x, bola_vel_y = .7, .7



#raquetas
paddle_width, paddle_height = 20,120
left_paddle_y = right_paddle_y = HIGH/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH - (100 + paddle_width/2)

right_paddle_vel= left_paddle_vel = 0

#gadgets
left_gadget =right_gadget = 0
left_gadget_remaining = right_gadget_remaining = 5


#main loop
while run:
    wn.fill((0,0,0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                right_paddle_vel = -.9
            if i.key == pygame.K_DOWN:
                right_paddle_vel = .9

            if i.key == pygame.K_RIGHT and right_gadget_remaining > 0:
                right_gadget = 1
        

            if i.key == pygame.K_w:
                left_paddle_vel = -.9
            if i.key == pygame.K_s:
                left_paddle_vel = .9

            if i.key == pygame.K_d and left_gadget_remaining > 0:
                left_gadget = 1

        if i.type == pygame.KEYUP:
            right_paddle_vel = 0
            left_paddle_vel = 0


    #movimientos de la bola
    if bola_y <= radius or bola_y >= HIGH - radius:
        bola_vel_y *= -1       
    if bola_x >= WIDTH - radius:
        bola_x, bola_y = WIDTH/2 - radius, HIGH/2 - radius
       
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                bola_vel_y,bola_vel_x = -1.4, 0.7
            if ang == 1:
                bola_vel_y,bola_vel_x = -0.7, 1.4
            if ang == 2:
                bola_vel_x,bola_vel_y = -0.7, 1.7    

        if dir == 1:
            if ang == 0:
                bola_vel_y,bola_vel_x = 1.4, 0.7
            if ang == 1:
                bola_vel_y,bola_vel_x = 0.7, 1.4
            if ang == 2:
                bola_vel_x,bola_vel_y = 0.7, 1.7    
        bola_vel_x *= -1
        
    if bola_x <= 0 + radius:
        bola_x, bola_y = WIDTH/2 - radius, HIGH/2 - radius
        bola_vel_x, bola_vel_y = 1, 1

        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                bola_vel_y,bola_vel_x = -1.4, 0.7
            if ang == 1:
                bola_vel_y,bola_vel_x = -0.7, 1.4
            if ang == 2:
                bola_vel_x,bola_vel_y = -0.7, 1.7    

        if dir == 1:
            if ang == 0:
                bola_vel_y,bola_vel_x = 1.4, 0.7
            if ang == 1:
                bola_vel_y,bola_vel_x = 0.7, 1.4
            if ang == 2:
                bola_vel_x,bola_vel_y = 0.7, 1.7

    #movimientos
    bola_x += bola_vel_x    
    bola_y += bola_vel_y

        #movimientos de las raquetas
    left_paddle_y += left_paddle_vel    
    right_paddle_y += right_paddle_vel
    if left_paddle_y >= HIGH - paddle_height:
        left_paddle_y = HIGH - paddle_height
    if left_paddle_y <= 0:
        left_paddle_y = 0

    if right_paddle_y >= HIGH - paddle_height:
        right_paddle_y = HIGH - paddle_height
    if right_paddle_y <= 0:
        right_paddle_y = 0   

    #colisiones de las raquetas
        #raqueta izq
    if bola_x - radius <= left_paddle_x + paddle_width and left_paddle_y <= bola_y <= left_paddle_y + paddle_height:
        bola_x = left_paddle_x + paddle_width + radius
        bola_vel_x *= -1

    #raqueta der
    if bola_x + radius >= right_paddle_x and right_paddle_y <= bola_y <= right_paddle_y + paddle_height:
        bola_x = right_paddle_x - radius
        bola_vel_x *= -1
        

    #gadgets in action
    if left_gadget == 1:
        if bola_x - radius <= left_paddle_x + paddle_width and left_paddle_y <= bola_y <= left_paddle_y + paddle_height:
            bola_x = left_paddle_x + paddle_width + radius
            bola_vel_x *= -3.5
            left_gadget = 0  
            left_gadget_remaining -= 1  

    if right_gadget== 1:        
        if bola_x + radius >= right_paddle_x and right_paddle_y <= bola_y <= right_paddle_y + paddle_height:
            bola_x = right_paddle_x - radius
            bola_vel_x *= -1
            left_gadget_remaining -= 3.5
            right_gadget = 0
        right_gadget_remaining -= 1


    #objetos
    pygame.draw.circle(wn,WHITE,(bola_x,bola_y),radius) 
    pygame.draw.rect(wn, WHITE, pygame.Rect(left_paddle_x, left_paddle_y,paddle_width, paddle_height))    
    pygame.draw.rect(wn, WHITE, pygame.Rect(right_paddle_x, right_paddle_y,paddle_width, paddle_height))    

    pygame.display.update()