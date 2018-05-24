import pygame 

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


#we need a surface like a canvas 
#this parameter has to be a tuple
gameDisplay = pygame.display.set_mode((800,600))
#title
pygame.display.set_caption('Slither')

#pygame.display.flip() is interchangable with the command below
#flip is like a flip book - this is motion 
#updating frames etc
#pygame.display.update()

#game loop
gameExit= False

#leader of the groups of blocks
lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0
#FPS
clock = pygame.time.Clock()

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change -= 10 
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change += 10
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change -= 10 
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change += 10
                lead_x_change = 0
        """if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                lead_x_change = 0 """
    
    if lead_x >= 800 or lead_x < 0 or lead_y >= 600 or lead_y < 0:
        gameExit = True
        
    lead_x += lead_x_change
    lead_y += lead_y_change

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay,black, [lead_x,lead_y,20,20])
    
    #good way to also create a rectangle
    #gameDisplay.fill(red, rect=[200,200,50,50])
    
    pygame.display.update()
    
    #FPS
    clock.tick(15)

#this uninitializes pygame
pygame.quit()
quit()
