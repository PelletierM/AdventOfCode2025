import sys

def get_lines():
    with open(sys.argv[1], "r") as f:
        return [line.strip() for line in f]

def count_line(line, size):
    num = ['0'] * size
    index = 0
    for i in range(size):
        for j in range(index, (len(line) - (size - i - 1))):
            if line[j] > num[i]:
                num[i] = line[j]
                index = j + 1
    return int("".join(num))

def main():
    count = 0
    lines = get_lines()
    for line in lines:
        count += count_line(line, 12)
    print(count)

main()