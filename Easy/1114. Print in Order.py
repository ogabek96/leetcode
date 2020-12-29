class Foo:
    def __init__(self):
        self.cnt = 1
    def first(self, printFirst: 'Callable[[], None]') -> None:
            # printFirst() outputs "first". Do not change or remove this line.
            printFirst()
            self.cnt = 2


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.cnt != 2:
            pass
        printSecond()
        self.cnt = 3


    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.cnt != 3:
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()