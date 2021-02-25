from pygame import Rect, Surface, SRCALPHA, MOUSEBUTTONDOWN, mouse
from pygame.draw import rect
from pygame.font import SysFont


class Popup:
    def __init__(self, **options):
        self.which = options["which"] or "UNKNOWN_TYPE"
        self.title = options["title"] or ""
        self.buttons_options = options["buttons"] or [
            {"label": "???", "function": None}
        ]
        self.data = {"pos": options["pos"]}
        self.bg = None
        self.popup = None
        self.buttons = []

    def event(self, e):
        if e.type != MOUSEBUTTONDOWN:
            return

        pos = mouse.get_pos()

        for i, b in enumerate(self.buttons):
            obj = b["obj"]

            if obj.collidepoint(pos):
                f = b["options"]["function"]
                f(self.data)
                break

    def draw_background(self, surface):
        BG_COLOR = (180, 180, 180, 200)

        ws_x, ws_y = surface.get_size()

        # Fill the screen with light-grey, so the popup
        # appears as it's on top of the game elements
        bg = Rect(0, 0, ws_x, ws_y)
        s = Surface(bg.size, SRCALPHA)
        rect(s, BG_COLOR, s.get_rect())
        surface.blit(s, bg)

        return bg

    def draw_popup(self, surface):
        SCALE = (0.65, 0.40)
        POPUP_COLOR = (230, 230, 230)

        ws_x, ws_y = surface.get_size()

        # Prepare popup rectangle.
        # We change the popup-rectangle size to 65% of original width,
        # and 40% of original height, so it's not drawn from
        # left top corner, but with a bit of 'padding'
        x = ws_x * (1.0 - SCALE[0]) / 2
        y = ws_y * (1.0 - SCALE[1]) / 2
        w = ws_x - x * 2
        h = ws_y - y * 2

        popup = rect(surface, POPUP_COLOR, (x, y, w, h))

        # Finally, draw the popup
        rect(surface, POPUP_COLOR, popup)

        return popup

    def draw_title(self, surface):
        FONT_COLOR = (0, 0, 0)
        FONT = SysFont("Arial", 30)

        text = FONT.render(self.title, True, FONT_COLOR)
        h = text.get_rect().height
        mt = self.popup.midtop
        center = (mt[0], mt[1] + h)
        pos = text.get_rect(center=center)

        surface.blit(text, pos)

    def draw_buttons(self, surface):
        BUTTON_COLOR = (150, 20, 20)
        FONT_COLOR = (0, 0, 0)
        FONT = SysFont("Arial", 30)

        for i, b in enumerate(self.buttons):
            button = b["obj"]
            rect(surface, BUTTON_COLOR, button)

            text = FONT.render(self.buttons_options[i]["label"], True, FONT_COLOR)
            pos = text.get_rect(center=button.center)

            surface.blit(text, pos)

    def make_buttons(self):
        X_OFFSET = 10
        Y_OFFSET_MULTIPLIER = 0.2
        BOTTOM_OFFSET = 10

        amount = len(self.buttons_options)
        popup_size = self.popup.size
        p_x, p_y = self.popup.topleft
        x_off = popup_size[0] / amount - X_OFFSET
        x = X_OFFSET
        y = popup_size[1] - popup_size[1] * Y_OFFSET_MULTIPLIER
        h = popup_size[1] - y - BOTTOM_OFFSET

        for i in range(amount):
            button = Rect(p_x + x, p_y + y, x_off - X_OFFSET, h)

            self.buttons.append(
                {"obj": button, "options": self.buttons_options[i],}
            )

            x += x_off + X_OFFSET

    def draw(self, surface):
        self.bg = self.draw_background(surface)
        self.popup = self.draw_popup(surface)
        self.draw_title(surface)

        if len(self.buttons):
            self.draw_buttons(surface)
        else:
            self.make_buttons()
