import pygame, math

pygame.init()
pygame.font.init()

#global
screen_x = 500
screen_y = 500 
level = 1
tile_size = 50
gravity = 600
clock = pygame.time.Clock()
dialouge_x = 0
dialouge_y = 0
timer_seconds = 0

#player
player_x = 250
player_y = 250
player_speed = 1
player_radius = 16
player_weight = 1
top_speed = 1200
player_y_velocity = 0

spawn_player_x = 0
spawn_player_y = 0

mouseX = 0
mouseY = 0

#end circle
end_x = 0
end_y = 0
end_radius = 20

#colors
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
 
#start
font = pygame.font.SysFont("couriernew", 20, bold = False, italic = False)
screen = pygame.display.set_mode((screen_x, screen_y))
history = []
running = True

#little level desginer because its quicker this way
# 0 = open space
# 1 = closed space
# 2 = start (player beginning)
# 3 = end
# 9 = text
# 4 = timer


grid_layout = {
    #1,2,3,4,5,6,7,8,9,10
   1:[ 
    [4,1,1,1,1,1,1,1,1,1], #1
    [1,1,1,1,1,1,1,1,1,1], #2
    [1,1,1,9,1,1,1,1,1,1], #3
    [1,1,1,1,1,1,1,1,1,1], #4
    [1,2,0,0,0,0,0,0,3,1], #5
    [1,1,1,1,1,1,1,1,1,1], #6
    [1,1,1,1,1,1,1,1,1,1], #7
    [1,1,1,1,1,1,1,1,1,1], #8
    [1,1,1,1,1,1,1,1,1,1], #9
    [1,1,1,1,1,1,1,1,1,1], #10
    ],
    #1,2,3,4,5,6,7,8,9,10
    2:[ 
    [4,1,1,1,1,1,1,1,1,1], #1
    [1,0,0,0,0,0,0,0,0,1], #2
    [1,0,0,0,0,0,0,0,0,1], #3
    [1,0,1,1,1,1,1,0,0,1], #4
    [1,0,1,1,1,1,1,0,2,1], #5
    [1,0,1,1,1,1,1,1,1,1], #6
    [1,0,1,1,1,1,1,1,1,1], #7
    [1,0,1,9,1,1,1,1,1,1], #8
    [1,3,1,1,1,1,1,1,1,1], #9
    [1,1,1,1,1,1,1,1,1,1], #10
    ],
    3:[ 
    [4,1,1,1,1,1,1,1,1,1], #1
    [1,1,1,9,1,1,1,1,1,1], #2
    [1,1,0,0,0,1,1,1,1,1], #3
    [1,1,0,0,0,0,1,1,1,1], #4
    [1,1,0,1,1,0,0,1,1,1], #5
    [1,1,0,1,1,1,0,0,1,1], #6
    [1,1,0,1,1,1,1,0,0,1], #7
    [1,1,0,1,1,1,1,1,0,1], #8
    [1,2,0,1,3,0,0,0,0,1], #9
    [1,1,1,1,1,1,1,1,1,1], #10
    ],
    4:[ 
    [4,1,1,1,1,1,1,1,1,1], #1
    [1,1,1,1,0,0,0,1,3,1], #2
    [1,1,1,0,0,1,0,1,0,1], #3
    [1,1,0,0,1,1,0,1,0,1], #4
    [1,0,0,1,0,0,0,1,0,1], #5
    [1,0,1,1,0,1,1,1,0,1], #6
    [1,0,0,1,0,0,0,0,0,1], #7
    [1,1,0,0,9,1,1,1,1,1], #8
    [1,1,1,0,2,1,1,1,1,1], #9
    [1,1,1,1,1,1,1,1,1,1], #10
    ],
    5:[ 
    [4,1,1,1,1,3,1,1,1,1], #1
    [1,1,1,1,1,0,1,1,2,1], #2
    [1,1,1,1,1,0,1,1,0,1], #3
    [1,1,1,0,0,0,1,1,0,1], #4
    [1,1,0,0,1,1,1,1,0,1], #5
    [1,1,1,0,0,1,1,1,0,1], #6
    [1,1,1,1,0,0,1,1,0,1], #7
    [1,1,1,1,1,0,0,1,0,1], #8
    [1,9,1,1,1,1,0,0,0,1], #9
    [1,1,1,1,1,1,1,1,1,1], #10
    ],
    6:[ 
    [1,1,1,1,1,1,1,1,1,1], #1
    [1,1,1,1,1,1,1,1,1,1], #2
    [1,1,1,1,1,1,1,1,1,1], #3
    [9,1,1,1,1,1,1,1,1,1], #4
    [1,1,1,1,1,1,1,1,1,1], #5
    [1,2,1,1,4,1,1,1,3,1], #6
    [1,1,1,1,1,1,1,1,1,1], #7
    [1,1,1,1,1,1,1,1,1,1], #8
    [1,1,1,1,1,1,1,1,1,1], #9
    [1,1,1,1,1,1,1,1,1,1], #10
    ],
}


dialouge = [
    "Heya! cant move?", #level 1
    "I guess that works too..", #level 2
    "Woah that was sick!", #and so on
    "Theres a ton of curves..", 
    "Last one!",
    "Not bad! Lets see if you can do better...",
]

