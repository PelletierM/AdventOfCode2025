import sys

def get_problems():
    map = []
    with open(sys.argv[1], "r") as f:
        for line in f:
            map.append(line.rstrip("\n"))
    problems = []
    curr_problem = []
    for i in range(len(map[0])):
        if i != len(map[0]) - 1 and map[len(map) - 1][i + 1] != " ":
            problems.append(curr_problem)
            curr_problem = []
            continue
        if len(curr_problem) == 0:
            curr_problem.append(map[len(map) - 1][i])
        num = []
        for j in range(len(map) - 1):
            num.append(map[j][i])
        curr_problem.append(int("".join(num)))
    problems.append(curr_problem)
    return problems

def solve_problems(problems):
    count = 0
    for problem in problems:
        subcount = problem[1]
        for i in range(2, len(problem)):
            if problem[0] == "*":
                subcount *= problem[i]
            else:
                subcount += problem[i]
        count += subcount
    return count
                
def main():
    problems = get_problems()
    print(solve_problems(problems))
    
main()