import pygame
import sys
from objects import Snake
from objects import Food
import settings as sett
import screen_modifications as sm


def GameLoop():
    errors = pygame.init()[1]
    if errors > 0:
        print(f"[!] Game had {errors} when starting, exiting...")
        sys.exit(-1)
    else:
        print("[+] Successfully started game")

    fps_controller = pygame.time.Clock()
    game_window = pygame.display.set_mode(
        (sett.SCREEN_WIDTH, sett.SCREEN_HEIGHT), 0, 32
    )
    pygame.display.set_caption("Snake game")

    surface = pygame.Surface(game_window.get_size())
    surface = surface.convert()
    sm.title_screen(game_window)
    sm.draw_grid(surface)

    snake = Snake()
    food = Food(snake.get_head_position())

    while True:
        fps_controller.tick(sett.FPS_MAX)
        snake.handle_keys()
        sm.draw_grid(surface)
        gaming = snake.move()
        if not gaming:
            sm.game_over_screen(game_window, snake)
        else:
            if snake.get_head_position() == food.position:
                snake.addCube(food)
                pygame.display.set_caption(f"Snake game | Score: {snake.score}")
            snake.draw(surface)
            food.draw(surface)
            game_window.blit(surface, (0, 0))
            pygame.display.update()


GameLoop()
