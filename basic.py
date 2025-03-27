import pygame
from settings import Settings
from player import Player
from bubble import Bubble
import game_functions as gf


def run_game():
    gm_set = Settings()
    pygame.init()

    screen = pygame.display.set_mode((gm_set.screen_width, gm_set.screen_height))
    pygame.display.set_caption(gm_set.caption)
    running = True

    player = Player(screen)
    
    bubbles = pygame.sprite.Group()
        
    while True:
        gf.check_events(player, screen, gm_set, bubbles)
        player.update()
        bubbles.update()
        gf.update_screen(gm_set, screen, player, bubbles)
    
run_game()
