from tkinter import Y
import pygame
from pygame.locals import *
from random import randint

width = 500
height = 400

SIZE = 500,400

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

YELLOW = (255,255,0)
MAGENTA = (255,0,255)
CYAN = (0,255,255)

BLACK = (0,0,0)
GRAY = (150,150,150)
WHITE = (255,255,255)

PINK = (255, 119, 215)
PURPLE = (128, 0, 128)


dir = {K_LEFT: (-5,0), K_RIGHT: (5,0), K_UP: (0, -5), K_DOWN: (0,5)}



rect = Rect(0,0,100,100)

class particle:
    def __init__(self,circleRadius,position,velocity,color):
        self.position = position
        self.velocity = velocity
        self.circleRadius = circleRadius
        if color == 1:
            self.color = PURPLE
        elif color == 2:
            self.color = CYAN
        elif color == 3:
            self.color = RED
        elif color == 4:
            self.color = YELLOW
        elif color == 5:
            self.color = BLUE
        elif color == 6:
            self.color = WHITE
        elif color == 7:
            self.color = GREEN
        
def draw_text(text, pos):
    img = font.render(text, True, WHITE)
    screen.blit(img, pos)

def random_point():
    x = randint(20, width-20)
    y = randint(20,height-20)
    return(x,y)

def random_points(n):
    points = []
    for i in range(n):
        p = random_point()
        points.append(p)
    return points

def random_rects(n):
    rects = []
    for i in range(n):
        r = Rect(random_points(), (20,20))
        rects.append(r)
    return rects

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width/2),(height/2))
    screen.blit(TextSurf, TextRect)



pygame.init()
font_small = pygame.font.Font('data/fonts/font.otf', 32)
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 24)
running = True