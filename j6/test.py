from j6.solve import first_n


class TestBuffer:
    def test4(self):
        assert first_n(iter("nppdvjthqldpwncqszvftbrmjlhg"), max_len=4) == 6
        assert first_n(iter("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"), max_len=4) == 10
        assert first_n(iter("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"), max_len=4) == 11
        assert first_n(iter("mjqjpqmgbljsphdztnvjfqwrcgsmlb"), max_len=4) == 7
        assert first_n(iter("bvwbjplbgvbhsrlpgdmjqwftvncz"), max_len=4) == 5
