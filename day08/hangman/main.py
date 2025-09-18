import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()
# Window size
X = 1000
Y = 681
# Set up the game window
screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Hangman game")


# Charge l'image de background
imp = pygame.image.load(
    "hangman/assets/tree.jpg"
).convert()  # Load an image from a file source and convert it to cover
screen.blit(
    imp, (0, 0)
)  # Les Blit sont des fonctions de rendu spéciales permettant de copier une partie rectangulaire de la mémoire vidéo vers une autre
pygame.display.flip()  # Update the full display Surface to the screen


def draw_hangman():
    base = pygame.draw.line(screen, (0, 0, 0), [100, 600], [250, 600], 20)
    pole1 = pygame.draw.line(screen, (0, 0, 0), [165, 600], [165, 210], 12)
    support = pygame.draw.polygon(
        screen, (0, 0, 0), [[300, 210], [165, 300], [165, 210]], 5
    )
    pole2 = pygame.draw.line(screen, (0, 0, 0), [158, 210], [500, 210], 12)
    rope1 = pygame.draw.line(screen, (0, 0, 0), [500, 210], [500, 280], 5)
    head = pygame.draw.circle(screen, (0, 0, 0), [500, 280], 40)
    body = pygame.draw.line(screen, (0, 0, 0), [500, 230], [500, 400], 7)
    left_arm = pygame.draw.line(screen, (0, 0, 0), [500, 340], [550, 375], 7)
    right_arm = pygame.draw.line(screen, (0, 0, 0), [500, 340], [450, 375], 7)
    left_leg = pygame.draw.line(screen, (0, 0, 0), [500, 400], [550, 450], 7)
    right_leg = pygame.draw.line(screen, (0, 0, 0), [500, 400], [450, 450], 7)


def draw_full_gallow():
    base = pygame.draw.line(screen, (0, 0, 0), [100, 600], [250, 600], 20)
    pole1 = pygame.draw.line(screen, (0, 0, 0), [165, 600], [165, 210], 12)
    support = pygame.draw.polygon(
        screen, (0, 0, 0), [[300, 210], [165, 300], [165, 210]], 5
    )
    pole2 = pygame.draw.line(screen, (0, 0, 0), [158, 210], [500, 210], 12)
    rope1 = pygame.draw.line(screen, (0, 0, 0), [500, 210], [500, 280], 5)


def draw_head():
    head = pygame.draw.circle(screen, (0, 0, 0), [500, 280], 40)


def draw_body():
    body = pygame.draw.line(screen, (0, 0, 0), [500, 230], [500, 400], 7)


def draw_arm1():
    left_arm = pygame.draw.line(screen, (0, 0, 0), [500, 340], [550, 375], 7)


def draw_arm2():
    right_arm = pygame.draw.line(screen, (0, 0, 0), [500, 340], [450, 375], 7)


def draw_leg1():
    left_leg = pygame.draw.line(screen, (0, 0, 0), [500, 400], [550, 450], 7)


def draw_leg2():
    right_leg = pygame.draw.line(screen, (0, 0, 0), [500, 400], [450, 450], 7)


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                draw_hangman()
                pygame.display.update()


# Quit Pygame
pygame.quit()
