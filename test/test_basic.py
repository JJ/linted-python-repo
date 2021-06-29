from unittest import TestCase
from foo import Foo

BAR = "bar"


class BasicTest(TestCase):
    def test_different_args(self):
        print(Foo(BAR))
        assert(Foo(BAR).args() == (BAR,))
