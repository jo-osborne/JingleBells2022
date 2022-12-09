test_input = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""".splitlines()

test_2 = """noop
addx 3
addx -5""".splitlines()

def read_input():
    with open('./day-010.txt') as f:
        return f.read().splitlines()

def process(input):
    register_history = [1]

    input_idx = 0
    cycle_count = 0
    next_add_val = 0
    skip = False

    while input_idx < len(input):
        cycle_count += 1
        next_reg = register_history[-1]

        if skip == True: 
            skip = False
        else:
            next_reg += next_add_val
            # print(input[input_idx])
            if input[input_idx][:4] == 'noop':
                # do nothing this cycle
                next_add_val = 0
                pass
            else:
                next_add_val = int(input[input_idx].split()[-1])
                skip = True
            input_idx += 1
            
        # print(f'Cycle: {cycle_count}, reg={register_history}')
        register_history.append(next_reg)

    return register_history


def draw_crt(register_history):
    
    crt = [ [ '_' for _ in range(0, 40) ] for _ in range(0, 6) ]
    
    def print_crt(crt):
        lines = [ ''.join(line) for line in crt ]
        for line in lines: print(line)

    print_crt(crt)

    def pos(cycle):
        return (int((cycle) / 40)), ((cycle) % 40)

    cycle = 1

    for register_value in register_history[1:]:
        print(f'Cycle: {cycle}, register value: {register_value}')
        sprite_pos_1 = pos(register_value - 1)
        sprite_pos_2 = pos(register_value)
        sprite_pos_3 = pos(register_value + 1)

        crt_pos = pos(cycle - 1)

        if crt_pos[1] == sprite_pos_1[1] or crt_pos[1] == sprite_pos_2[1] or crt_pos[1] == sprite_pos_3[1]:
            crt[crt_pos[0]][crt_pos[1]] = '#'
        else:
            crt[crt_pos[0]][crt_pos[1]] = '.'

        print(f'Cycle: {cycle}')
        print_crt(crt)

        cycle += 1




def star_one():
    register_history = process(test_input)
    
    critical_cycles = [20, 60, 100, 140, 180, 220]
    signal_strength = 0
    
    for cycle in critical_cycles:
        signal_strength += (register_history[cycle] * cycle)
        
    return signal_strength

print(star_one())

register_history = process(read_input())
draw_crt(register_history)
# print(register_history)