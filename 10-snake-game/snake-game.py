"""

"""

import pygame
import time
import random
# Imports menu
import pygame_menu 

pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
# Changed the score to display both p1's score and p2's score
def Your_score(p1_score, p2_score):
    score_title_txt = score_font.render("Score", True, yellow)
    score_txt = score_font.render(str(p1_score) + "|" + str(p2_score), True, yellow)

    dis.blit(score_title_txt, [(dis_width / 2) - (score_title_txt.get_width() / 2), 0])
    dis.blit(score_txt, [(dis_width / 2) - (score_txt.get_width() / 2), score_title_txt.get_height() - 10])
 
 
# Added snakenum to differenciate between the snakes and their colors 
def our_snake(snake_block, snake_list, snakeColor):
    for x in snake_list:
        pygame.draw.rect(dis, snakeColor, [x[0], x[1], snake_block, snake_block])
 
#  Centered the message and added height variable
def message(msg, color, height):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [(dis_width / 2) - (mesg.get_width() / 2), height])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    snake1_x1 = (dis_width * 1) / 4 
    snake1_y1 = dis_height / 2
 
    snake1_x1_change = 0
    snake1_y1_change = 0
 
    snake_List = []
    Length_of_snake1 = 1

    # Snake 2 variables
    snake2_x1 = (dis_width * 3) / 4 
    snake2_y1 = dis_height / 2
 
    snake2_x1_change = 0
    snake2_y1_change = 0
 
    snake2_List = []
    Length_of_snake2 = 1


    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red, dis_height / 3)
            message("Player1" + win_info[0] + " Won!", red, dis_height / 3 + 40)
            Your_score(Length_of_snake1 - 1, Length_of_snake2 - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
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

                # Movement for second snake
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

        # Print statements
        print("Snake 1")
        print(snake_List)
        print("Snake 2")
        print(snake2_List)
        print("")


        if snake1_x1 >= dis_width or snake1_x1 < 0 or snake1_y1 >= dis_height or snake1_y1 < 0:
            game_close = True
            win_txt = score_font.render("Player 2 Wins!", True, yellow)
            win_reason = score_font.render("Player 1 hit the edge", True, yellow)

            dis.blit(win_txt, [(dis_width / 2) - (win_txt.get_width() / 2), dis_width / 2])
            dis.blit(win_reason, [(dis_width / 2) - (win_txt.get_width() / 2), dis_width / 2])

        snake1_x1 += snake1_x1_change
        snake1_y1 += snake1_y1_change

        # Snake 2 changes in direction and checks if its off the window
        if snake2_x1 >= dis_width or snake2_x1 < 0 or snake2_y1 >= dis_height or snake2_y1 < 0:
            game_close = True

        snake2_x1 += snake2_x1_change
        snake2_y1 += snake2_y1_change


        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(snake1_x1)
        snake_Head.append(snake1_y1)
        snake_List.append(snake_Head)

        # Second snake 
        snake2_Head = []
        snake2_Head.append(snake2_x1)
        snake2_Head.append(snake2_y1)
        snake2_List.append(snake2_Head)

        # First snake cant hit the second one
        for i in range(len(snake2_List)):
            if snake_Head[0] == snake2_List[i][0] and snake_Head[1] == snake2_List[i][1]:
                game_close = True

        # Second snake cant hit the first one
        for i in range(len(snake_List)):
            if snake2_Head[0] == snake_List[i][0] and snake2_Head[1] == snake_List[i][1]:
                game_close = True


        if len(snake_List) > Length_of_snake1:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Second snake cant hit itself
        if len(snake2_List) > Length_of_snake2:
            del snake2_List[0]

        for x in snake2_List[:-1]:
            if x == snake2_Head:
                game_close = True
        
        # added number for snake color
        our_snake(snake_block, snake_List, color1.get_value())

        # Draws the second snake
        our_snake(snake_block, snake2_List, color2.get_value())

        Your_score(Length_of_snake1 - 1, Length_of_snake2 - 1)
 
        pygame.display.update()
 
        if snake1_x1 == foodx and snake1_y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake1 += 1
 
        # Snake 2 eat food
        if snake2_x1 == foodx and snake2_y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake2 += 1

        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
# Add menu
menu = pygame_menu.Menu('Snake', 600, 400,
                       theme=pygame_menu.themes.THEME_DARK)
menu.add.button('Play', gameLoop)

color1 = menu.add.color_input('Snake color 1: ',
                     color_type=pygame_menu.widgets.COLORINPUT_TYPE_RGB,
                     default=(200, 0, 0), font_size=15, margin=(0, 0))

color2 = menu.add.color_input('Snake color 2: ',
                     color_type=pygame_menu.widgets.COLORINPUT_TYPE_RGB,
                     default=(0, 0, 200), font_size=15, margin=(0, 0))

menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(dis)
