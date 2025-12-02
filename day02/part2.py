import sys

def get_ranges(filename):
    with open(filename, "r") as f:
        ranges = []
        strings = f.readline().split(",")
        for string in strings:
            elem = string.split("-")
            ranges.append(range(int(elem[0]), int(elem[1]) + 1))
        return ranges
    
def check_invalid_recur(string, split_size):
    if split_size < 1:
        return False
    if len(string) % split_size == 0:
        elems = [string[i:i+split_size] for i in range(0, len(string), split_size)]
        if all(elem == elems[0] for elem in elems):
            return True
    return check_invalid_recur(string, split_size - 1)

def check_invalid(string):
    return check_invalid_recur(string, len(string) // 2)

def count_invalid_ids(rang):
    count = 0
    for i in rang:
        if check_invalid(str(i)):
            count += i
    return count

def main():
    ranges = get_ranges(sys.argv[1])
    count = 0
    for i in ranges:
        count += count_invalid_ids(i)
    print(count)

main()