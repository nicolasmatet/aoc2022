import re
from collections import defaultdict

move_regex = re.compile("move ([0-9]+) from ([0-9]+) to ([0-9]+)")


def lines():
    for line in open("input.txt"):
        match = re.match(move_regex, line)
        if match:
            n_crates, from_stack, to_stack = map(int, match.groups())
            yield n_crates, from_stack - 1, to_stack - 1


def get_stacks():
    stacks_dict = defaultdict(list)
    for line in open("input.txt"):
        if not line.strip():
            break
        crates = [line[n + 1].strip() for n in range(0, len(line), 4)]
        for n_stack, crate in enumerate(crates):
            if crate:
                stacks_dict[n_stack].append(crate.strip())
    return [list(reversed(stacks_dict[n_stack])) for n_stack in sorted(stacks_dict.keys())]


def solve1():
    all_stacks = get_stacks()
    for n_crates, from_stack, to_stack in lines():
        all_stacks[to_stack].extend(reversed(all_stacks[from_stack][-n_crates:]))
        all_stacks[from_stack] = all_stacks[from_stack][:-n_crates]
    return "".join(stack[-1] for stack in all_stacks)


def solve2():
    all_stacks = get_stacks()
    for n_crates, from_stack, to_stack in lines():
        all_stacks[to_stack].extend(all_stacks[from_stack][-n_crates:])
        all_stacks[from_stack] = all_stacks[from_stack][:-n_crates]
    return "".join(stack[-1] for stack in all_stacks)


if __name__ == "__main__":
    print(solve1())
    print(solve2())
