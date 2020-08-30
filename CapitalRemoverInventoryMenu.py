with open("menusPortingShop.conf", "r", encoding="utf8") as File1:
    file_contents = File1.read().split('\n')
newlist = []
for line in file_contents:
    if 'cooldown=' in line:
        newlist.append(line.lower())
    else:
        newlist.append(line)
with open("output.conf", "a", encoding="utf-8") as output:
    for line in newlist:
        output.write(f'{line}\n')
