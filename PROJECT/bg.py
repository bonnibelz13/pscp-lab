import pygame
pygame.init()

clock = pygame.time.Clock()
FPS = 60

#game window width and height
screen_width = 780
screen_height = 680

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('HATYAI CHICKEN\'S SPACE WAR')

#def game variables
scroll = 0


bg_imgs = []
for i in range(1, 6):
    bg_img = pygame.image.load(f'town.jpg').convert_alpha()
    bg_imgs.append(bg_img)
bg_width = bg_imgs[0].get_width()

def draw_bg():
    for x in range(5):
        speed = 1
        for i in bg_imgs:
            screen.blit(i, ((x * bg_width) - scroll * speed, 0))


#game loop เปิดตัวเกมอยู่
run = True
while run:

    clock.tick(FPS)

    #draw world
    draw_bg()

    #get keypresses
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and scroll > 0:
        scroll -= 5
    if key[pygame.K_RIGHT] and scroll < 3000:
        scroll += 5

    #event handlers ปิดตัวเกม
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
