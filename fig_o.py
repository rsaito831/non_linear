# -*- coding: utf-8 -*-

import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


class Data_read:
    def __init__(self, n=2, argvs=[]):
        self.n = n
        self.argvs = argvs

    def reading(self):
        data = []
        t = []
        x = []
        y = []

        t_poin = []
        x_poin = []
        y_poin = []

        f1 = open("{}".format(self.argvs[1]))

        lines = f1.readlines()
        for l in lines:
            data = l.split()

            t.append(float(data[0]))
            x.append(float(data[1]))
            y.append(float(data[2]))
        f1.close()

        if self.n == 3:
            f2 = open("{}".format(self.argvs[2]))
            lines = f2.readlines()
            for l in lines:
                data = l.split()

                t_poin.append(float(data[0]))
                x_poin.append(float(data[1]))
                y_poin.append(float(data[2]))

            f2.close()

        if self.n == 1:
            return t, x, y
        else:
            return t, x, y, t_poin, x_poin, y_poin


class Fig_output:
    def __init__(self, t, x, y, t_poin, x_poin, y_poin):
        self.t = t
        self.x = x
        self.y = y
        self.t_poin = t_poin
        self.x_poin = x_poin
        self.y_poin = y_poin

    def xy_t_put(self):
        plt.xlabel("Time[s]")
        plt.ylabel("The number of individuals x,y")
#       plt.xlim([0, max(self.t)])
#       plt.ylim([0, max(max(self.x), max(self.y))])
        plt.plot(self.t, self.x, label="x-t")
        plt.plot(self.t, self.y, label="y-t")
        plt.legend()
        plt.show()

    def x_y_out(self):
        plt.xlabel("x")
        plt.ylabel("Y")
#       plt.xlim([300, max(self.x)])
#       plt.ylim([300, max(self.y)])
        plt.plot(self.x, self.y, linewidth=0.5)
        plt.plot(self.x_poin, self.y_poin, "r.")
        plt.legend()
        plt.show()

    def r3_out(self):
        fig = plt.figure()
        ax = Axes3D(fig)

        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")

        x = np.array(self.x)
        y = np.array(self.y)
        z = np.array(self.t)
        ax.plot(x, y, z)
        plt.show()


def main():

    n = len(sys.argv)
    rd = Data_read(n, sys.argv)

    t, x, y, t_poin, x_poin, y_poin = rd.reading()

    fo = Fig_output(t, x, y, t_poin, x_poin, y_poin)
    fo.xy_t_put()
    fo.x_y_out()
    fo.r3_out()


if __name__ == "__main__":
    main()
