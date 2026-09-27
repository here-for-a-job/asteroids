import pygame
from constants import TEXT_SIZE, POINTBOARD_EDGE_LENGTH, POINTBOARD_TEXT_GAP_LENGTH, POINTBOARD_BORDER_THICKNESS

class Pointboard(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, name:str, amount:int, x:float, y:float):
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__(*self.containers)

        self.name:str = name
        self.current_amount:int = amount
        self.x:float = x
        self.y:float = y

        pygame.font.init()
        self.font = pygame.font.SysFont(None, TEXT_SIZE)

        self.surface_name = self.font.render(self.name + ":", True, (125, 125, 125))
        self.surface_name_pos = (self.x + POINTBOARD_EDGE_LENGTH, self.y + POINTBOARD_EDGE_LENGTH)
        self.surface_amount = self.font.render(str(self.current_amount), True, (125, 125, 125))
        self.surface_amount_pos = (self.x + POINTBOARD_EDGE_LENGTH, self.y + POINTBOARD_EDGE_LENGTH + POINTBOARD_TEXT_GAP_LENGTH + self.surface_name.get_height())

        self.update_surface()

    def add_amount(self, amount:int):
        self.current_amount += amount
        self.update_surface()

    def update_surface(self):
        self.surface_amount = self.font.render(str(self.current_amount), True, (125, 125, 125))
        dim_surface_name = self.surface_name.get_size()
        dim_surface_amount = self.surface_amount.get_size()
        min_width = max(dim_surface_amount[0], dim_surface_name[0])
        surface_width = min_width + 2 * POINTBOARD_EDGE_LENGTH
        surface_heigth = dim_surface_amount[1] + dim_surface_name[1] + POINTBOARD_TEXT_GAP_LENGTH + 2 * POINTBOARD_EDGE_LENGTH
        self.surface_border = pygame.Rect(self.x, self.y, surface_width, surface_heigth)

    def draw(self, screen:pygame.Surface):
        pygame.draw.rect(screen, (125, 125, 125), self.surface_border, width=POINTBOARD_BORDER_THICKNESS)
        screen.blit(self.surface_name, self.surface_name_pos)
        screen.blit(self.surface_amount, self.surface_amount_pos)
