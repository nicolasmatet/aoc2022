def lines():
    for line in open("input.txt"):
        res = line.strip().split()
        yield res


def get_instuctions():
    instructions = lines()
    for instruction in instructions:
        match instruction:
            case ["noop"]:
                yield NoopInstruction()
            case ["addx", value]:
                yield AddInstruction(int(value))


class Instruction:
    def __init__(self, duration):
        self.duration = duration

    def pass_cycle(self):
        self.duration -= 1

    def execute(self, register):
        pass

    def ended(self):
        return self.duration == 0


class NoopInstruction(Instruction):
    def __init__(self):
        super().__init__(1)

    def execute(self, register):
        pass


class AddInstruction(Instruction):
    def __init__(self, value):
        super().__init__(2)
        self.value = value

    def execute(self, register):
        register.value += self.value


class Register:
    def __init__(self):
        self.value = 1


class Program:
    def __init__(self, first_instruction):
        self.register = Register()
        self.instruction = first_instruction
        self.cycle = 1

    def next_instruction(self, instructions):
        try:
            return next(instructions)
        except StopIteration:
            return None

    def ended(self):
        return self.instruction is None

    def advance_one_cycle(self, instructions):
        self.instruction.pass_cycle()
        if self.instruction.ended():
            self.instruction.execute(self.register)
            self.instruction = self.next_instruction(instructions)
        self.cycle += 1

    def get_pixel(self):
        if abs((self.cycle - 1) % 40 - self.register.value) < 2:
            return "#"
        return " "


def solve1():
    total = 0
    instructions = get_instuctions()
    program = Program(next(instructions))
    while not program.ended():
        program.advance_one_cycle(instructions)
        if (program.cycle - 20) % 40 == 0:
            total += program.cycle * program.register.value
    return total


def print_image(image):
    for i in range(len(image) // 40):
        print("".join(image[i * 40 : (i + 1) * 40 - 1]))


def solve2():
    image = []
    instructions = get_instuctions()
    program = Program(next(instructions))
    while not program.ended():
        image.append(program.get_pixel())
        program.advance_one_cycle(instructions)
    return image


if __name__ == "__main__":
    print(solve1())
    print_image(solve2())
