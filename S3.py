import sys
from collections import deque
input = sys.stdin.readline
info = []
branch = deque([])
min = 1
trials = int(input())
answers = deque([])

while trials > 0:
    for i in range(int(input())):
        info.append(int(input()))
    while info or len(branch) > 0:
        if info and info[-1] == min:
            info.pop()
            min += 1
        elif branch and branch[0] == min:
            branch.popleft()
            min += 1
        elif info:
            branch.appendleft(info[-1])
            info.pop()
        else:
            break
    if not branch:
        answers.append('Y')
    else:
        answers.append('N')
    trials -= 1
    min = 1
    info = []
    branch = deque([])
for i in range(len(answers)):
    print(answers[i])