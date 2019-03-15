import pygame

Hero_rect = pygame.Rect(100, 500, 120, 125)
print("英雄的原点：(%d, %d)" % (Hero_rect.x, Hero_rect.y))
print("英雄的尺寸：(%d, %d)" % (Hero_rect.width, Hero_rect.height))
print("%d %d" % Hero_rect.size)