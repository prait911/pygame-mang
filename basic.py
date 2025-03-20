import pygame

pygame.init()
(width, height) = (800, 600)
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
        
    screen.fill("dark blue")

    pygame.display.flip()
    
    pygame.display.set_caption('Bubbler blaster')
        
pygame.quit()
