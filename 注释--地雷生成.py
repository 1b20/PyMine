import sys
import random


class MineAlgo:
    """
    扫雷游戏地雷生成算法类
    职责：负责生成扫雷游戏的地图数据，包括随机布置地雷和计算周围地雷数量
    设计意图：为扫雷游戏提供核心的地图生成功能，确保第一次点击安全
    使用方法：实例化时传入地雷数量和要保护的安全位置，即可生成完整的地图数据
    """

    # 10x10的雷区地图，0表示初始无雷状态
    mine = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # 类级别标记，表示地雷布局是否已完成
    fMineSet = False

    def setMine(self, mineNum, outRow, outCol):
        """
        随机布置指定数量的地雷到10x10网格中
        功能：使用随机算法在排除安全位置后布置地雷
        参数含义：
            mineNum - 要布置的地雷总数
            outRow - 要保护的行坐标（玩家第一次点击位置）
            outCol - 要保护的列坐标（玩家第一次点击位置）
        返回值说明：无，直接修改类的mine属性
        """
        row = 0
        col = 0
        i = 0

        # 重置雷区地图为全零状态，确保每次调用都是全新的开始
        self.mine = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        # 初始化随机数生成器，确保每次运行结果不同
        random.seed()

        # 地雷布置循环：使用拒绝采样算法直到布置完所有地雷
        while i < mineNum:
            # 生成0-9范围内的随机行列坐标
            row = random.randint(0, 9)
            col = random.randint(0, 9)

            # 关键条件判断：位置未被占用且不是受保护的安全位置
            if (self.mine[row][col] != 9 and (row != outRow or col != outCol)):
                # 在地图相应位置标记地雷（用数字9表示）
                self.mine[row][col] = 9
                i = i + 1  # 成功布置一个地雷，计数器增加

    def setMineNum(self):
        """
        计算每个非地雷格子周围的地雷数量
        功能：遍历整个地图，为每个非地雷格子计算相邻地雷数
        业务逻辑：扫雷游戏核心算法，根据地雷位置推导出数字提示
        """
        # 双重循环遍历10x10网格的每个单元格
        for i in range(0, 10):
            for j in range(0, 10):
                # 只处理非地雷格子（地雷用9标记）
                if (self.mine[i][j] != 9):
                    # 调用辅助方法计算周围8个方向的地雷总数
                    summ = self.checkMineNum(i, j)
                    # 将计算结果存入当前格子
                    self.mine[i][j] = summ
        # 设置完成标记，表明地雷布局和数字计算都已结束
        MineAlgo.fMineSet = True

    def checkMineNum(self, ii, jj):
        """
        计算指定格子周围3x3区域内的地雷数量
        功能：统计一个格子所有相邻位置的地雷个数
        参数含义：
            ii - 当前格子的行索引
            jj - 当前格子的列索引
        返回值说明：周围地雷数量（0-8）
        算法逻辑：通过边界检查确保不越界，然后遍历周围8格
        """
        count = 0
        top = 0
        bottom = 0
        left = 0
        right = 0

        # 计算上边界：确保不超出网格上边界（第0行）
        if ii - 1 > 0:
            top = ii - 1
        else:
            top = 0

        # 计算下边界：确保不超出网格下边界（第9行）
        if ii + 1 < 10:
            bottom = ii + 1
        else:
            bottom = 9

        # 计算左边界：确保不超出网格左边界（第0列）
        if jj - 1 > 0:
            left = jj - 1
        else:
            left = 0

        # 计算右边界：确保不超出网格右边界（第9列）
        if jj + 1 < 10:
            right = jj + 1
        else:
            right = 9

        # 遍历以(ii,jj)为中心的3x3区域（包括自身）
        for i in range(top, bottom + 1):
            for j in range(left, right + 1):
                # 检查当前格子是否为地雷（值为9）
                if self.mine[i][j] == 9:
                    count = count + 1  # 发现地雷，计数器增加
        return count  # 返回周围地雷总数

    def printMine(self):
        """
        以文本形式打印完整的雷区地图
        功能：将10x10的数字矩阵格式化输出到控制台
        输出格式：每行10个数字，数字间用空格分隔
        """
        # 遍历每一行
        for i in range(0, 10):
            # 遍历当前行的每一列
            for j in range(0, 10):
                # 打印当前格子的值，保持对齐
                print("%d " % self.mine[i][j], end="")
            # 每行结束后换行
            print('\n', end="")

    def __init__(self, mineNum, outRow, outCol):
        """
        类构造函数：初始化地雷地图
        功能：创建实例时自动完成地雷布置和数字计算
        参数含义：
            mineNum - 地雷数量
            outRow - 受保护的行坐标
            outCol - 受保护的列坐标
        执行流程：先布置地雷，再计算数字，完成地图生成
        """
        # 第一步：随机布置地雷
        self.setMine(mineNum, outRow, outCol)
        # 第二步：计算每个格子的周围地雷数
        self.setMineNum()


if __name__ == "__main__":
    # 从命令行参数获取输入：地雷数量、安全位置行和列
    # sys.argv[1]：地雷数量，sys.argv[2]：受保护行，sys.argv[3]：受保护列
    mine = MineAlgo(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    # 打印生成的地图数据

    mine.printMine()
