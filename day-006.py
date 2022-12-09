test_input_1 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb' # 7, 19
test_input_2 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'   # 5, 23
test_input_3 = 'nppdvjthqldpwncqszvftbrmjlhg'   # 6, 23
test_input_4 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg' # 10, 29
test_input_5 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'  # 11, 29


def read_input():
    with open('./day-006.txt') as f:
        return f.read()


def find_start(data_stream, distinct_count):
    idx = 0

    for _ in data_stream:
        idx += 1
        last_x = data_stream[idx-distinct_count:idx]
        if len(set(last_x)) == distinct_count:
            return idx

    raise(Exception(f'reached end of string without finding start of packet'))


def find_start_of_packet(data_stream): 
    return find_start(data_stream, distinct_count=4)


def find_start_of_message(data_stream):
    return find_start(data_stream, distinct_count=14)


print(find_start_of_packet(read_input()))
print(find_start_of_message(read_input()))