
test_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".split('\n')


class Dir:

    def __init__(self, name, parent = None):
        self.name = name
        self.subdirs = set()
        self.files = set()
        self.parent = parent
    
    def add_subdir(self, dir):
        self.subdirs.add(dir)

    def get_subdir(self, dir_name):
        return [ d for d in self.subdirs if d.name == dir_name][0]
    
    def add_file(self, file):
        self.files.add(file)

    def get_size(self):
        dirs = sum([ d.get_size() for d in self.subdirs ])
        files = sum([ f.size for f in self.files ])
        return dirs + files

    def __str__(self) -> str:
        if self.parent != None:
            return f'{self.name} with parent {self.parent.name}'
        else:
            return f'{self.name} (ROOT)'

    def pretty_print(self, level=0):
        indentation = '\t' * level
        desc = f'{indentation}- {self.name} (dir)'
        sorted_contents = sorted(list(self.subdirs) + list(self.files), key=lambda x: x.name)
        contents = '\n'.join([ item.pretty_print(level + 1) for item in sorted_contents ])
        return f'{desc}\n{contents}'

    def fullname(self):
        dir = self
        path = [self.name]
        while dir.parent != None:
            path.append(dir.parent.name)
            dir = dir.parent
        path.reverse()
        return '/'.join(path)

    def get_dir_sizes(self, sizes):
        if self.name in sizes:
            dir_name = f'{self.fullname()}'
        else:
            dir_name = self.name

        sizes[dir_name] = self.get_size()
        for sd in self.subdirs:
            sd.get_dir_sizes(sizes)

class File:

    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

    def pretty_print(self, level):
        indentation = '\t' * level
        return f'{indentation}- {self.name} (file, size={self.size})'


def read_input():
    with open('./day-007.txt') as f:
        return [ line.strip('\n') for line in f.readlines()]


# returns the root directory of the file structure
def generate_file_structure(input):

    curr_dir = None

    for line in input:
        if line[:4] == '$ cd':
            dir_name = line.split()[-1]

            if dir_name == '..':
                curr_dir = curr_dir.parent

            else:

                print(f'{line}: changing directory to {dir_name}')
                
                if curr_dir == None:
                    curr_dir = Dir(dir_name)
                else:
                    dir = curr_dir.get_subdir(dir_name)
                    curr_dir = dir

            print(f'Current directory is {curr_dir}')



        elif line[:4] == '$ ls':
            print(f'{line} listing contents for {curr_dir.name}')
            pass

        else:
            if line[:3] == 'dir':
                sdir = Dir(line.split()[-1], curr_dir)
                print(f'Adding subdir {sdir.name} to {curr_dir.name}')
                curr_dir.add_subdir(sdir)
            else:
                # this is a file
                file_listing = line.split()
                file = File(file_listing[1], file_listing[0])
                curr_dir.add_file(file)

    root_dir = curr_dir
    while root_dir.parent != None:
        print(root_dir)
        root_dir = root_dir.parent

    return root_dir



root_dir = generate_file_structure(read_input())

# optional - print the file structure
print('****')
print(root_dir.pretty_print())
print('****')

# -------------------------

def get_all_dir_sizes():
    dir_sizes = dict()
    root_dir.get_dir_sizes(dir_sizes)
    return dir_sizes


def star_one(): 
    dir_size_threshold = 100000
    dir_sizes = get_all_dir_sizes()
    return sum([ d for d in dir_sizes.values() if d <= dir_size_threshold ])


def star_two():
    dir_sizes = get_all_dir_sizes()

    total_space = 70000000
    req_unused_space = 30000000

    used_space = root_dir.get_size()
    unused = total_space - used_space
    more_req = req_unused_space - unused

    deletable_dirs = [ d for d in dir_sizes.values() if d >= more_req ]
    return min(deletable_dirs)


print(star_one())
print(star_two())