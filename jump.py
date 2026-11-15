import pygame, math

pygame.init()

#global
screen_x = 500
screen_y = 500 
level = 1
tile_size = 50
end_x = 0
end_y = 0
gravity = 0.7

#player
player_x = 250
player_y = 250
player_speed = 1
player_radius = 3
player_weight = 1

player_y_velocity

mouseX = 0
mouseY = 0

#colors
black = (0,0,0)
white = (255,255,255)
 
#start
screen = pygame.display.set_mode((screen_x, screen_y))
running = True

#functions
def draw_level():
    global level, player_x, player_y, end_x, end_y,

    #little level desginer because its quicker this way
    # 0 = open space
    # 1 = closed space
    # 2 = start (player beginning)
    # 3 = end
    # 4 = nut 1
    # 5 = nut 2
    # 6 = nut 3


    grid_layout = {
        #1,2,3,4,5,6,7,8,9,10
       1:[ 
        [1,1,1,1,1,1,1,1,1,1], #1
        [1,1,1,1,1,1,1,1,1,1], #2
        [1,1,1,1,1,1,1,1,1,1], #3
        [1,1,1,1,1,1,1,1,1,1], #4
        [1,2,0,0,0,0,0,0,3,1], #5
        [1,1,1,1,1,1,1,1,1,1], #6
        [1,1,1,1,1,1,1,1,1,1], #7
        [1,1,1,1,1,1,1,1,1,1], #8
        [1,1,1,1,1,1,1,1,1,1], #9
        [1,1,1,1,1,1,1,1,1,1], #10
       ],
        2:[ 
        [1,1,1,1,1,1,1,1,1,1], #1
        [1,1,1,1,1,1,1,1,1,1], #2
        [1,1,1,1,1,1,1,1,1,1], #3
        [1,1,1,1,1,1,1,1,1,1], #4
        [1,2,0,0,0,0,0,0,3,1], #5
        [1,1,1,1,1,1,1,1,1,1], #6
        [1,1,1,1,1,1,1,1,1,1], #7
        [1,1,1,1,1,1,1,1,1,1], #8
        [1,1,1,1,1,1,1,1,1,1], #9
        [1,1,1,1,1,1,1,1,1,1], #10
        ],
    }

    grid = grid_layout.get(level)
    
    open_tile = pygame.Surface((tile_size,tile_size))
    open_tile.fill(white)

    closed_tile = pygame.Surface((tile_size,tile_size))
    closed_tile.fill(black)

    for row_stuff, row in enumerate(grid):
            for collumn_stuff, tile in enumerate(row):
                x = collumn_stuff * tile_size
                y = row_stuff * tile_size
                if tile == 1:
                    screen.blit(closed_tile, (x,y))
                else:
                    screen.blit(open_tile, (x,y))
                    if tile == 2:
                        player_x = x + tile_size/2
                        player_y = y + tile_size/2
                    elif tile == 3:
                        end_x = x
                        end_y = y

def draw_player():
    global player_y_velocity

    player_y_vel += gravity
    player_rect.y += player_y_vel

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN: 
            (mouseX, mouseY) = pygame.mouse.get_pos()
        print(mouseX, mouseY)

    draw_level()
    pygame.draw.circle(screen,black,(player_x,player_y),player_radius)
    pygame.display.flip()
pygame.quit()



