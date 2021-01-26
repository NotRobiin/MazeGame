from pygame.image import load
from os.path import join


class Config:
    def __init__(self):
        self.window_title = "Maja's maze game"

        self.fps = 90

        self.bg_color = (140, 140, 140)

        self.block_size = 64

        self.maze = [
            "xxsxxxxxx",
            "xx  d   x",
            "xxxx xxrx",
            "xxx  x  x",
            "x  rxxx x",
            "x x   xxx",
            "xxxxx xxx",
            "xx d    x",
            "xxxxxxexx",
        ]

        self.font = {
            "s": {
                "size": 30,
                "name": "freesansbold.ttf",
                "color": (255, 255, 255),
                "text": "Start",
            },
            "e": {
                "size": 30,
                "name": "freesansbold.ttf",
                "color": (255, 255, 255),
                "text": "End",
            },
        }

        self.assets = {
            "blocks": {
                "d": load(join("assets/blocks", "dirtblock.png")),
                "r": load(join("assets/blocks", "rockpile64.png")),
                "x": load(join("assets/blocks", "lightblue.png")),
            }
        }