#functions 
def draw_level():
    global level, player_x, player_y, end_x, end_y, spawn_player_x, spawn_player_y, dialouge_x, dialouge_y

    grid = grid_layout.get(level)

    
    open_tile = pygame.Surface((tile_size,tile_size))
    open_tile.fill(white)

    closed_tile = pygame.Surface((tile_size,tile_size))
    closed_tile.fill(black)

    for row_stuff, row in enumerate(grid):
            for collumn_stuff, tile in enumerate(row):
                x = collumn_stuff * tile_size
                y = row_stuff * tile_size
                if tile == 1 or tile == 9 or tile == 4:
                    screen.blit(wall, (x,y), (x, y, tile_size, tile_size))
                    if tile == 9:
                        dialouge_x = x
                        dialouge_y = y
                    if tile == 4:
                        timer_x = x
                        timer_y = y
                else:
                    screen.blit(open_tile, (x,y))
                    if tile == 2:
                        spawn_player_x = x + tile_size/2
                        spawn_player_y = y + tile_size/2
                    elif tile == 3:
                        end_x = x + tile_size/2
                        end_y = y + tile_size/2
                        pygame.draw.circle(screen,green,(x+ tile_size/2,y+ tile_size/2), end_radius)
    text_rendered = font.render(dialouge[level-1], True, white)
    screen.blit(text_rendered, (dialouge_x + tile_size/3,dialouge_y + tile_size/3))
    timer_rendered = font.render(str(round(timer_seconds, 2)), True, white)
    screen.blit(timer_rendered, (timer_x + tile_size/3,timer_y + tile_size/3))

def level_start():
    global player_x, player_y
    player_x = spawn_player_x
    player_y = spawn_player_y

def is_walls(x,y):
    player_to_grid_x = math.floor(x / tile_size)
    player_to_grid_y = math.floor(y / tile_size)

    if player_to_grid_x < 0 or player_to_grid_x > 9 or player_to_grid_y < 0 or player_to_grid_y > 9:
        return True
    else:
        num = grid_layout[level][player_to_grid_y][player_to_grid_x]
        if num == 0 or num == 2 or num == 3:#these are all open spaces
            return False
    return True

dragging = False
roll = 0
ball_vel = pygame.Vector2(0, 0)

sheet = pygame.image.load("Assets/hamstersheet.png") .convert_alpha()
wall = pygame.transform.scale(pygame.image.load("Assets/brick.png").convert_alpha(), (screen_x, screen_y)) 
frames = [
 sheet.subsurface((0, 0, 32, 32)),
    sheet.subsurface((32, 0, 32, 32)),  
    sheet.subsurface((32, 32, 32, 32)),  
    sheet.subsurface((0, 32, 32, 32)),
]
intro_frames = [
pygame.image.load("Assets/hedgehoghandup.png") .convert_alpha(),
pygame.image.load("Assets/hedgehoghanddown.png") .convert_alpha(),




]
w, h = intro_frames[0].get_size ()
s = min(350 / w, 300 / h)
intro_frames = [pygame.transform.smoothscale(f, (int(w * s), int(h * s))) for f in intro_frames]

title_font = pygame.font.SysFont("arial", 40, bold=True)
small_font = pygame.font.SysFont("arial", 22)
state = "intro"




draw_level()
level_start()

while running == True:
    dt = clock.tick(60) / 1000   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif state == "intro":
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                state = "play"
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            dragging =True
            drag_start = pygame.Vector2(event.pos)

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and dragging:
                dragging = False
                ball_vel = (drag_start - pygame.Vector2(event.pos)) * 5
                if ball_vel.length() > top_speed:
                    ball_vel.scale_to_length(top_speed)
    if dragging: 
        now = pygame.time.get_ticks() / 1000
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        history.append((now, mouse_pos))
        history = [(t, p) for (t, p) in history if now - t <= 0.1]
    if state == "intro":
        screen.fill(black)
        frame = intro_frames[(pygame.time.get_ticks() // 250) % len(intro_frames)]
        screen.blit(frame, frame.get_rect(center=(screen_x / 2, screen_y / 2)))

        title = title_font.render("Hurlin Hedgehogs", True, white)
        screen.blit(title, title.get_rect(center=(screen_x / 2, 50)))

        hint = small_font.render("press to start", True, white)
        screen.blit(hint, hint.get_rect(center=(screen_x / 2, screen_y - 40)))

        pygame.display.flip()
        continue
    ball_vel.y += gravity * dt
    new_x = player_x + ball_vel.x * dt
    if ball_vel.x > 0: 
         edge_x = new_x + player_radius
    else:
         edge_x =new_x - player_radius
    if is_walls(edge_x,player_y):
        ball_vel.x *= -0.8
    else:
        player_x = new_x
    new_y = player_y + ball_vel.y * dt
    if ball_vel.y > 0: 
         edge_y = new_y + player_radius
    else:
         edge_y =new_y - player_radius
    if is_walls(player_x, edge_y): 
        if ball_vel.y > 0:
            ball_vel.x *= 0.98 
        ball_vel.y *= -0.8
        if abs(ball_vel.y) < 30: 
            ball_vel.y = 0 
    else:
        player_y = new_y 
    roll += ball_vel.x * dt 
    frame_num = int(roll // 16) % 4 
   

    if level != 6:
        timer_seconds += clock.get_time() / 1000
    draw_level()
    if math.hypot(player_x-end_x,player_y-end_y) <= end_radius + player_radius:
        level += 1
        draw_level()
        level_start()
    screen.blit(frames[frame_num], (player_x - player_radius, player_y - player_radius))
    pygame.display.flip()

    

pygame.quit()



