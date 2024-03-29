import pygame

pygame.init()

# 创建游戏的窗口
screen = pygame.display.set_mode((480, 700))

#绘制背景图片
# 1> 加载图像数据
bg = pygame.image.load("./images/background.png")
# 2> 绘制图像
screen.blit(bg,(0,0))
# 3> update 更新屏幕显示
# pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(150,500))

# 统一调用一次
pygame.display.update()



#创建时钟对象
clock = pygame.time.Clock()
# 游戏循环 ->意味着游戏的正式开始
i = 0
while True:
    # 循环体内部执行的频率
    clock.tick(60)
    print(i)
    i += 1
pygame.quit()