test_input = """30373
25512
65332
33549
35390""".split()


def read_input():
    with open('./day-008.txt') as f:
        return [ line.strip('\n') for line in f.readlines() ]


def parse_into_grid(input):
    return [ [ int(char) for char in list(line) ] for line in input ]


def visible(grid, tree_height, range, grid_indexer_function):
    count = 0
    for i in range:
        if grid_indexer_function(grid, i) >= tree_height:
            return (False, count + 1)
        else:
            count += 1
    return (True, count)


def visible_up(grid, row_idx, col_idx):
    return visible(
        grid, 
        grid[row_idx][col_idx], 
        range(row_idx - 1, -1, -1), 
        lambda grid, i: grid[i][col_idx])


def visible_down(grid, row_idx, col_idx):
    return visible(
        grid,
        grid[row_idx][col_idx],
        range(row_idx + 1, len(grid)),
        lambda grid, i: grid[i][col_idx]
    )


def visible_left(grid, row_idx, col_idx):
    return visible(
        grid,
        grid[row_idx][col_idx],
        range(col_idx - 1, -1, -1),
        lambda grid, i: grid[row_idx][i]
    )


def visible_right(grid, row_idx, col_idx):
    return visible(
        grid,
        grid[row_idx][col_idx],
        range(col_idx + 1, len(grid[row_idx])),
        lambda grid, i: grid[row_idx][i]
    )


def count_visible_trees(grid):

    visible_edge_trees = (2 * (len(grid[0]) - 1)) + (2 * (len(grid) - 1))
    print(f'There are {visible_edge_trees} visible trees along the edges')

    visible_center_trees = 0

    for row_idx in range(1, len(grid) - 1):
        for col_idx in range(1, len(grid[row_idx]) - 1):

            visible = visible_up(grid, row_idx, col_idx)[0] or \
                    visible_down(grid, row_idx, col_idx)[0] or \
                    visible_left(grid, row_idx, col_idx)[0] or \
                    visible_right(grid, row_idx, col_idx)[0]
            
            if visible:
                visible_center_trees += 1
                #print(f'Tree at location [{row_idx}, {col_idx}] is {tree_height} units tall and IS visible')
            else:
                #print(f'Tree at location [{row_idx}, {col_idx}] is {tree_height} units tall and is NOT visible')
                pass

    return visible_center_trees + visible_edge_trees


def find_most_scenic_tree(grid):

    most_scenic_so_far = None

    for row_idx in range(1, len(grid) - 1):
        for col_idx in range(1, len(grid[row_idx]) - 1):
            
            scenic_score = visible_up(grid, row_idx, col_idx)[1] * \
                    visible_down(grid, row_idx, col_idx)[1] * \
                    visible_left(grid, row_idx, col_idx)[1] * \
                    visible_right(grid, row_idx, col_idx)[1]

            if (most_scenic_so_far == None) or (scenic_score > most_scenic_so_far):
                most_scenic_so_far = scenic_score

    return most_scenic_so_far


grid = parse_into_grid(read_input())

def star_one():
    return count_visible_trees(grid)

def star_two():
    return find_most_scenic_tree(grid)


print(star_one())
print(star_two())
