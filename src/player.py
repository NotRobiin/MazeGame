from pygame import K_LEFT, K_RIGHT, K_UP, K_DOWN


class Player:
    def __init__(self, config, game):
        self.cfg = config
        self.game = game
        self.pos = None
        self.image = None
        self.gender = bool  # Hehe

    def set_gender(self, gender: str) -> None:
        self.gender = gender
        self.image = self.cfg.assets["player"][gender]

    def button_mine(self, data):
        x, y = data["pos"]
        self.game.level.update_block(x, y, " ")
        self.game.set_popup(False)

    def button_deny(self):
        self.game.set_popup(False)

    def move(self, key):
        keys_to_pos = {
            K_LEFT: (-1, 0),
            K_RIGHT: (1, 0),
            K_UP: (0, -1),
            K_DOWN: (0, 1),
        }

        # Make sure we move by entire blocks
        step = keys_to_pos[key]
        bs = self.cfg.block_size
        x = self.pos[0] + step[0] * bs
        y = self.pos[1] + step[1] * bs

        block = self.game.level.get_block(x, y)

        # We bumped into a wall
        if block in ["x"]:
            return

        # We bumped into a dirt
        if block in ["d"]:
            self.game.set_popup(
                True,
                which="dirt",
                title="Do you wish to mine the dirt?",
                buttons=[
                    {"label": "Mine it!", "function": self.button_mine,},
                    {"label": "Leave it!", "function": self.button_deny},
                ],
                pos=(x, y),
            )
            return

        # We bumped into a rock
        if block in ["r"]:
            self.game.set_popup(
                True,
                which="rock",
                title="Do you wish to mine the rock?",
                buttons=[
                    {"label": "Mine it!", "function": self.button_mine,},
                    {"label": "Leave it!", "function": self.button_deny},
                ],
                pos=(x, y),
            )
            return

        self.pos = (x, y)

    def draw(self, surface) -> None:
        surface.blit(self.image, self.pos)
