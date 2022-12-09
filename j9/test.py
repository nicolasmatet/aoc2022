import numpy as np

from j9.solve import Rope


class Test:

    def test_up(self):
        rope = Rope()
        rope.move('U')
        assert np.all(rope.head == np.array([-1, 0]))
        assert np.all(rope.tail == np.array([0, 0]))
        rope.move('U')
        assert np.all(rope.head == np.array([-2, 0]))
        assert np.all(rope.tail == np.array([-1, 0]))
        rope.move('D')
        assert np.all(rope.head == np.array([-1, 0]))
        assert np.all(rope.tail == np.array([-1, 0]))

    def test_right(self):
        rope = Rope()
        rope.move('R')
        assert np.all(rope.head == np.array([0, 1]))
        assert np.all(rope.tail == np.array([0, 0]))
        rope.move('R')
        assert np.all(rope.head == np.array([0, 2]))
        assert np.all(rope.tail == np.array([0, 1]))
        rope.move('L')
        assert np.all(rope.head == np.array([0, 1]))
        assert np.all(rope.tail == np.array([0, 1]))

    def test_diag_down_right(self):
        rope = Rope()
        rope.head = np.array([0, 1])
        rope.tail = np.array([0, 0])
        rope.move('D')
        assert np.all(rope.head == np.array([1, 1]))
        assert np.all(rope.tail == np.array([0, 0]))
        rope.move('D')
        assert np.all(rope.head == np.array([2, 1]))
        assert np.all(rope.tail == np.array([1, 1]))

    def test_diag_down_left(self):
        rope = Rope()
        rope.head = np.array([0, -1])
        rope.tail = np.array([0, 0])
        rope.move('D')
        assert np.all(rope.head == np.array([1, -1]))
        assert np.all(rope.tail == np.array([0, 0]))
        rope.move('D')
        assert np.all(rope.head == np.array([2, -1]))
        assert np.all(rope.tail == np.array([1, -1]))

    def test_diag_up_left(self):
        rope = Rope()
        rope.head = np.array([0, -1])
        rope.tail = np.array([0, 0])
        rope.move('U')
        assert np.all(rope.head == np.array([-1, -1]))
        assert np.all(rope.tail == np.array([0, 0]))
        rope.move('U')
        assert np.all(rope.head == np.array([-2, -1]))
        assert np.all(rope.tail == np.array([-1, -1]))

    def test_diag_up_right(self):
        rope = Rope()
        rope.head = np.array([0, 1])
        rope.tail = np.array([0, 0])
        rope.move('U')
        assert np.all(rope.head == np.array([-1, 1]))
        assert np.all(rope.tail == np.array([0, 0]))
        rope.move('U')
        assert np.all(rope.head == np.array([-2, 1]))
        assert np.all(rope.tail == np.array([-1, 1]))
