"""
- Added a second snake controlled by another player, the first snake is controlled with w, a, s, d, and the second snake is controlled with the arrow keys.
- Added menu before game starts
- added customizable colors for both snakes while in the menu
"""

# imports 
import pygame
import time
import random
import pygame_menu 

pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# General/setup variables
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
# Displays the score with both p1's score and p2's score
def Your_score(p1_score, p2_score):
    score_title_txt = score_font.render("Score", True, yellow)
    score_txt = score_font.render(str(p1_score) + "|" + str(p2_score), True, yellow)

    dis.blit(score_title_txt, [(dis_width / 2) - (score_title_txt.get_width() / 2), 0])
    dis.blit(score_txt, [(dis_width / 2) - (score_txt.get_width() / 2), score_title_txt.get_height() - 10])
 
# Draws snake with correct color
def our_snake(snake_block, snake_list, snakeColor):
    for x in snake_list:
        pygame.draw.rect(dis, snakeColor, [x[0], x[1], snake_block, snake_block])
 
#  Displays a message at the center and specified height
def message(msg, color, height):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [(dis_width / 2) - (mesg.get_width() / 2), height])
 
# Game loop
def gameLoop():
    game_over = False
    game_close = False
 
    # Defines vars for snake 1
    snake1_x1 = (dis_width * 1) / 4 
    snake1_y1 = dis_height / 2
 
    snake1_x1_change = 0
    snake1_y1_change = 0
 
    snake_List = []
    Length_of_snake1 = 1

    # Defines vars for snake 2
    snake2_x1 = (dis_width * 3) / 4 
    snake2_y1 = dis_height / 2
 
    snake2_x1_change = 0
    snake2_y1_change = 0
 
    snake2_List = []
    Length_of_snake2 = 1

    # List used later contains info about winning 
    win_info = []

    # Sets food x and y
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    # Runs while the game is not over
    while not game_over:
        while game_close == True:
            # Game over, displays end message
            dis.fill(blue)
            message(win_info[0] + " Won!", red, dis_height / 3 + 30)
            message(win_info[1], red, dis_height / 3 + 60)
            message("Game Over! Press C-Play Again or Q-Quit", red, dis_height / 3)
            # Updates score
            Your_score(Length_of_snake1 - 1, Length_of_snake2 - 1)
            # Updates display
            pygame.display.update()
 
            # When key pressed
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # If key pressed is q sets vars to end loops and stop game
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    # If c is pressed
                    if event.key == pygame.K_c:
                        gameLoop()
        # When key pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # Movement controls for first snake
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if snake1_x1_change != snake_block:
                        snake1_x1_change = -snake_block
                        snake1_y1_change = 0
                elif event.key == pygame.K_d:
                    if snake1_x1_change != -snake_block:
                        snake1_x1_change = snake_block
                        snake1_y1_change = 0
                elif event.key == pygame.K_w:
                    if snake1_y1_change != snake_block:
                        snake1_y1_change = -snake_block
                        snake1_x1_change = 0
                elif event.key == pygame.K_s:
                    if snake1_y1_change != -snake_block:
                        snake1_y1_change = snake_block
                        snake1_x1_change = 0

                # Movement controls for second snake
                if event.key == pygame.K_LEFT:
                    if snake2_x1_change != snake_block:
                        snake2_x1_change = -snake_block
                        snake2_y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    if snake2_x1_change != -snake_block:
                        snake2_x1_change = snake_block
                        snake2_y1_change = 0
                elif event.key == pygame.K_UP:
                    if snake2_y1_change != snake_block:
                        snake2_y1_change = -snake_block
                        snake2_x1_change = 0
                elif event.key == pygame.K_DOWN:
                    if snake2_y1_change != -snake_block:
                        snake2_y1_change = snake_block
                        snake2_x1_change = 0

        # Checks if first snake is off screen
        if snake1_x1 >= dis_width or snake1_x1 < 0 or snake1_y1 >= dis_height or snake1_y1 < 0:    
            win_info = ["Player 2", "Player 1 hit the edge!"]
            game_close = True

        # Moves snake 1
        snake1_x1 += snake1_x1_change
        snake1_y1 += snake1_y1_change

        # Checks if second snake is off screen
        if snake2_x1 >= dis_width or snake2_x1 < 0 or snake2_y1 >= dis_height or snake2_y1 < 0:
            win_info = ["Player 1", "Player 2 hit the edge!"]
            game_close = True

        # Moves second snake
        snake2_x1 += snake2_x1_change
        snake2_y1 += snake2_y1_change

        # Fills the screen with blue pixels
        dis.fill(blue)

        # Draws the food
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # Updates snake 1 variables
        snake_Head = []
        snake_Head.append(snake1_x1)
        snake_Head.append(snake1_y1)
        snake_List.append(snake_Head)

        # Updates snake 2 variables
        snake2_Head = []
        snake2_Head.append(snake2_x1)
        snake2_Head.append(snake2_y1)
        snake2_List.append(snake2_Head)

        # Checks if the first snake hit the second one
        for i in range(len(snake2_List)):
            if snake_Head[0] == snake2_List[i][0] and snake_Head[1] == snake2_List[i][1]:
                if game_close == False:
                    win_info = ["Player 2", "Player 1 hit player 2!"]

                    # Checks if heads collided
                    if snake_Head[0] == snake2_Head[0] and snake_Head[1] == snake2_Head[1]: 
                        win_info = ["No Player", "Player 1's Head hit player 2's Head!"]

                game_close = True

        # Checks if the second snake hit the first one
        for i in range(len(snake_List)):
            if snake2_Head[0] == snake_List[i][0] and snake2_Head[1] == snake_List[i][1]:
                if game_close == False:
                    win_info = ["Player 1", "Player 2 hit player 1!"]

                    # Checks if heads collided
                    if snake_Head[0] == snake2_Head[0] and snake_Head[1] == snake2_Head[1]: 
                        win_info = ["No Player", "Player 1's Head hit player 2's Head!"]

                game_close = True

        # Updates snake 1
        if len(snake_List) > Length_of_snake1:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                win_info = ["Player 2", "Player 1 hit themselves!"]
                game_close = True

        # Updates snake 2
        if len(snake2_List) > Length_of_snake2:
            del snake2_List[0]

        # Makes sure the snake can't hit itself
        for x in snake2_List[:-1]:
            if x == snake2_Head:
                win_info = ["Player 1", "Player 2 hit themselves!"]
                game_close = True
        
        # Draws snake 1
        our_snake(snake_block, snake_List, color1.get_value())

        # Draws snake 2
        our_snake(snake_block, snake2_List, color2.get_value())

        # Displays score
        Your_score(Length_of_snake1 - 1, Length_of_snake2 - 1)
 
        pygame.display.update()
 
        # Checks if snake 1 eats a food
        if snake1_x1 == foodx and snake1_y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake1 += 1

         # Checks if snake 2 eats a food
        if snake2_x1 == foodx and snake2_y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake2 += 1

        clock.tick(snake_speed)
    
    # quits if loop ends
    pygame.quit()
    quit()
 
# Creates a menu when the game first starts
menu = pygame_menu.Menu('Snake', 600, 400,
                       theme=pygame_menu.themes.THEME_DARK)
menu.add.button('Play', gameLoop)

# Color selection 1
color1 = menu.add.color_input('Snake color 1: ',
                     color_type=pygame_menu.widgets.COLORINPUT_TYPE_RGB,
                     default=(200, 0, 0), font_size=20, margin=(0, 0))

# Color selection 2
color2 = menu.add.color_input('Snake color 2: ',
                     color_type=pygame_menu.widgets.COLORINPUT_TYPE_RGB,
                     default=(0, 0, 200), font_size=20, margin=(0, 0))

menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(dis)
