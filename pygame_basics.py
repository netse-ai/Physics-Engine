import sys, os
import pygame

from pygame.locals import *
from pygame.color import THECOLORS

pygame.init()

display_surface = pygame.display.set_mode((600,400))

myclock = pygame.time.Clock()

display_surface.fill(THECOLORS["white"])

framerate_limit = 120
time_s = 0.0
key_e = "U"
key_f = "U"
user_done = False
mouse_button_UD = "U"

while not user_done:
    dt_s = float(myclock.tick(framerate_limit) * 1e-3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            user_done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                user_done = True
            elif event.key == K_e:
                key_e = "D"
            elif event.key == K_f:
                key_f == "D"

        elif event.type == pygame.KEYUP:
            if event.key == K_e:
                key_e = "U"
            elif event.key == K_f:
                key_f = "U"

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_button_UD == "D"

            (button1, button2, button3) = pygame.mouse.get_pressed()

            if button1:
                mouse_button = 1
            elif button2:
                mouse_button = 2
            elif button3:
                mouse_button = 3
            else:
                mouse_button = 0

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_button_UD = "U"

    mouse_xy = pygame.mouse.get_pos()


    if key_e == "D":
        display_surface.fill(THECOLORS['grey'])
    if mouse_button_UD == "D" and mouse_button == 1:
        circle_color = THECOLORS["yellow"]
    elif mouse_button_UD == "D" and mouse_button == 3:
        circle_color = THECOLORS["red"]
    else:
        circle_color = THECOLORS["blue"]

    pygame.draw.circle(display_surface, circle_color, mouse_xy, 10, 0)
    time_s += dt_s

    print time_s, dt_s, myclock.get_fps()

    if key_f != 'D':
        pygame.display.flip()
