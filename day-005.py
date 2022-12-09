test_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".split('\n')


def read_input():
    with open('./day-005.txt') as f:
        return [ line.strip('\n') for line in f.readlines() ]


# return a dict of stack_num -> crate_name, i.e. {1: None, 2: 'D', 3: None}
def parse_crates(line):

    line_chars = list(line)

    # return the crate name, e.g. 'D', if present, otherwise None
    def extract_crate(start_pos):
        crate = ''.join(line_chars[start_pos:start_pos+3]).strip().strip('[').strip(']')
        if len(crate) == 0:
            return None
        else:
            return crate



    grouped_chars = [ extract_crate(pos) for pos in range(0, len(line_chars), 4) ]
    return dict(enumerate(grouped_chars, start=1))


# crates is a dict in the form {1: None, 2: 'D', 3: None}
# stacks is a dict in the form {1: [], 2: ['D'], 3: []}
# stacks is modified, by appending the new crates to the lists for each stack
def add_new_crates(crates, stacks):
    for stack_number in list(crates):
        if (crates[stack_number] != None):
            if stack_number not in stacks:
                stacks[stack_number] = []
            stacks[stack_number].append(crates[stack_number])


# return a dict in the form: { 'move': #, 'from': #, 'to': # } where '#' represents numbers
def extract_instruction(inst_line):
    elements = [ elem.split('to') for elem in inst_line.replace('move', '').split('from') ]
    flattened = [ int(item.strip()) for sublist in elements for item in sublist ]
    return { 'move': flattened[0], 'from': flattened[1], 'to': flattened[2] }


# Returns a stacks dictionary and the line number of the first instruction in the input
def parse_input(input_lines):
    stacks = dict()
    line_idx = -1
    
    for line in input_lines:
        line_idx += 1
        if line[:2] == ' 1':
            break
        else:
            crates = parse_crates(line)
            add_new_crates(crates, stacks)
    
    instructions = [ extract_instruction(line) for line in input_lines[line_idx + 2:] ]
    
    for stack_number in list(stacks):
        stacks[stack_number].reverse()

    return (stacks, instructions)


def all_in_one_go(crates_to_move):
    crates_to_move.reverse()
    return crates_to_move


def one_at_a_time(crates_to_move):
    return crates_to_move


def simulate(stacks, instructions, stacking_style):

    for instruction in instructions:
        # print(instruction)
        # print(stacks)

        from_stack = stacks[instruction['from']]
        crates_to_move = []
        for x in range(0, instruction['move']):
            crates_to_move.append(from_stack.pop())
        to_stack = stacks[instruction['to']]
        crates_to_move = stacking_style(crates_to_move)
        to_stack.extend(crates_to_move)

        # print(stacks)
        # print('****')
    return None


def star(stacking_style):
    stacks, instructions = parse_input(read_input())
    simulate(stacks, instructions, stacking_style)
    tops = []
    for stack in sorted(list(stacks)):
        tops.append(stacks[stack][-1])
    return ''.join(tops)


def star_one():
    return star(stacking_style=one_at_a_time)


def star_two():
    return star(stacking_style=all_in_one_go)


print(star_one())
print(star_two())