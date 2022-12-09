def test_input():
    return """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".splitlines()


def read_input():
    with open('./day-009.txt') as f:
        return f.read().splitlines()


def parse_input(input):
    def parse(line):
        sections = line.split()
        return (sections[0], int(sections[1]))
    return [ parse(line) for line in input ]


def simulate(instructions, rope_length):
    positions_visited = set()
    
    h_pos = (0, 0)
    t_pos = { i: (0, 0) for i in range(0, rope_length) }

    def move_up(pos): return (pos[0] + 1, pos[1])
    def move_down(pos): return (pos[0] - 1, pos[1])
    def move_left(pos): return (pos[0], pos[1] - 1)
    def move_right(pos): return (pos[0], pos[1] + 1)


    def move_closer(h_pos, t_pos):
        # H and T are in same spot, no need to move
        if h_pos == t_pos: 
            return t_pos
        # H and T are adjacent, no need to move
        if abs(h_pos[0] - t_pos[0]) < 2 and abs(h_pos[1] - t_pos[1]) < 2: 
            return t_pos

        # Move T right if it is to the left of H
        if h_pos[1] > t_pos[1]:
            t_pos = move_right(t_pos)
        # Alternatively, move T left if it is to the right of H
        elif h_pos[1] < t_pos[1]:
            t_pos = move_left(t_pos)

        # Move T up if it is below H
        if h_pos[0] > t_pos[0]:
            t_pos = move_up(t_pos)
        # Alternatively, move T down if it is above H
        elif h_pos[0] < t_pos[0]:
            t_pos = move_down(t_pos)

        return t_pos

    for (dir, dist) in instructions:
        
        for step in range(0, dist):

            # print(f'H starts at {h_pos} and will be moved {dir} {dist}')

            # update pos of H according to inst
            if dir == 'R':
                h_pos = move_right(h_pos)

            elif dir == 'L':
                h_pos = move_left(h_pos)

            elif dir == 'U':
                h_pos = move_up(h_pos)

            elif dir == 'D':
                h_pos = move_down(h_pos)

            else:
                raise(Exception(f'strange instruction: {dir} {dist}'))

            for i in t_pos.keys():
                if i == 0:
                    t_pos[i] = move_closer(h_pos, t_pos[i])
                else:
                    t_pos[i] = move_closer(t_pos[i-1], t_pos[i])

            # print(f'H is now at {h_pos}')
            # print(f'T is now at {t_pos}')
            positions_visited.add(t_pos[rope_length - 1])


    return positions_visited



def star(rope_length):
    instructions = parse_input(read_input())
    visited = simulate(instructions, rope_length)
    return len(visited)


def star_one(): return star(rope_length=1)
def star_two(): return star(rope_length=9)

print(star_one())
print(star_two())
