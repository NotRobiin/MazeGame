from src.config import Config
from src.game import Game
from src.menu import MainMenu


def main() -> None:
    # Make all requirements
    cfg = Config()
    game = Game(cfg)
    menu = MainMenu(game, cfg)

    # Start the game
    game.loop()


if __name__ == "__main__":
    main()
