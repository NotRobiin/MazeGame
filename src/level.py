import pygame


class Level:
    def __init__(self, config):
        self.cfg = config

    def get_starting_pos(self) -> tuple:
        for y in range(len(self.cfg.maze)):
            for x in range(len(self.cfg.maze[y])):
                field = self.cfg.maze[y][x]

                if field == "s":
                    bs = self.cfg.block_size
                    pos = (x * bs, y * bs)

                    return pos

    def get_block(self, x: int, y: int) -> str:
        bs = self.cfg.block_size
        j, i = int(y / bs), int(x / bs)

        # Outside the map, just mark it as a wall
        if j >= len(self.cfg.maze[0]) or i >= len(self.cfg.maze):
            return "x"

        return self.cfg.maze[j][i]

    def update_block(self, x, y, new):
        bs = self.cfg.block_size
        j, i = int(y / bs), int(x / bs)

        if j >= len(self.cfg.maze[0]) or i >= len(self.cfg.maze):
            return 0

        text = list(self.cfg.maze[j])
        text[i] = new
        self.cfg.maze[j] = "".join(text)
        print(i, j)

        return 1

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
