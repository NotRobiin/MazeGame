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

        self.buttons = {
            "main": {
                "start": (33, 220, 207, 290),
                "highscore": (33, 336, 207, 409),
                "exit": (33, 449, 207, 522),
            },
            "character": {"girl": (23, 196, 326, 263), "boy": (24, 414, 330, 480),},
            "level": {
                "1": {
                    "image": load(join("assets/menu", "level1preview.png")),
                    "pos": (50, 150, 347, 330),
                },
                "2": {
                    "image": load(join("assets/menu", "level1preview.png")),
                    "pos": (367, 350, 564, 540),
                },
            },
        }

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
            },
            "player": {
                "girl": load(join("assets/player", "girl.png")),
                "boy": load(join("assets/player", "boy.png")),
            },
            "main_menu": {"background": load(join("assets/menu", "Menuscreen.jpg"))},
            "character": {
                "background": load(join("assets/menu", "characterselect.png"))
            },
            "level": {"background": load(join("assets/menu", "levelselect.jpg")),},
        }
