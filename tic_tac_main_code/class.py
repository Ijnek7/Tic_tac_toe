class Example(object):
    def __init__(self):
        self.x = 3
        self.y = 4
        self.__privatevar = 32
    def __aprivate(self):
        self.x = self.x*30
        self.y = self.y*40
    def returnxy(self):
        print(self.x,self.y)
        self.__aprivate()
        print(self.x,self.y)

a = Example()
# a.returnxy()
print(a.x)