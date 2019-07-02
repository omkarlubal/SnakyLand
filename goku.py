import pygame
import time
import random
pygame.init()

white = [255,255,255]
black = [0,0,0]
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
background = pygame.image.load("bg2.png")
lawn = pygame.image.load("lawn.png")
img = pygame.image.load('snakehead.png')
appleimg = pygame.image.load('apple.png')
specialimg = pygame.image.load('IMG-20170507-WA0000.png')

disp_width=800
disp_height=600

SetDisp = pygame.display.set_mode((disp_width,disp_height))
pygame.display.set_caption('Goku')

blocksize = 20
applesize = 30

clock= pygame.time.Clock()
FPS = 20

                
smallfont = pygame.font.SysFont("Algerian", 25)
medfont = pygame.font.SysFont("Algerian", 40)
largefont = pygame.font.SysFont("Algerian", 60)
direction = "up"
def about():
        about = True

        while about:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_c:
                                        about = False
                                if event.key == pygame.K_q:
                                        pygame.quit()
                                        quit()
                SetDisp.blit(specialimg,(0,0))
                Text_pop("Just keep eating apples and you will be fine xD",black,0,"small")
                Text_pop("Press C for main menu and Q to Quit",black,60,"small")
                pygame.display.update()
                clock.tick(15)
                

def StartScreen():
        intro = True

        while intro:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_c:
                                        intro = False
                                if event.key == pygame.K_q:
                                        pygame.quit()
                                        quit()
                                if event.key == pygame.K_a:
                                        about()

                SetDisp.blit(background,(0,0))
                Text_pop("Welcome to SnakeYland!!",green,-150,"large")
                Text_pop("Pro tip: don't run into yourselves",black,-50,"small")
                Text_pop("eat as much as you can!! xP",black,-20,"small")
                Text_pop("press c to play and q to quit",black,20,"medium")
                Text_pop("Press A for About ",black,100,"medium")
                
                
                pygame.display.update()
                clock.tick(15)


def Snake(snakelist,blocksize):                                                                # SNAKE FUNCTION
        if direction == "right":
                head = pygame.transform.rotate(img,270)
        if direction == "left":
                head = pygame.transform.rotate(img,90)
        if direction == "up":
                head = img
        if direction == "down":
                head = pygame.transform.rotate(img,180)

        SetDisp.blit(head,(snakelist[-1][0],snakelist[-1][1]))
        for XnY in snakelist[:-1]:
                pygame.draw.rect(SetDisp,green,[XnY[0],XnY[1],blocksize,blocksize])

def score(score):
        text = smallfont.render("Score: "+str(score), True, black)
        SetDisp.blit(text,(0,0))

def text_objects(text,color,size):                                                                           # TEXT FUNCTION
        if size == "small":
                TextSurface = smallfont.render(text, True, color)
        if size == "medium":
                TextSurface = medfont.render(text, True, color)
        if size == "large":
                TextSurface = largefont.render(text, True, color)
        return TextSurface, TextSurface.get_rect()

def Text_pop(msg,color,Y_DISPLACE=0,size="small"):                                                                        #TEXT_BLIT FUCNTION
        TextSurface, TextRect = text_objects(msg,color,size)
        TextRect.center = (disp_width/2),(disp_height/2)+Y_DISPLACE
        SetDisp.blit(TextSurface, TextRect)

def GameLoop():                                                                                  #GAMELOOP
    global direction
    exit_stat=False
    game_overstat = False

    lead_x = disp_width/2
    lead_y = disp_height/2
    
    lead_x_change=0
    lead_y_change=0
    snakelist=[]
    snakelength=1
    
    
    RandApple_x = random.randrange(0,disp_width-blocksize,10)
    RandApple_y = random.randrange(0,disp_height-blocksize,10)

    while not exit_stat:
        while game_overstat == True:
            Text_pop("Game over",red, -50,"large")
            Text_pop("PRESS C TO CONTINUE OR Q TO QUIT!!!",black, 50, "medium")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        game_overstat = False
                        exit_stat = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_overstat = False
                        exit_stat = True
                    if event.key == pygame.K_c:
                        GameLoop()
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  exit_stat = True
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                   direction = "left"
                   lead_x_change = -blocksize
                   lead_y_change = 0
               if event.key == pygame.K_RIGHT:
                   direction = "right"
                   lead_x_change = blocksize
                   lead_y_change = 0
               if event.key == pygame.K_UP:
                   direction = "up"    
                   lead_y_change = -blocksize
                   lead_x_change = 0
               if event.key == pygame.K_DOWN:
                   direction = "down"    
                   lead_y_change = blocksize
                   lead_x_change = 0
        lead_x += lead_x_change
        lead_y += lead_y_change

        
        if lead_x > RandApple_x and lead_x < RandApple_x + applesize or lead_x + blocksize > RandApple_x and lead_x + blocksize < RandApple_x + applesize:
                if lead_y > RandApple_y and lead_y < RandApple_y + applesize or lead_y + blocksize > RandApple_y and lead_y + blocksize < RandApple_y + applesize:  
                        RandApple_x = random.randrange(0,disp_width-applesize,10)
                        RandApple_y = random.randrange(0,disp_height-applesize,10)
                        snakelength += 1

                

        if lead_x > disp_width or lead_x < 0 or lead_y > disp_height or lead_y < 0:
            game_overstat = True
        
        if len(snakelist) >= snakelength:
                del snakelist[0]
        
        for eachSegment in snakelist[:-1]:
                if eachSegment == snakehead:
                        game_overstat = True
                
        SetDisp.blit(lawn,(0,0))
        score((snakelength-1)*100)
        SetDisp.blit(appleimg,(RandApple_x,RandApple_y))
        snakehead=[]
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        Snake(snakelist,blocksize)

        clock.tick(FPS)
        pygame.display.update()
        
 
    pygame.quit()
    quit()

StartScreen()
GameLoop()
