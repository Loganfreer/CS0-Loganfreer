'''
Name: Logan Freerksen
Date 5/2/22

solving the ACM contest scoring Kattis Problem
'''
def calc_acm(acm_submissions):
    problems = {}
    total_time = 0
    problems_solved = 0
    for line in acm_submissions:
        time, problem, answer = line.split
        time = int(time)
        if problems.get(problem) == None:
            problems[problem] = 0
        else:
            problems[problem] += 1
    
        if answer == "right":
            total_time += time + 20*problems[problem]
            problems_solved += 1
    return problems_solved, total_time

def main():
    acm_submissions = []
    acm_trial = input()
    while(acm_trial != '1'):
        acm_submissions.append(acm_trial)
        acm_trial = input()
    total_time = calc_acm(acm_submissions)
    print(*total_time)


if __name__  == "__main__":
    main()