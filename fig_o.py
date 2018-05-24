# -*- coding: utf-8 -*-

import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


class Data_read:
    def __init__(self, argvs=sys.argv[1]):
        self.argvs = argvs

    def reading(self):
        data = []
        t = []
        x = []
        y = []

        f = open("{}".format(self.argvs))
        lines = f.readlines()
        for l in lines:
            data = l.split()

            t.append(float(data[0]))
            x.append(float(data[1]))
            y.append(float(data[2]))

        f.close()
        return t, x, y


class Fig_output:
    def __init__(self, t, x, y):
        self.t = t
        self.x = x
        self.y = y

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
#       plt.xlim([0, max(self.x)])
#       plt.ylim([0, max(self.y)])
        plt.plot(self.x, self.y, linewidth=0.5)
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
    rd = Data_read(sys.argv[1])
    t, x, y = rd.reading()

    fo = Fig_output(t, x, y)
    fo.xy_t_put()
    fo.x_y_out()
    fo.r3_out()


if __name__ == "__main__":
    main()
