class Foo:
    def __init__(self, *args):
        self._args = args

    def args(self):
        return self._args
