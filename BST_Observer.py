from BST_Subject import *
class BST_Observer:

    def __init__(self, parent, subject : BST_Subject):
        self.subject = subject
        self.parent = parent

    def update(self, data):
        print("Default Observer: " + str(data))


class NetworkObserver(BST_Observer):

    def __init__(self, parent, subject):
        super().__init__(parent, subject)
        subject.attach(self) if type(subject) == NetworkSubject else ""

    def update(self, data):
        print("Network Data: " + str(data))


class USBObserver(BST_Observer):

    def __init__(self, parent, subject):
        super().__init__(parent, subject)
        subject.attach(self) if type(subject) == USBSubject else ""

    def update(self, data):
        print("USB Data: " + str(data))


class GPIOObserver(BST_Observer):

    def __init__(self, parent, subject):
        super().__init__(parent, subject)
        subject.attach(self) if type(subject) == GPIOSubject else ""

    def update(self, data):
        print("GPIO Data: " + str(data))