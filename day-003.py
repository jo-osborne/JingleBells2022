test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


def read_input():
    with open('./day-003.txt') as f:
        return f.read()


def parse_input(input):
    
    def split_compartments(rucksack):
        total_item_count = len(rucksack)
        half_idx = int(total_item_count / 2)
        return (rucksack[:half_idx], rucksack[half_idx:])

    compartments = [ split_compartments(rucksack) for rucksack in input.split('\n') ]

    return compartments


def find_single_common_element_in_lists(lists):
    sets = map(set, lists)
    duplicates = set.intersection(*sets)
    if len(duplicates) != 1:
        raise Exception(f'I expected only one common element but found {len(duplicates)} common elements in this data: {lists}')
    return duplicates.pop()    


def find_duplicated_item(rucksack):
    return find_single_common_element_in_lists(list(rucksack))


def item_priority(item):
    ascii = ord(item)
    if item.isupper():
        return ascii - 38
    else:
        return ascii - 96


def group_rucksacks(input):
    rucksacks = [ input[pos: pos + 3] for pos in range(0, len(input), 3) ]
    return [ [ ''.join(compartments) for compartments in group ] for group in rucksacks ]


rucksacks = parse_input(read_input())

def star_one():
    duplicated_items = [ find_duplicated_item(rucksack) for rucksack in rucksacks ]
    return sum([item_priority(item) for item in duplicated_items])


def star_two():
    grouped_rucksacks = group_rucksacks(rucksacks)
    duplicates = [ find_single_common_element_in_lists(group) for group in grouped_rucksacks]
    return sum([item_priority(item) for item in duplicates])


print(star_one())
print(star_two())

