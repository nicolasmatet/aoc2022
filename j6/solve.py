

def lines():
    for line in open("input.txt"):
        res = line.strip()
        yield res


class Buffer:
    def __init__(self, max_len=4):
        self._buffer = []
        self.max_len = max_len

    def clean_duplicate(self, last_value):
        for idx, value in enumerate(reversed(self._buffer[:-1])):
            if value == last_value:
                self._buffer = self._buffer[-idx-1:]
                break

    def advance(self, new_char):
        self._buffer.append(new_char)
        self.clean_duplicate(new_char)
        return len(self._buffer) == self.max_len


def first_n(line, max_len):
    buffer = Buffer(max_len=max_len)
    for idx, new_char in enumerate(line):
        stop = buffer.advance(new_char)
        if stop:
            return idx + 1


def solve1():
    line = iter(next(lines()))
    return first_n(line, max_len=4)


def solve2():
    line = iter(next(lines()))
    return first_n(line, max_len=14)


if __name__ == "__main__":
    print(solve1())
    print(solve2())
