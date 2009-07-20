class List:    
    def __init__(self, data):
        self.myList = data

    def toString(self):
        print self.myList

class WindowList(List):
    def __init__(self, data, hasHead = False, hasTail = False):
        List.__init__(self, data)
        self.hasHead = hasHead
        self.hasTail = hasTail
    
    def toString(self):
        List.toString(self)
        print self.hasHead, self.hasTail

def main():
    mine = List([0,1])
    mine.toString()
    yours = WindowList([0,1,1], True)
    yours.toString()

if __name__ == "__main__":
    main()


