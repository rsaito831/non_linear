# -*- coding: utf-8 -*-
import math


class Function:
    def __init__(self, ep, zeta, a, b, c, t_0, x_0, y_0):
        self.ep = ep
        self.zeta = zeta
        self.a = a
        self.b = b
        self.c = c
        self.t_0 = t_0
        self.x_0 = x_0
        self.y_0 = y_0

    def func1(self, t, x, y):  # 関数(1)
        return -self.zeta * x - (self.a - 3 / 4 * self.c * (x**2 + y**2)) * y

    def func2(self, t, x, y):  # 関数(2)
        return (self.a - 3 / 4 * self.c * (x**2 + y**2)) * x - self.zeta * y + self.b


class Runge_kutta(Function):
    def __init__(self, ep, zeta, a, b, c, t_0, x_0, y_0, h, times):
        super().__init__(ep, zeta, a, b, c, t_0, x_0, y_0)
        self.h = h
        self.times = times

    def runge_kutta(self):  # Runge Kutta本体

        t = self.t_0
        x = self.x_0
        y = self.y_0

        print(t, " ", x, " ", y)

        for i in range(self.times):

            k1_x = self.h * super().func1(t, x, y)

            k1_y = self.h * super(). func2(t, x, y)

            k2_x = self.h * super().func1(t + self.h / 2,
                                          x + k1_x / 2,
                                          y + k1_y / 2)

            k2_y = self.h * super().func2(t + self.h / 2,
                                          x + k1_x / 2,
                                          y + k1_y / 2)

            k3_x = self.h * super().func1(t + self.h / 2,
                                          x + k2_x / 2,
                                          y + k2_y / 2)

            k3_y = self.h * super().func2(t + self.h / 2,
                                          x + k2_x / 2,
                                          y + k2_y / 2)

            k4_x = self.h * super().func1(t + self.h,
                                          x + k3_x,
                                          y + k3_y)

            k4_y = self.h * super().func2(t + self.h,
                                          x + k3_x,
                                          y + k3_y)

            t = t + self.h
            x = x + 1 / 6 * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)
            y = y + 1 / 6 * (k1_y + 2 * k2_y + 2 * k3_y + k4_y)

            print(t, " ", x, " ", y)

            """ print(round(t[i], 3),
                  " ",
                  round(x[i], 3),
                  " ",
                  round(y[i], 3))
            """


def main():
    times = 50000  # 試行回数
    h = 0.01  # 刻み幅

    t = 0
    x_0 = 1  # x0
    y_0 = -2  # y0
    ep = 0.01
    a = 1
    b = 0.3
    c = 1
    zeta = 0.1

    rk = Runge_kutta(ep, zeta, a, b, c, t, x_0, y_0, h, times)
    rk.runge_kutta()


if __name__ == '__main__':
    main()
