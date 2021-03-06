# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

__author__ = 'Evan'


def draw_tendency_chart():
    """
    绘制折线图
    """
    # 处理中文乱码
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 提高画质
    plt.figure(figsize=(10, 5), dpi=130)
    plt.subplot(111)

    plt.xlabel('天数', size=12)  # 添加X轴标签
    plt.ylabel('数值', size=12)  # 添加Y轴标签
    plt.ylim([1, 50])  # 设置Y轴的刻度范围

    case_1_x = ['2020/5/1', '2020/5/2', '2020/5/3', '2020/5/4']
    case_1_y = [10, 20, 30, 40]

    case_2_x = ['2020/5/1', '2020/5/2', '2020/5/3', '2020/5/4']
    case_2_y = [15, 25, 35, 45]

    case_3_x = ['2020/5/1', '2020/5/2', '2020/5/3', '2020/5/4']
    case_3_y = [18, 28, 38, 48]

    # 画点
    for i in range(0, len(case_1_x)):
        plt.scatter(case_1_x[i], case_1_y[i], marker='D', s=30, color="#1E90FF")
    for i in range(0, len(case_2_x)):
        plt.scatter(case_2_x[i], case_2_y[i], marker='D', s=30, color="#FFA500")
    for i in range(0, len(case_3_x)):
        plt.scatter(case_3_x[i], case_3_y[i], marker='D', s=30, color="g")

    # 画线
    plt.plot(case_1_x, case_1_y, linewidth=2, label='case_1', color="#1E90FF")
    plt.plot(case_2_x, case_2_y, linewidth=2, label='case_2', color='#FFA500')
    plt.plot(case_3_x, case_3_y, linewidth=2, label='case_3', color='g')

    # 显示曲线标注
    plt.legend()  # 默认位置
    # plt.legend(loc="right")  # 居右
    # plt.legend(loc="row right")  # 居右下
    plt.grid(linewidth=1.0, linestyle='--')
    plt.show()
    # plt.savefig('tendency_chart.jpg', bbox_inches='tight')  # 保存图片


if __name__ == '__main__':
    draw_tendency_chart()
