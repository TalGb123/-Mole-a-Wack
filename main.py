import pygame
from constants import *
import random


def add_image(img_path, x_pos, y_pos, width, height):
    img = pygame.image.load(img_path)
    img = pygame.transform.scale(img,
                                 (width, height))
    screen.blit(img, (x_pos, y_pos))


def rand_squirrel_location(start_x_pos, space_x_pos, y_pos):
    squirrel_location = [0, 1, 2]
    x_pos = start_x_pos + space_x_pos * random.choice(squirrel_location)
    return [x_pos, y_pos]


def set_text(font_name, font_size, massage, text_location, color):
    font = pygame.font.SysFont(font_name,
                               font_size)
    text = font.render(massage, True, color)
    screen.blit(text, text_location)


def update_square(start_x_pos, space_x_pos, y_pos, squirrel_width, squirrel_height):
    squirrel_location = rand_squirrel_location(start_x_pos, space_x_pos, y_pos)
    for i in range(5):
        add_image(SQUIRREL_IMAGE, squirrel_location[0], squirrel_location[1]-i*20 ,
              squirrel_width, squirrel_height)
        pygame.time.wait(100)

def click_on_spot(start_x_pos, space_x_pos, y_pos, mouse_pos):
    squirrel_location = rand_squirrel_location(start_x_pos, space_x_pos, y_pos)
    if (mouse_pos[0] >= squirrel_location[0] and mouse_pos[0] <= squirrel_location[0]+space_x_pos and
            mouse_pos[1] >= squirrel_location[1] and mouse_pos[1] <= squirrel_location[1]):
        return True
    return False

def main():
    pygame.init()
    # Setting the screen
    global screen
    global score
    score = 0
    screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("wack a mole")
    screen.fill(GREEN)

    set_text("Arial", 24, "SCORE: " + str(score), SCORE_TEXT_POS, WHITE)
    squirrel_location = rand_squirrel_location(START_X_POS_SQU, SPACE_X_POS_SQU, START_Y_POS_SQU)
    # Screen update
    for i in range(3):
        add_image(CARROT_IMAGE, START_X_POS_CAR + SPACE_X_POS_CAR * i, Y_POS_CAR,
                  CARROT_WIDTH, CARROT_HEIGHT)
        add_image(HOLE_IMAGE, START_X_POS_HOL + SPACE_X_POS_HOL * i, Y_POS_HOL,
                  HOLE_WIDTH, HOLE_HEIGHT)
    add_image(SQUIRREL_IMAGE, squirrel_location[0], squirrel_location[1],
              SQUIRREL_WIDTH, SQUIRREL_HEIGHT)

    square = pygame.Rect(squirrel_location[0], MIDLINE,
                         SQUARE_WIDTH, SQUARE_HIGHT)
    pygame.draw.rect(screen, GREEN, square)

    for i in range(3):
        add_image(HALF_HOLE_IMAGE, START_X_POS_HOL + SPACE_X_POS_HOL * i, MIDLINE, HALF_HOLE_WIDTH, HALF_HOLE_HEIGHT)

    finish = False
    while not finish:
        # Checking events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill(GREEN)
                score += 1
                mouse_pos = pygame.mouse.get_pos()
                if click_on_spot(START_X_POS_SQU, SPACE_X_POS_SQU, START_Y_POS_SQU, mouse_pos):
                # update_square(START_X_POS_SQU, SPACE_X_POS_SQU, START_Y_POS_SQU, SQUIRREL_WIDTH, SQUIRREL_HEIGHT)
                    set_text("Arial", 24, "SCORE: " + str(score), SCORE_TEXT_POS, WHITE)
                    # Screen update
                    for i in range(3):
                        add_image(CARROT_IMAGE, START_X_POS_CAR + SPACE_X_POS_CAR * i, Y_POS_CAR,
                                  CARROT_WIDTH, CARROT_HEIGHT)
                        add_image(HOLE_IMAGE, START_X_POS_HOL + SPACE_X_POS_HOL * i, Y_POS_HOL,
                                  HOLE_WIDTH, HOLE_HEIGHT)
                    squirrel_location = rand_squirrel_location(START_X_POS_SQU, SPACE_X_POS_SQU, START_Y_POS_SQU)
                    add_image(SQUIRREL_IMAGE, squirrel_location[0], squirrel_location[1],
                              SQUIRREL_WIDTH, SQUIRREL_HEIGHT)

                    square = pygame.Rect(squirrel_location[0], MIDLINE,
                                         SQUARE_WIDTH, SQUARE_HIGHT)
                    pygame.draw.rect(screen, GREEN, square)

                    for i in range(3):
                        add_image(HALF_HOLE_IMAGE, START_X_POS_HOL + SPACE_X_POS_HOL * i, MIDLINE, HALF_HOLE_WIDTH,
                                  HALF_HOLE_HEIGHT)

        pygame.display.flip()
    pygame.quit()


main()