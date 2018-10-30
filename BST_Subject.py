import threading
import random as rand

from BST_Observer import *

class BST_Subject:

    def __init__(self):
        self.observers = []
        self.data = "default"

    def attach(self, new_observer):
        self.observers.append(new_observer)

    def detach(self):
        self.observers.pop()

    def detach_at(self, pos):
        self.observers.pop(pos)

    def notify(self):
        for obs in self.observers:
            obs.update(self.get_data())

    def test(self):
        t = threading.Thread(target=self.test_thread_func)
        t.start()

    def test_thread_func(self):
        while self.data != 1:
            self.data = rand.randint(1,1000)
            self.notify()

    def get_data(self):
        return self.data


class NetworkSubject(BST_Subject):

    def __init__(self):
        super().__init__()

    # Network specific get_data() call
    def get_data(self):
        return self.data


class USBSubject(BST_Subject):

    def __init__(self):
        super().__init__()

    # USB specific get_data() call
    def get_data(self):
        return self.data


class GPIOSubject(BST_Subject):

    def __init__(self):
        super().__init__()

    # GPIO specific get_data() code
    def get_data(self):
        return self.data