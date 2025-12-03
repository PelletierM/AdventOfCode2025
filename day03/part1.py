import sys

def get_lines():
    with open(sys.argv[1], "r") as f:
        return [line.strip() for line in f]

def count_line(line):
    num = list("00")
    index = None
    for i in range(len(line) - 1):
        if line[i] > num[0]:
            num[0] = line[i]
            index = i
    for i in range(index + 1, len(line)):
        if line[i] > num[1]:
            num[1] = line[i]
    return int("".join(num))

def main():
    count = 0
    lines = get_lines()
    for line in lines:
        count += count_line(line)
    print(count)

main()