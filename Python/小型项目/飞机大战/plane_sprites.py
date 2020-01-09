# 这个模块放一些常用的工具和基础类和精灵类
# 在其他模块调用
import random

import pygame

# 设置游戏屏幕大小 这是一个常量
SCREEN_RECT = pygame.Rect(0, 0, 580, 700)
# 敌机的定时器事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

# 定制一个精灵类，需要继承pygame提供的精灵类
# 需要定义的属性有：
# image图片
# rect坐标
# speed速度

# 接下来开始写敌机方面的内容 产生敌机
# 先定义一个事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 我们还可以定义一个事件常量(发射子弹)
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, new_image, new_speed=1):
        super().__init__()
        # 图片
        self.image = pygame.image.load(new_image)
        # 速度
        self.speed = new_speed
        # 位置 获取图片的宽和高 get_rect()(0,0,宽，高)
        self.rect = self.image.get_rect()
        # 精灵移动的速度 包括英雄精灵 背景精灵 敌机精灵 子弹精灵
        self.speed = new_speed

    def update(self):
        # 默认垂直方向移动 y轴控制垂直方向
        self.rect.y += self.speed
        # self.rect.x += 1


# 以上是游戏的基础类，接下来设置背景类
# 明确背景类继承自游戏的精灵类
class Background(GameSprite):
    def __init__(self, is_alt=False):
        # is_alt判断是否为另一张图像
        # False表示第一张图像
        # Ture表示另外一张图像
        # 两张图像交替循环
        # 传图片
        super().__init__("D:\\work_data\py\\小型项目\\飞机大战\\1test.png")
        if is_alt:
            # 如果是第二张图片 初始位置为-self.rect.height
            self.rect.y = -self.rect.height

    # def __init__(self,new_image):
    #   super().init__(new_image)
    def update(self):
        # 调用父类方法
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


# 敌机出场
class Enemy(GameSprite):
    # 敌机精灵
    def __init__(self):
        # 1 调用父类方法 创建敌机精灵 并且指定敌机图像
        super().__init__("D:\\work_data\py\\小型项目\\飞机大战\\1test.png")

        # 2 设置敌机的随机初始速度1~3
        self.speed = random.randint(2, 6)
        # 3 设置敌机的随机初始位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 1 调用父类方法 让敌机在垂直方向运动
        super().update()

        # 2 判断是否飞出屏幕 如果是 需要将敌机从精灵组删除
        if self.rect.y >= SCREEN_RECT.height:
            # print("敌机飞出屏幕")
            # 将精灵从精灵组中删除
            self.kill()


# 英雄出场
class Hero(GameSprite):
    def __init__(self):
        super().__init__("D:\\work_data\py\\小型项目\\飞机大战\\1test.png", 0)
        self.bullet = pygame.sprite.Group()
        # 设置初始位置
        self.rect.center = SCREEN_RECT.center
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.move = False

    def update(self):
        # super().update()
        if not self.move:
            self.rect.x += self.speed
        else:
            self.rect.y += self.speed

        # self.rect.y += self.speed
        # 飞机飞出屏幕
        if self.rect.bottom <= 0:
            self.rect.y = self.rect.bottom + SCREEN_RECT.height
        elif self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

        if self.rect.right <= 0:
            self.rect.x = self.rect.right + SCREEN_RECT.width
        elif self.rect.x >= SCREEN_RECT.width:
            self.rect.x = -self.rect.width

    def fire(self):
        # print("发射子弹")

        for i in (1, 2, 3):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.center = self.rect.center
            self.bullet.add(bullet)


# 子弹精灵
class Bullet(GameSprite):

    def __init__(self):
        super().__init__("D:\\work_data\py\\小型项目\\飞机大战\\1test.png", -5)

    def update(self):
        super().update()

        # 判断是否超出屏幕 如果是 从精灵组删除
        if self.rect.bottom < 0:
            self.kill()
