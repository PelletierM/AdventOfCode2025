import sys

def get_ranges(filename):
    with open(filename, "r") as f:
        ranges = []
        strings = f.readline().split(",")
        for string in strings:
            elem = string.split("-")
            ranges.append(range(int(elem[0]), int(elem[1]) + 1))
        return ranges

def count_invalid_ids(rang):
    count = 0
    for i in rang:
        string = str(i)
        string_len = len(string)
        if string_len % 2 == 0 and string[0:string_len//2] == string[string_len//2:]:
            count += i
    return count

def main():
    ranges = get_ranges(sys.argv[1])
    count = 0
    for i in ranges:
        count += count_invalid_ids(i)
    print(count)

main()