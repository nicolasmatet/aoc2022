from j13.solve import comparison


def test_order1():
    left, right = [[1], [2, 3, 4]], [[1], 4]
    assert comparison(left, right) < 0

def test_order2():
    left, right = [], [3]
    assert comparison(left, right) < 0

def test_order3():
    left, right = [[[]]], [[]]
    assert comparison(left, right) > 0
