shape_mapping = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C',
}
win_mapping = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}
lose_mapping = {v: k for k, v in win_mapping.items()}
shape_score_mapping = {
    'A': 1,
    'B': 2,
    'C': 3,
}
LOSE = 'X'
DRAW = 'Y'
WINS = 'Z'
outcome_score_mapping = {
    LOSE: 0,
    DRAW: 3,
    WINS: 6,
}


def lines():
    for line in open("input.txt"):
        res = line.strip().split()
        yield res[0], res[1]


def get_outcome(other, mine):
    if mine in win_mapping[other]:
        return LOSE
    if other in win_mapping[mine]:
        return WINS
    return DRAW


def get_shape(other, outcome):
    if outcome == LOSE:
        return win_mapping[other]
    if outcome == WINS:
        return lose_mapping[other]
    return other


def solve1():
    total_score = 0
    for other, mine in lines():
        mine = shape_mapping[mine]
        outcome = get_outcome(other, mine)
        outcome_score = outcome_score_mapping[outcome]
        shape_score = shape_score_mapping[mine]
        total_score += outcome_score + shape_score
    return total_score


def solve2():
    total_score = 0
    for other, outcome in lines():
        mine = get_shape(other, outcome)
        outcome_score = outcome_score_mapping[outcome]
        shape_score = shape_score_mapping[mine]
        total_score += outcome_score + shape_score
    return total_score


if __name__ == '__main__':
    print(solve1())
    print(solve2())
