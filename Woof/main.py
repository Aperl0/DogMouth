import os
import time
#Pygame import
import pygame

#import pygame.locals for keys
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            print("up")
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            print("down")
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            print("left")
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            print("right")
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 600:
            self.rect.bottom = 600

pygame.init()

window = pygame.display.set_mode([800, 600])

player = Player()

#run until user quits
running = True
while running:
    #did user click window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            #was it escape key?
            if event.key == K_ESCAPE:
                running = False

    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)

    window.fill((0, 0, 0))

    window.blit(player.surf, player.rect)

    pygame.display.flip()

#quit
pygame.quit()

# def main():
#     print("PALAMAGOO DATING SIM")
#     print("===--------------===")

#     print("===========")
#     print("=  o   o  =")
#     print("=    |    =")
#     print("=         =")
#     print("=  \___/  =")
#     print("===========")
#     print()
#     print("Welcome to the game")
#     print("Enter your name down below.")
#     name = str(input("> "))
#     print()
#     time.sleep(2)
#     os.system('clear')
#     if name.lower() == "palamagoo":
#         print("===\===/===")
#         print("=  o   o  =")
#         print("=    |    =")
#         print("=   ___   =")
#         print("=  /   \  =")
#         print("===========")
#         print()
#         print("Thats... MY NAME!!!! YOU LITTLE PIECE OF SHIT")
#         print("You were brutally stabbed 28.3 times")
#     else:
#         print("So, you're name is " + name + "? What a loveeeeely name. My name Palamagoo!!")
#         print("So what do you wanna do today my lovely little darling lovely?")
    


if __name__ == '__main__': main()