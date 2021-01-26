import pygame


class Game:
    def __init__(self, cfg):
        self.cfg = cfg
        self.window = None
        self.level = None

    def setup(self, lvl) -> None:
        pygame.init()
        pygame.display.set_caption(self.cfg.window_title)

        bs = self.cfg.block_size
        size = (bs * len(self.cfg.maze[0]), bs * len(self.cfg.maze))

        self.window = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.level = lvl

    def draw(self) -> None:
        self.level.draw(self.window)

    def event(self, e) -> None:
        print(f"Event: {e}")

    def loop(self) -> None:
        while True:
            self.clock.tick(self.cfg.fps)

            for e in pygame.event.get():
                self.event(e)

            self.draw()
            pygame.display.update()
