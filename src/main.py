from config import Config
from game import Game
from level import Level


def main() -> None:
    # Make all requirements
    cfg = Config()
    game = Game(cfg)
    lvl = Level(cfg)

    # Setup all requirements
    game.setup(lvl)

    # Start the game
    game.loop()


if __name__ == "__main__":
    main()
