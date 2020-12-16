import pygame
import settings as sett
import screen_modifications as sm
import random


class Snake(object):
    """Snake class"""

    def __init__(self):
        self.lenght = 1
        self.positions = [
            (
                (sett.GRID_WIDTH // 2) * sett.GRID_SIZE,
                (sett.GRID_HEIGHT // 2) * sett.GRID_SIZE,
            )
        ]
        self.direction = (0, 0)
        self.color = sett.SnakeColor
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        """Changes snakes self.direction"""
        if self.lenght > 1 and ((point[0] * -1, point[1] * -1) == self.direction):
            return
        else:
            self.direction = point

    def move(self):
        """Moves snake in the direction = self.direction"""
        curr_head_pos = self.get_head_position()
        x, y = self.direction
        new = (
            ((curr_head_pos[0] + x * sett.GRID_SIZE) % sett.SCREEN_WIDTH),
            ((curr_head_pos[1] + y * sett.GRID_SIZE) % sett.SCREEN_HEIGHT),
        )

        if len(self.positions) > 3 and new in self.positions[2:]:
            if self.score == sett.GRID_HEIGHT * sett.GRID_WIDTH - 1:
                print("(・_・ヾ")
                sm.close_game()
            return False
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.lenght:
                self.positions.pop()
            return True

    def reset(self):
        """Puts all values to default"""
        self.lenght = 1
        self.positions = [
            (
                (sett.GRID_WIDTH // 2) * sett.GRID_SIZE,
                (sett.GRID_HEIGHT // 2) * sett.GRID_SIZE,
            )
        ]
        self.direction = (0, 0)
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            rect = pygame.Rect(p[0], p[1], sett.GRID_SIZE, sett.GRID_SIZE)
            pygame.draw.rect(surface, self.color, rect)
            pygame.draw.rect(surface, sett.White, rect, 1)

    def handle_keys(self):
        """Handling pressed keys"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sm.close_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.turn(sett.UP)
                    break
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.turn(sett.DOWN)
                    break
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.turn(sett.LEFT)
                    break
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.turn(sett.RIGHT)
                    break
                elif event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

    def addCube(self, food):
        self.lenght += 1
        self.score += 1
        food.randomize_position(self.positions)


class Food(object):
    def __init__(self, positions=[]):
        self.position = (0, 0)
        self.color = sett.FoodColor
        self.randomize_position(positions)

    def randomize_position(self, positions=[]):
        while True:
            self.position = (
                random.randint(0, sett.GRID_WIDTH - 1) * sett.GRID_SIZE,
                random.randint(0, sett.GRID_HEIGHT - 1) * sett.GRID_SIZE,
            )
            if self.position not in positions:
                break

    def draw(self, surface):
        rect = pygame.Rect(
            (self.position[0], self.position[1]), (sett.GRID_SIZE, sett.GRID_SIZE)
        )
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, sett.White, rect, 1)
