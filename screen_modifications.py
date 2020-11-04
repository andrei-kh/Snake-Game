import pygame
import sys
import settings as sett
import time


def draw_grid(surface):
    '''Draws grid on the given surface.\n
       Grid size can be changed in settings.'''
    for x in range(sett.GRID_WIDTH):
        for y in range(sett.GRID_HEIGHT):
            rect = pygame.Rect((x * sett.GRID_SIZE, y * sett.GRID_SIZE),
                               (sett.GRID_SIZE, sett.GRID_SIZE))
            if (x + y) % 2 == 0:
                pygame.draw.rect(surface, sett.GridColor1, rect)
            else:
                pygame.draw.rect(surface, sett.GridColor2, rect)


def title_screen(surface):
    '''Draws Title screen'''
    surface.fill(sett.GridColor1)
    # Snake
    draw_text(surface, 'comic sans', 120, 'SNAKE', sett.SnakeColor,
              (sett.SCREEN_WIDTH // 2, sett.SCREEN_HEIGHT // 3))
    # Press any key
    draw_text(surface, 'times', 20, 'Press any key to continue',
              sett.SnakeColor, (sett.SCREEN_WIDTH // 2, int(sett.SCREEN_HEIGHT / 1.8)))
    pygame.display.flip()

    idle()


def game_over_screen(surface, snake):
    '''Draws game over screen on surface.\n
       Snake needed for score.'''
    surface.fill(sett.Black)
    # You Died message
    draw_text(surface, 'times new roman', 90, 'YOU DIED', sett.Red,
              (sett.SCREEN_WIDTH // 2, sett.SCREEN_HEIGHT // 4))
    # Score
    draw_text(surface, 'times', 25, f'Score: {snake.score}', sett.Red,
              (sett.SCREEN_WIDTH // 2, int(sett.SCREEN_HEIGHT / 1.25)))
    pygame.display.flip()

    snake.reset()

    time.sleep(1)
    # Press any key message
    draw_text(surface, 'times', 20, 'Press any key to continue',
              sett.LightRed, (sett.SCREEN_WIDTH // 2, int(sett.SCREEN_HEIGHT / 1.8)))
    pygame.display.flip()

    time.sleep(1)

    idle()


def draw_text(surface, font='times', fsize=14, text='', Color=sett.White, position=(0, 0)):
    text_font = pygame.font.SysFont(font, fsize)
    text_surface = text_font.render(text, True, Color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = position
    surface.blit(text_surface, text_rect)


def idle():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                else:
                    return


def close_game():
    '''Terminates program.'''
    print("[-] Quiting... ('_')")
    pygame.quit()
    sys.exit()
