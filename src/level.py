import pygame


class Level:
    def __init__(self, config):
        self.cfg = config

    def draw(self, surface) -> None:
        # Draw background
        surface.fill(self.cfg.bg_color)

        maze = self.cfg.maze

        # Draw map
        for maze_y in range(len(maze)):
            for maze_x in range(len(maze[maze_y])):
                field = maze[maze_y][maze_x]
                x = maze_x * self.cfg.block_size
                y = maze_y * self.cfg.block_size

                if field in ["s", "e"]:
                    self.draw_text(surface, field, x, y)
                else:
                    self.draw_block(surface, field, x, y)

    def draw_block(self, surface, field, x, y):
        if field in self.cfg.assets["blocks"].keys():
            image = self.cfg.assets["blocks"][field]
            surface.blit(image, (x, y))

    def draw_text(self, surface, field, x, y):
        # Prepare font and render obj
        font = self.cfg.font[field]
        text = pygame.font.SysFont(font["name"], font["size"])
        source = text.render(font["text"], True, font["color"])

        # Center text inside the block that it's in
        bs = self.cfg.block_size / 2
        rect = source.get_rect(center=(x + bs, y + bs))

        surface.blit(source, rect)
