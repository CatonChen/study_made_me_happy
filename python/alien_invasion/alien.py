import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """单个外星人的类"""

    def __init__(self, ai_game):
        # 初始化并设置起始位置
        super().__init__()
        self.screen = ai_game.screen
        # 外星人图片和rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 外星人最初都在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 保存外人的水平位置
        self.x = float(self.rect.x)
