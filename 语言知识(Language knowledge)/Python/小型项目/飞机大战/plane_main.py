from 小型项目.飞机大战.plane_sprites import *

# 初始化

pygame.mixer.init()

pygame.mixer.music.load("D:\\work_data\\py\\小型项目\\飞机大战\\music.mp3")
# 播放
pygame.mixer.music.play(loops=-1)

HERO_FIRE_EVENT = pygame.USEREVENT + 1


class PlaneGame(object):
    def __init__(self):
        # print("游戏初始化")

        # 1.创建游戏窗口pygame.display.set_mode
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏时钟pygame.time.Clock()
        self.clock = pygame.time.Clock()
        # 3.创建精灵和精灵组内容较多 故封装成一个方法
        # 调用创建精灵的方法
        self.__creat_sprites()
        # 以上属于游戏初始化时候的设置
        # 4.设置定时器 每隔多少秒创建一个敌机
        # pygame.time.set_timer相当于写了一个定时器 每隔一秒调用一次
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 500)
        # 再写一个定时器 发射子弹
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)
        # 上面这一步定义了系统每隔0.5秒 调用一次pygame事件
        # 下面去事件监听方法里监听事件

    def star_game(self):
        while True:
            # 1 设置帧率
            self.clock.tick(200)
            # 2 事件监听 主要监听我们鼠标键盘的一些事件
            self.__event_handler()

            # 3 碰撞检测
            self.__check_collide()
            # 4 更新精灵和精灵组
            self.__update_sprites()
            # 5 更新显示
            pygame.display.update()
            # 以上都是要实时监测的，so写在循环里
            # 每1\60秒就会调用一次

    # 创建精灵和精灵组
    def __creat_sprites(self):
        bg1 = Background()
        # Ture 就表示是第二张图片
        bg2 = Background(True)

        # 英雄
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 敌机组
        self.enemy_group = pygame.sprite.Group()

    # 事件监听
    def __event_handler(self):

        for event in pygame.event.get():
            # 如果某个按键按下 对应的值应该会是
            keys_pressed = pygame.key.get_pressed()
            # 控制飞机移动
            if keys_pressed[276]:
                self.hero.move = False
                self.hero.speed = -9
            elif keys_pressed[275]:
                self.hero.move = False
                self.hero.speed = 9
            elif keys_pressed[273]:
                self.hero.move = True
                self.hero.speed = -9
            elif keys_pressed[274]:
                self.hero.move = True
                self.hero.speed = 9
            else:
                self.hero.speed = 0

            if event.type == pygame.QUIT:
                self.__game_over()

            elif event.type == CREATE_ENEMY_EVENT:
                # print("新的敌机产生")

                self.enemy_group.add(Enemy())

            # 发射子弹
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

    # 更新精灵和精灵组
    def __update_sprites(self):

        for x in [self.back_group, self.enemy_group, self.hero_group, self.hero.bullet]:
            x.update()
            x.draw(self.screen)

    def __check_collide(self):
        # 碰撞检测
        # 1.子弹摧毁飞机
        # 第一个参数和第二个参数是要参与碰撞检测的精灵
        # 第三个参数为Ture的时候 就是当碰撞的时候被碰撞的精灵从精灵组移除
        pygame.sprite.groupcollide(self.enemy_group, self.hero.bullet, True, True)  # 子弹
        # 2.敌机撞毁飞机
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        # 判断列表时候有内容
        if len(enemies) > 0:
            # 让英雄牺牲
            self.hero.kill()

            # 结束游戏
            PlaneGame.__game_over()

    @staticmethod
    def __game_over():
        print("游戏结束")
        # 这是pygame提供的卸载模块功能
        pygame.quit()
        # 这是pygame本身提供的退出脚本的功能
        exit()
        # 需要先卸载pygame模块 然后退出脚本


if __name__ == "__main__":
    game = PlaneGame()
    game.star_game()
