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

# Added a list of different colors for the snakes
snakeColors = [(180, 30, 60), (0, 60, 120)]

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
 
 
# Added snakenum to differenciate between the snakes and thier colors 
def our_snake(snake_block, snake_list, snakenum):
    for x in snake_list:
        pygame.draw.rect(dis, snakeColors[snakenum], [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
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
            message("You Lost! Press C-Play Again or Q-Quit", red)
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
                if event.key == pygame.K_LEFT:
                    if snake1_x1_change != snake_block:
                        snake1_x1_change = -snake_block
                        snake1_y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    if snake1_x1_change != -snake_block:
                        snake1_x1_change = snake_block
                        snake1_y1_change = 0
                elif event.key == pygame.K_UP:
                    if snake1_y1_change != snake_block:
                        snake1_y1_change = -snake_block
                        snake1_x1_change = 0
                elif event.key == pygame.K_DOWN:
                    if snake1_y1_change != -snake_block:
                        snake1_y1_change = snake_block
                        snake1_x1_change = 0

                # Movement for second snake
                if event.key == pygame.K_a:
                    if snake2_x1_change != snake_block:
                        snake2_x1_change = -snake_block
                        snake2_y1_change = 0
                elif event.key == pygame.K_d:
                    if snake2_x1_change != -snake_block:
                        snake2_x1_change = snake_block
                        snake2_y1_change = 0
                elif event.key == pygame.K_w:
                    if snake2_y1_change != snake_block:
                        snake2_y1_change = -snake_block
                        snake2_x1_change = 0
                elif event.key == pygame.K_s:
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
        our_snake(snake_block, snake_List, 0)

        # Draws the second snake
        our_snake(snake_block, snake2_List, 1)

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

        clock.tick(6) # originally snake_speed
 
    pygame.quit()
    quit()
 
# Add menu
menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

# menu.add.text_input('Name :', default='John Doe')
# menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', gameLoop)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(dis)
