import sys, os
import pygame
import datetime
from pygame.locals import *
from pygame.color import THECOLORS

class GamWindow:
    def __init__(self, screen_tuple_px):
        self.width_px = screen_tuple_px[0]
        self.height_px = screen_tuple_px[1]

        self.surface = pygame.display.set_mode(screen_tuple_px)
        #paint screen black
        self.erase_and_update()

    def update_caption(self, title):
        pygame.display.set_caption(title)
        self.caption = title

    def erase_and_update(self):
        self.surface.fill(THECOLORS['black'])
        pygame.display.flip()

class Detroit:
    def __init__(self, color=THECOLORS['white'], left_px=10, width_px=98, speed_mps=1):
        self.color = color
        self.height_px = height_px
        self.top_px = game_window.height_px - self.height_px
        self.width_px = width_px
        self.width_m = env.m_from_px(width_px)
        self.halfwidth_m = self.width_m/2.0
        self.height_m = env.m_from_px(left_px) + self.halfwidth_m

        self.center_m = env.m_from_px(left_px) - self.halfwidth_m
        self.speed_mps = speed_mps
        self.rect = pygame.Rect(left_px, self.top_px, self.width_px, self.height_px)

    def draw_car(self):
        self.rect.centerx = env.px_from_m(self.center_m)
        pygame.draw.rect(game_window.surface, self.color, self.rect)

class AirTrack:
    def __init__(self):
        self.cars = []

    def update_SpeedandPosition(self, car, dt_s):
        car.center_m = car.center_m + (car.speed_mps)

    def make_some_cars(self, nmode):
        game_window.update_caption("Air Track (basic): Demo" + str(nmode))
        if (nmode == 1):
            self.cars.append(Detroit(color=THECOLORS['red'], left_px=240, speed_mps=0.2))
            self.cars.append(Detroit(color=THECOLORS['blue'], left_px=340, speed_mps=-0.2))
        elif (nmode == 2):
            self.cars.append(Detroit(color=THECOLORS['red'], left_px=240, speed_mps=-0.1))
            self.cars.append(Detroit(color=THECOLORS['blue'], left_px=440, speed_mps=-0.2))
        elif (nmode == 3):
            n_colors= 20
            for j, eachcolor in enumerate(THECOLORS):
                self.cars.append(Detroit(color=THECOLORS[eachcolor], width_px=15,left_px=450, speed_mps=0.05*(j-n_colors/2.0)))
                if j > n_colors: break

        elif (nmode == 4):
            n_colors= 180
            for j, eachcolor in enumerate(THECOLORS):
                self.cars.append(Detroit(color=THECOLORS[eachcolor], width_px=15,left_px=450, speed_mps=0.01*(j-n_colors/2.0)))
                if j > n_colors: break

        elif (nmode == 5):
            n_colors= 300
            for j, eachcolor in enumerate(THECOLORS):
                self.cars.append(Detroit(color=THECOLORS[eachcolor], width_px=15,left_px=450, speed_mps=0.01*(j-n_colors/2.0)))
                if j > n_colors: break

class Environment:
    def __init__(self, length_px, length_m):
        self.px_to_m = length_m/float(length_px)
        self.m_to_px = (float(length_px)/length_m)

    def px_from_m(self, dx_m):
        return int(round(dx_m * self.m_to_px))

    def m_from_px(self, dx_px):
        return float(dx_px) * self.px_to_m

    def get_local_user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    return 'quit'
                elif event.key == K_1:
                    return 1
                elif event.key == K_2:
                    return 2
                elif event.key == K_3:
                    return 3
                elif event.key == K_4:
                    return 4
                elif event.key == K_5:
                    return 5
                else:
                    return "Nothing set up for this key"


def main():
    global env, game_window, air_track

    pygame.init()
    window_size_px = window_width_px, window_height_px = (950,120)
    env = Environment(window_size_px, 1.5)
    game_window = GamWindow(window_size_px)
    air_track = AirTrack()
    air_track.make_some_cars(1)
    myclock = pygame.time.Clock()
    framerate_limit = 400

    time_s = 0.0
    user_done = False

    while not user_done:
        game_window.surface.fill(THECOLORS['black'])
        dt_s = float(myclock.tick(framerate_limit) * 1e-3)
        resetmode = env.get_local_user_input()
        if resetmode in [0,1,2,3,4,5,6,7,8,9]:
            print "reset mode %r" % (resetmode)

            air_track.cars= []
            game_window.erase_and_update()
            air_track.make_some_cars(resetmode)

        elif resetmode == 'quit':
            user_done = True
        elif resetmode != None:
            print resetmode

        for car in air_track.cars:
            air_track.update_SpeedandPosition(car, dt_s)

        for car in air_track.cars:
            car.draw_car()
        time_s += dt_s
        pygame.display.flip()

main()
