groups = []
while True:
    a = input()
    if a == "yeet":
        break
    else:
        groups.append(a)
for i in range(len(groups)):
    # print(f'/lp group {group} clone locked_{group}')
    # print(f'/lp group locked_vip_{group} permission set vip_{group}.rankup false')
    # print(f'/lp group locked_{group} permission set {group}.rankup false')
    # print(f'/lp track locked append locked_{group}')
    # print(f'/lp track locked append locked_vip_{group}')
    if i:
        print(f'/lp group locked_vip_{groups[i]} parent set locked_vip_{groups[i-1]}')