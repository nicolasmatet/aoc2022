import pytest

from j3.solve import Bag


class TestBag():
    def test_item_value(self):
        a = Bag.get_item_value('a')
        z = Bag.get_item_value('z')
        A = Bag.get_item_value('A')
        Z = Bag.get_item_value('Z')
        assert a == 1
        assert z == 26
        assert A == 27
        assert Z == 52
