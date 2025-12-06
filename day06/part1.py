import sys
import re

def get_problems():
    problems = []
    with open(sys.argv[1], "r") as f:
        for line in f:
            problems.append(re.split(r" +", line.strip()))
    return problems

def solve_problems(problems):
    count = 0
    for i in range(len(problems[0])):
        subcount = int(problems[0][i])
        for j in range(1, len(problems) - 1):
            if problems[len(problems) - 1][i] == '*':
                subcount = subcount * int(problems[j][i])
            else:
                subcount = subcount + int(problems[j][i])
        count += subcount
    return count
                
def main():
    problems = get_problems()
    print(solve_problems(problems))

main()