a = []
while True:
    b = input()
    if not b:
        break
    elif b not in a:
        a.append(b)
while True:
    b = input()
    if not b:
        break
    elif b.split(" ")[1] not in a:
        a.append(b.split(" ")[1])
a.sort()
for c in a:
    print(f'- {c}')