import pygame

pygame.init()
clock = pygame.time.Clock()

# colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

block_size = 10
move_size = 10

# game parameters
dis_width = 800
dis_height = 400

dis = pygame.display.set_mode((dis_width,dis_height))

# instantiate variables
game_over = False
dis.fill(white)

x1_change = 0
y1_change = 0

# starting spot
x1 = dis_width/2
y1 = dis_height/2

while not game_over:
    for event in pygame.event.get():
        
        print(event)

        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -move_size
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = move_size
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -move_size
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = move_size
                x1_change = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x1_change = 0
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 0
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = 0
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 0
                x1_change = 0
        
    x1 += x1_change
    y1 += y1_change

    # reset display
    dis.fill(white)
    
    # block
    pygame.draw.rect(dis, black, [x1, y1, block_size, block_size])

    # falling objects
    pygame.draw.rect(dis, red, [x1, y1, block_size, block_size])
        
    
    pygame.display.update()
    clock.tick(10)
