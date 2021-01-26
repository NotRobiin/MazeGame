import pygame
from level import Level


class MainMenu:
    def __init__(self, game, config):
        self.cfg = config
        self.game = game
        self.buttons = []
        self.game.set_menu(self)

        for b in self.cfg.buttons["main"].keys():
            self.buttons.append(make_button(self, b, "main"))

    def pressed(self, which: str):
        if which == "start":
            CharacterMenu(self.game, self.cfg)

        elif which == "highscore":
            print("Clicked highscore")

        elif which == "exit":
            self.game.quit()

    def event(self, e):
        b = check_button_click(self, e, "main")

        if b and len(b):
            self.pressed(b)

    def draw(self, surface):
        bg = self.cfg.assets["main_menu"]["background"]
        surface.blit(bg, (0, 0))


class CharacterMenu:
    def __init__(self, game, config):
        self.game = game
        self.cfg = config
        self.game.set_menu(self)
        self.buttons = []

        for b in self.cfg.buttons["character"].keys():
            self.buttons.append(make_button(self, b, "character"))

    def pressed(self, which: str):
        self.game.player.set_gender(which)

        LevelMenu(self.game, self.cfg)

    def event(self, e):
        b = check_button_click(self, e, "character")

        if b and len(b):
            self.pressed(b)

    def draw(self, surface):
        bg = self.cfg.assets["character"]["background"]
        surface.blit(bg, (0, 0))


class LevelMenu:
    def __init__(self, game, config):
        self.game = game
        self.cfg = config
        self.game.set_menu(self)
        self.buttons = []
        self.previews = []

        for b in self.cfg.buttons["level"].keys():
            x, y, w, h = self.cfg.buttons["level"][b]["pos"]
            button = pygame.Rect(x, y, w - x, h - y)
            preview = {"image": self.cfg.buttons["level"][b]["image"], "pos": (x, y)}

            self.previews.append(preview)
            self.buttons.append(button)

    def pressed(self, which: str):
        self.game.set_menu(None)
        lvl = Level(self.cfg)
        self.game.level = lvl
        self.game.player.pos = lvl.get_starting_pos()

    def event(self, e):
        b = check_button_click(self, e, "level")

        if b and len(b):
            self.pressed(b)

    def draw(self, surface):
        bg = self.cfg.assets["level"]["background"]
        surface.blit(bg, (0, 0))

        for p in self.previews:
            surface.blit(p["image"], p["pos"])


def make_button(obj, key, which):
    x, y, w, h = obj.cfg.buttons[which][key]
    rect = pygame.Rect(x, y, w - x, h - y)

    return rect


def check_button_click(obj, e, which):
    if e.type != pygame.MOUSEBUTTONDOWN:
        return None

    pos = pygame.mouse.get_pos()

    # Check every button for collision with current mouse pos
    for i, b in enumerate(obj.buttons):
        if b.collidepoint(pos):
            return list(obj.cfg.buttons[which])[i]

    return None
