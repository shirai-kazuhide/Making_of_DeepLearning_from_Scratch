class Man:
    #初期化メソッド = コンストラクタ
    def __init__(self,name):
        self.name = name
        print("Initialized")

    def hello(self):
        print("Hello" + self.name)

    def goodbye(self):
        print("Goodbye" + self.name)


m = Man("David")
m.goodbye()