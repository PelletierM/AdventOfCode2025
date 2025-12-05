import sys

def get_sorted_ranges():
    ranges = []
    with open(sys.argv[1], "r") as f:
        for line in f:
            if line == "\n":
                break
            nums = [int(i) for i in line.split("-")]
            ranges.append([nums[0], nums[1]])
    ranges = sorted(ranges, key=lambda range:range[0])
    return ranges

def merge_ranges(ranges):
    i = 0
    while i < len(ranges) - 1:
        if ranges[i][1] >= ranges[i + 1][0]:
            if ranges[i][1] < ranges[i + 1][1]:
                ranges[i][1] = ranges[i + 1][1]
            ranges.pop(i + 1)
        else:
            i += 1
    return
    
def count_all_possible_ids(ranges):
    count = 0
    for range in ranges:
        count += range[1] + 1 - range[0]
    return count 

def main():
    ranges = get_sorted_ranges()
    merge_ranges(ranges)
    print(count_all_possible_ids(ranges))

main()