import pygame 

pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 1400, 800
FPS = 20
window = pygame.display.set_mode((WIDTH, HEIGHT))
layer_amount = 6
layer_height = 5

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        layer_amount += 1

    if keys[pygame.K_LEFT]:
        layer_amount -= 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        layer_height += 1

    if keys[pygame.K_DOWN]:
        layer_height -= 1


    cords = [[((WIDTH//layer_amount)*i, (HEIGHT//layer_height)*j) for i in range(1, layer_amount)] for j in range(1, layer_height)]
    try:
        for i in range(-1, 1):
            for j in range(-1, 1):
                cords[i].pop(j)
    except:
        pass


    window.fill('black')

    for i, cord in enumerate(cords):
        for c in cord:
            pygame.draw.circle(window, 'red', c, max(WIDTH, HEIGHT)//(layer_amount*layer_height))
            if cords.index(cord) == len(cords) - 1:
                continue
            for n in cords[cords.index(cord)+1]:
                pygame.draw.line(window, 'white', c, n, 5)

    pygame.display.update()