DIR = "d"
FILE = "f"


def lines():
    for line in open("input.txt"):
        res = line.strip()
        yield res


class FileSystem:
    def __init__(self, name, parent, ftype, size=0):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = dict()
        self.type = ftype


class Dir(FileSystem):
    def __init__(self, name, parent):
        super().__init__(name, parent, DIR, 0)


class File(FileSystem):
    def __init__(self, name, parent, size):
        super().__init__(name, parent, FILE, size)


class Command:
    def __init__(self, current):
        self.current = current

    def cd(self, name):
        self.current = self.current.parent if name == ".." else self.current.children[name]

    def add_file(self, name, size):
        self.current.children[name] = File(name, self.current, size)

    def add_dir(self, name):
        self.current.children[name] = Dir(name, self.current)

    def compute_sizes(self, from_file: FileSystem):
        if not from_file.size:
            from_file.size = sum(self.compute_sizes(f) for f in from_file.children.values())
        return from_file.size

    def crawl(self, from_file: FileSystem):
        yield from_file
        for child in from_file.children.values():
            for cchild in self.crawl(child):
                yield cchild


def populate(cli):
    all_commands = lines()
    next(all_commands)
    for line in all_commands:
        match line.split():
            case ["$", "cd", name]:
                cli.cd(name)
            case ["$", "ls"]:
                pass
            case ["dir", name]:
                cli.add_dir(name)
            case [size, name]:
                cli.add_file(name, int(size))


def solve1(cli, root):
    return sum(file.size for file in cli.crawl(root) if file.size < 100000 and file.type == DIR)


def solve2(cli, root):
    free_space = 70000000 - root.size
    min_size = 30000000 - free_space
    return min([file.size for file in cli.crawl(root) if file.size > min_size and file.type == DIR])


if __name__ == "__main__":
    root = Dir("/", None)
    cli = Command(root)
    populate(cli)
    cli.compute_sizes(root)
    print(solve1(cli, root))
    print(solve2(cli, root))
