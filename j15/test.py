from j15.solve import remove_all_intersections, join_sorted_segments


def test_intersection():
    res = remove_all_intersections([(0, 10), (2, 8)])
    assert res == [(0, 10)]

    res = remove_all_intersections([(0, 10), (2, 12)])
    assert res == [(0, 10), (10, 12)]

    res = remove_all_intersections([(0, 10), (2, 12), (-1, 10)])
    assert res == [(-1, 10), (10, 12)]

    res = remove_all_intersections([(0, 10), (12, 20)])
    assert res == [(0, 10), (12, 20)]

    res = remove_all_intersections([(0, 10), (12, 20), (10, 20)])
    assert res == [(0, 10), (10, 20)]

    res = remove_all_intersections([(0, 10), (20, 25), (8, 21)])
    assert res == [(0, 10), (10, 21), (21, 25)]



def test_join():
    res = join_sorted_segments( [(0, 10), (10, 21), (21, 25)])
    assert res == [(0, 25)]

    res = join_sorted_segments( [(0, 10), (11, 21), (21, 25)])
    assert res == [(0, 10), (11, 25)]
