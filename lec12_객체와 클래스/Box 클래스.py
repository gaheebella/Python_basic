class Box:
    def __init__(self, l, h, d):
        self.__l = l
        self.__h = h
        self.__d = d

    def getLength(self):
        return self.__l

    def setLength(self, l):
        self.__l = l

    def getHeight(self):
        return self.__h

    def setHeight(self, h):
        self.__h = h

    def getDepth(self):
        return self.__d

    def setDepth(self, d):
        self.__d = d

    def __str__(self):
        msg = "(" + str(self.getLength()) + ", " + str(self.getHeight()) +", "+ str(self.getDepth()) + ")"
        return msg

b1 = Box(100, 100, 100)
print(b1)
print("상자의 부피: ", b1.getLength() * b1.getHeight() * b1.getDepth())