import pokebase
import pygame

pygame.init()

bulbasaur = pokebase.pokemon_sprite(1)

print(bulbasaur.path)

screen = pygame.display.set_mode((800, 600))

saurImage = pygame.image.load(bulbasaur.path)

screen.blit(saurImage, (0, 0))

def displayPokemon():

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

pygame.display.update()
displayPokemon()