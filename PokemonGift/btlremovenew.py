with open("pokegive.conf", "r", encoding="utf8") as File1:
    commands = File1.read().split('\n')
with open("btl.conf", "r", encoding="utf8") as File2:
    lines = File2.read().split('\n')
new_lines = []
remove_next = False
for i in range(len(lines)):
    if remove_next:
        remove_next = False
        pass
    elif lines[i].split(" ")[-1][:-1] not in commands:
        if '" {' not in lines[i]:
            new_lines.append(lines[i])
    else:
        new_lines.pop()
        new_lines.pop()
        i += 1
        remove_next = True
index = 0
linenum = 0
for line in new_lines:
    if line.strip().startswith("#"):
        print(line)
    elif linenum % 4 == 0:
        print(f'      "{index}" ' + "{")
        print(line)
        index += 1
        linenum += 1
    else:
        print(line)
        linenum += 1
