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
        return -self.ep / 2 *\
            (self.zeta * x + (self.a - 3 / 4 * self.c * (x**2 + y**2)) * y)

    def func2(self, t, x, y):  # 関数(2)
        return self.ep / 2 * \
            ((self.a - 3 / 4 * self.c * (x**2 + y**2)) * x
             - self.zeta * y + self.b)


class Runge_kutta(Function):
    def __init__(self, ep, zeta, a, b, c, t_0, x_0, y_0, h, times):
        super().__init__(ep, zeta, a, b, c, t_0, x_0, y_0)
        self.h = h
        self.times = times

    def runge_kutta(self):  # Runge Kutta本体

        t = self.t_0
        x = self.x_0
        y = self.y_0
        t_save = [self.t_0]
        x_save = [self.x_0]
        y_save = [self.y_0]

        cnt_t = -1

        f1 = open("kadai3_result.txt", "w")
        f2 = open("poin_kadai3.txt", "w")

        f1.write(str(t) + " " + str(x) + " " + str(y) + "\n")

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

            cnt_t += 1
            if cnt_t % 628 == 0:
                cnt_t = 0
                f2.write(str(t) + " " + str(x) + " " + str(y) + "\n")

            t = t + self.h
            x = x + 1 / 6 * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)
            y = y + 1 / 6 * (k1_y + 2 * k2_y + 2 * k3_y + k4_y)

            t_save.append(t)
            x_save.append(x)
            y_save.append(y)
            f1.write(str(t) + " " + str(x) + " " + str(y) + "\n")

        f1.close()
        f2.close()

        return t_save, x_save, y_save

    def para_change(self, t=[], u=[], v=[]):

        f = open("para_change.txt", "w")

        for i in range(self.times):
            x = u[i] * math.cos(t[i]) + v[i] * math.sin(t[i])
            y = -u[i] * math.sin(t[i]) + v[i] * math.cos(t[i])

            f.write(str(t[i]) + " " + str(x) + " " + str(y) + "\n")

        f.close()


def main():
    times = 50000  # 試行回数
    h = 2 * math.pi / 628  # 刻み幅

    t_0 = 0
    x_0 = 1  # x0
    y_0 = 0  # y0
    ep = 5
    a = 1
    b = 0.3
    c = 1
    zeta = 0.1

    rk = Runge_kutta(ep, zeta, a, b, c, t_0, x_0, y_0, h, times)
    t, u, v = rk.runge_kutta()
    rk.para_change(t, u, v)


if __name__ == '__main__':
    main()
