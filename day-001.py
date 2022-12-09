test_input="""1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def load_input():
    with open('./day-001.txt') as file:
        return file.read()


def parse_input(input):
    lines = input.split('\n')
    
    elves = []
    elves.append([])
    elf_count=0

    for line in lines:
        if len(line) == 0:
            # this is a line break between this elf and the next
            elf_count += 1
            elves.append([])
        else:
            elves[elf_count].append(int(line))

    return elves[:-1]


def count_elf_calories(elf):
    return sum(elf)


def elves_calorie_counts(test=False):
    if test:
        input = test_input
    else:
        input = load_input()
    
    elves = parse_input(input)

    
    return [ count_elf_calories(elf) for elf in elves ]



def star_one():
    calorie_counts = elves_calorie_counts()
    max_calories = max(calorie_counts)
    return max_calories



def star_two():
    calorie_counts = sorted(elves_calorie_counts())
    highest_three = calorie_counts[-3:]
    return sum(highest_three)



print(f'Star one: {star_one()}')
print(f'Star two: {star_two()}')
