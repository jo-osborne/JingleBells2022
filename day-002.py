from enum import Enum


test_input = """A Y
B X
C Z"""


def read_input():
    with open('./day-002.txt') as f:
        return f.read()


class Shape:
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Result:
    WIN = 6
    DRAW = 3
    LOSE = 0


def match_shape(shape):
    if shape == 'A' or shape == 'X':
        return Shape.ROCK
    if shape == 'B' or shape == 'Y':
        return Shape.PAPER
    if shape == 'C' or shape == 'Z':
        return Shape.SCISSORS

    raise(Exception(f'unknown shape: {shape}'))


def match_result(result):
    if result == 'X': return Result.LOSE
    if result == 'Y': return Result.DRAW
    if result == 'Z': return Result.WIN
    raise(Exception(f'unknown result: {result}'))


def parse_input(input, match_second_item):
    for line in input.split('\n'):
        shapes =  line.split(' ')
        opponent_shape = match_shape(shapes[0].strip())
        my_shape = match_second_item(shapes[1].strip())
        yield(opponent_shape, my_shape)


def simulate_round(opp_shape, my_shape):
    # this was a draw
    if opp_shape == my_shape:
        return Result.DRAW

    # I win
    if (opp_shape == Shape.ROCK and my_shape == Shape.PAPER) \
            or (opp_shape == Shape.PAPER and my_shape == Shape.SCISSORS) \
            or (opp_shape == Shape.SCISSORS and my_shape == Shape.ROCK):
        return Result.WIN

    # I lose
    if (opp_shape == Shape.ROCK and my_shape == Shape.SCISSORS) \
            or (opp_shape == Shape.PAPER and my_shape == Shape.ROCK) \
            or (opp_shape == Shape.SCISSORS and my_shape == Shape.PAPER):
        return Result.LOSE

    raise(Exception(f'Could not process game. Opponent shape: {opp_shape}, my shape: {my_shape}'))


def calculate_my_shape(opp_shape, result):
    # result should be a draw
    if result == Result.DRAW:
        return opp_shape
    
    # result should be a win:
    if result == Result.WIN:
        if opp_shape == Shape.ROCK: return Shape.PAPER
        if opp_shape == Shape.PAPER: return Shape.SCISSORS
        if opp_shape == Shape.SCISSORS: return Shape.ROCK

    # result should be a loss:
    if result == Result.LOSE:
        if opp_shape == Shape.ROCK: return Shape.SCISSORS
        if opp_shape == Shape.PAPER: return Shape.ROCK
        if opp_shape == Shape.SCISSORS: return Shape.PAPER

    raise(Exception(f'Could not calculate my shape. Opponent shape: {opp_shape}, result: {result}'))


def score_round(result, my_shape):
    return result + my_shape


def star_one():
    rounds = parse_input(read_input(), match_shape)
    scores = [ score_round(simulate_round(opp, me), me) for (opp, me) in rounds ]
    return sum(scores)


def star_two():
    rounds = parse_input(read_input(), match_result)
    scores = [ score_round(res, calculate_my_shape(opp, res)) for (opp, res) in rounds ]
    return sum(scores)


print(star_one())
print(star_two())
