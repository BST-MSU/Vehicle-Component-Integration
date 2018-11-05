from BST_Observer import *
from BST_Subject import *


class Driver:

    def __init__(self):
        self.observers:[BST_Observer] = None
        self.vehicle_network = None            # Network already built? Ask Kyle

    def test(self):

        n = NetworkSubject()
        print(type(n))
        u = USBSubject()
        print(type(u))
        g = GPIOSubject()
        print(type(g))

        n_o = NetworkObserver(self, n)
        print(type(n_o))
        u_o = USBObserver(self, u)
        print(type(u_o))
        g_o = GPIOObserver(self, g)
        print(type(g_o))

        n.test()
        u.test()
        g.test()


temp = Driver()
temp.test()
