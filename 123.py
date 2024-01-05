import pygame
import sys

# 初始化 Pygame
pygame.init()

# 定義顏色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 設置視窗大小
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('我的遊戲')

# 主遊戲迴圈
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 在這裡可以加入遊戲的邏輯和繪製的程式碼

    # 清除畫面
    screen.fill(WHITE)

    # 在這裡繪製遊戲元素或角色

    # 更新畫面
    pygame.display.flip()

# 退出 Pygame
pygame.quit()
sys.exit()
