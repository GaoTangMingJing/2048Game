# coding=utf-8

import sys
import os
import random
import itertools

class Game:
    grid = []
    controls = ['w', 'a', 's', 'd']

    #判断下标合法性
    def inRange(self, i, j):
        return i>=0 and i <=3 and j>=0 and j <=3

    #得到下一个非零位置（只判断up的情况）
    #[r, c, value]
    def nextNonZero(self, i, j):
        nextI, nextJ = i+1, j

        if not self.inRange(nextI, nextJ):
            return None

        while(self.inRange(nextI, nextJ)):
            value = self.grid[nextI][nextJ]
            if(value != 0):
                return [nextI, nextJ, value]

            nextI, nextJ = nextI+1, nextJ

    # 从i，j出发，依次处理某行或某列的所有数据（因为针对up，所以处理一列）
    def delOneCol(self, i, j):
        if(not self.inRange(i, j)):
            return

        nextCell = self.nextNonZero(i, j)
        if(not nextCell):
            return

        nextI, nextJ, nextValue = nextCell

        if(self.grid[i][j] == 0):
            self.grid[i][j] = nextValue
            self.grid[nextI][nextJ] = 0
            self.delOneCol(i, j)
        elif(self.grid[i][j] == nextValue):
            self.grid[i][j] *= 2
            self.grid[nextI][nextJ] = 0

        nextI += 1
        self.delOneCol(nextI, nextJ)


    def up(self):
        for j in range(4):
            self.delOneCol(0, j)

    def down(self):
        pass

    def left(self):
        pass

    def right(self):
        pass

    def random_number(self):
        number = random.choice([2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4])
        x, y = random.choice([(x, y) for x, y in itertools.product([0, 1, 2, 3], [0, 1, 2, 3]) if self.grid[x][y] == 0])
        self.grid[x][y] = number

    def print_grid(self):
        os.system('cls')
        print('-' * 21)
        for row in self.grid:
            print('|{}|'.format('|'.join([str(col or ' ').center(4) for col in row])))
            print('-' * 21)

    # def logic(self, control):
    #     dict = {'w': self.up, 's': self.down, 'a': self.left, 'd': self.right}
    #     grid_deepcopy = [[col for col in row] for row in self.grid]
    #     new_grid = dict[control](grid_deepcopy)
    #     # grid = {'w': up, 's': down, 'a': left, 'd': right}[control]([[col for col in row] for row in self.grid])
    #     if new_grid != self.grid:
    #         del self.grid[:]
    #         self.grid.extend(new_grid)
    #         if [n for n in itertools.chain(*self.grid) if n >= 2048]:
    #             return 1, "You Win!"
    #         self.random_number()
    #         self.random_number()
    #     else:
    #         if not [1 for g in [f(new_grid) for f in dict.values()] if g != self.grid]:
    #             return -1, "You Lose"
    #     return 0, "" # 1, "You Win!"; -1, "You Lose!"

    def logic(self, control):
        dict = {'w': self.up, 's': self.down, 'a': self.left, 'd': self.right}
        grid_deepcopy = [[col for col in row] for row in self.grid]
        dict[control]()
        # grid = {'w': up, 's': down, 'a': left, 'd': right}[control]([[col for col in row] for row in self.grid])
        if self.grid != grid_deepcopy:
            if [n for n in itertools.chain(*self.grid) if n >= 2048]:
                return 1, "You Win!"
            self.random_number()
            self.random_number()
        else:
            if not [1 for g in [f() for f in dict.values()] if g != self.grid]:
                return -1, "You Lose"
        return 0, "" # 1, "You Win!"; -1, "You Lose!"

    def main_loop(self):
        # 棋盘初始化
        self.grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

        # 生成两个随机数
        self.random_number()
        self.random_number()

        while True:
            # 打印棋盘
            self.print_grid()

            # 根据用户输入移动棋盘
            control = input('请输入方向(w, a, s, d): ')
            if control in self.controls:
                status, info = self.logic(control)
                if status != 0:
                    print(info)
                    if input('是否继续游戏(y/n): ').lower() == 'y':
                        break
                    else:
                        sys.exit(0)

        self.main_loop()

if __name__ == '__main__':
    game = Game()
    game.main_loop()