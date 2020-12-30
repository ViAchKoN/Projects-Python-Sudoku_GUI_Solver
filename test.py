import pygame
import pygame.freetype

pygame.init()
size = (640, 480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

def game_state(surf):
    rect = pygame.Rect(200, 200, 32, 32)
    while True:
        events = yield
        pressed = pygame.key.get_pressed()
        x = 1 if pressed[pygame.K_RIGHT] else -1 if pressed[pygame.K_LEFT] else 0
        rect.move_ip(x*5, 0)
        pygame.draw.rect(surf, pygame.Color('dodgerblue'), rect)
        yield

def title_state(surf):
    text = 'Awesome Game'
    colors = [[255, 255, 255, 20] for letter in text]
    font = pygame.freetype.SysFont(None, 22)
    font.origin = True
    while True:
        for color in colors:
            color[3] += 33
            if color[3] > 255: color[3] = 0
            x = 200
            for (letter, c) in zip(text, colors):
                bounds = font.get_rect(letter)
                font.render_to(surf, (x, 100), letter, c)
                x += bounds.width + 1

            font.render_to(surf, (180, 150), 'press [space] to start', pygame.Color('grey'))
            event = yield
            yield

def main():
    title = title_state(screen)
    game = game_state(screen)
    state = title

    while True:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    return
                if e.key == pygame.K_SPACE:
                    state = game if state == title else title
                if e.key == pygame.K_f:
                    if screen.get_flags() & pygame.FULLSCREEN:
                        pygame.display.set_mode(size)
                    else:
                        pygame.display.set_mode(size, pygame.FULLSCREEN)

        screen.fill(pygame.Color('grey12'))
        next(state)
        state.send(events)
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
