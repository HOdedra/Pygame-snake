import pygame 
import time
import random
""" 
Three steps:
1. event handling
2. logic
3. rendering
"""

#an event in pygame is a change in status it is not continuous

#initialise all the pygme modules
pygame.init()

#defining colours - uses RGB
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

display_width = 800
display_height = 600

#we need a surface like a canvas 
#this parameter has to be a tuple
gameDisplay = pygame.display.set_mode((display_width,display_height))
#title
pygame.display.set_caption('Slither')

#pygame.display.flip() is interchangable with the command below
#flip is like a flip book - this is motion 
#updating frames etc
#pygame.display.update()


#FPS
clock = pygame.time.Clock()

block_size = 20
FPS = 30

font = pygame.font.SysFont(None,25)

def snake(block_size, snakeList):
    for XnY in snakeList:     
        pygame.draw.rect(gameDisplay,green, [XnY[0],XnY[1],block_size,block_size])

def text_objects(text,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color):
    textSurf, textRect = text_objects(msg,color)
    textRect.center = (display_width/2),(display_height/2)
    gameDisplay.blit(textSurf, textRect)
    #screen_text = font.render(msg,True,color)
    #gameDisplay.blit(screen_text,[display_width/2,display_height/2])

def gameLoop():
    #game loop
    gameExit= False
    gameOver = False
    
    #leader of the groups of blocks
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0
    
    snakeList = []
    snakeLength = 1
    
    randAppleX = round(random.randrange(0,display_width-block_size))#/10.0)*10.0
    randAppleY = round(random.randrange(0,display_height-block_size))#/10.0)*10.0
    
    while not gameExit:
        
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit",red)
            pygame.display.update()
            
            for event in pygame.event.get():
                for event in pygame.event.get():
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change -= block_size 
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change += block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change -= block_size 
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change += block_size
                    lead_x_change = 0
            """if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    lead_x_change = 0 """
        
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
            
        
        lead_x += lead_x_change
        lead_y += lead_y_change
        
        
        gameDisplay.fill(white)
        AppleThickness = 30
        pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,AppleThickness,AppleThickness])
        snake(block_size, snakeList)
        
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]
        
        #to prevent us turning in on ourselves
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver == True
        
        snake(block_size, snakeList)
        
        #good way to also create a rectangle
        #gameDisplay.fill(red, rect=[200,200,50,50])
        
        pygame.display.update()

        """"
        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
                randAppleX = round(random.randrange(0,display_width-block_size))#/10.0)*10.0
                randAppleY = round(random.randrange(0,display_height-block_size))#/10.0)*10.0
                snakeLength += 1
        """
        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size  > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                randAppleX = round(random.randrange(0,display_width-block_size))#/10.0)*10.0
                randAppleY = round(random.randrange(0,display_height-block_size))#/10.0)*10.0
                snakeLength += 1
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX = round(random.randrange(0,display_width-block_size))#/10.0)*10.0
                randAppleY = round(random.randrange(0,display_height-block_size))#/10.0)*10.0
                snakeLength += 1
        
        
        #FPS
        clock.tick(FPS)
    
    pygame.quit()
    quit()

gameLoop()