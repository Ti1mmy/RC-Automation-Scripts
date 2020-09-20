with open("gift.conf", "r", encoding="utf8") as File1:
    lines = File1.read().split('\n')
total = 0
for line in lines:
    if "chance=" in line:
        total += (int(line.split("=")[1]))
print(total)