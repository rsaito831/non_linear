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
        # return self.a * x - self.c * x * y
        return y

    def func2(self, t, x, y):  # 関数(2)
        # return -self.b * y + self.c * x * y
        # return -x
        return - x + self.ep *\
            (self.b * math.cos(t) + self.a * x - self.zeta * y - self.c * x**3)


class Runge_kutta(Function):
    def __init__(self, ep, zeta, a, b, c, t_0, x_0, y_0, h, times):
        super().__init__(ep, zeta, a, b, c, t_0, x_0, y_0)
        self.h = h
        self.times = times

    def runge_kutta(self):  # Runge Kutta本体

        f1 = open("sim_result.txt", "w")
        f2 = open("poin_result.txt", "w")

#        t = self.t_0
        t = [i / 100 for i in range(0, self.times)]
        x = self.x_0
        y = self.y_0

        cnt_t = -1

#        f1.write(str(t) + " " + str(x) + " " + str(y) + "\n")
        f1.write(str(t[0]) + " " + str(x) + " " + str(y) + "\n")

        for i in range(self.times):

            k1_x = self.h * super().func1(t[i], x, y)

            k1_y = self.h * super(). func2(t[i], x, y)

            k2_x = self.h * super().func1(t[i] + self.h / 2,
                                          x + k1_x / 2,
                                          y + k1_y / 2)

            k2_y = self.h * super().func2(t[i] + self.h / 2,
                                          x + k1_x / 2,
                                          y + k1_y / 2)

            k3_x = self.h * super().func1(t[i] + self.h / 2,
                                          x + k2_x / 2,
                                          y + k2_y / 2)

            k3_y = self.h * super().func2(t[i] + self.h / 2,
                                          x + k2_x / 2,
                                          y + k2_y / 2)

            k4_x = self.h * super().func1(t[i] + self.h,
                                          x + k3_x,
                                          y + k3_y)

            k4_y = self.h * super().func2(t[i] + self.h,
                                          x + k3_x,
                                          y + k3_y)

            cnt_t += 1
            if cnt_t % 628 == 0:
                cnt_t = 0
                f2.write(str(t[i]) + " " + str(x) + " " + str(y) + "\n")

            # t = t + self.h
            x = x + 1 / 6 * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)
            y = y + 1 / 6 * (k1_y + 2 * k2_y + 2 * k3_y + k4_y)

            # f1.write(str(t) + " " + str(x) + " " + str(y) + "\n")
            f1.write(str(t[i]) + " " + str(x) + " " + str(y) + "\n")

        f1.close()
        f2.close()


def main():
    times = 50000  # 試行回数
    h = 0.01  # 刻み幅

    t = 0
    x_0 = 1  # x0
    y_0 = 0  # y0
    ep = 0.01
    a = 1
    b = 0.3
    c = 1
    zeta = 0.1

    rk = Runge_kutta(ep, zeta, a, b, c, t, x_0, y_0, h, times)
    rk.runge_kutta()


if __name__ == '__main__':
    main()
