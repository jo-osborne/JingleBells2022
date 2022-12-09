test_input="""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def read_input():
    with open('./day-004.txt') as f:
        return f.read()



def parse_input(input):
    pairs = input.split('\n')
    
    for pair in pairs:
        elves = pair.split(',')
        def to_range(range_desc):
            start = int(range_desc.split('-')[0])
            end = int(range_desc.split('-')[1])
            return range(start, end + 1)
        yield (to_range(elves[0]), to_range(elves[1]))


def ranges_overlap(range1, range2):
    srange1 = set(range1)
    srange2 = set(range2)
    return srange1.issubset(srange2) or srange2.issubset(srange1)


def ranges_intersect(range1, range2):
    srange1 = set(range1)
    srange2 = set(range2)
    return len(srange1.intersection(srange2)) > 0


elves = list(parse_input(read_input()))

def star_one():
    overlapping = [ ranges_overlap(r1, r2) for (r1, r2) in elves ]
    return sum(overlapping)

def star_two():
    overlapping = [ ranges_intersect(r1, r2) for (r1, r2) in elves ]
    return sum(overlapping)


print(star_one())
print(star_two())


