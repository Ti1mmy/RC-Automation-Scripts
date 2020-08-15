with open("genball.conf", "r", encoding="utf8") as File1:
    file_contents = File1.read().split(sep="\n")
pokelist = []
for line in file_contents:
    if "reward=" in line and "relicvase" not in line:
        pokelist.append(line.split(sep=" ")[-1][:-1])
while True:
    a = input()
    if a == "yeet":
        break
    else:
        pokelist.append(a)
pokelist.sort()
newlist = []
newlist.append('trivia {')
for thing in pokelist:
    newlist.append('    questions {')
    newlist.append("        " + thing + " {")
    newlist.append(f'            answers=["{thing}"]')
    newlist.append(f'            question="&e&oType the word to win a prize: &6&l{thing}"')
    newlist.append('        }')
    newlist.append('	}')
for thing in pokelist:
    newlist.append('    scrambles {')
    newlist.append("        " + thing + " {")
    newlist.append(f'            #Left blank for random scramble')
    newlist.append(f'            word="{thing}"')
    newlist.append('        }')
    newlist.append('	}')
newlist.append("}")
with open("genballoutput.conf", "a", encoding="utf8") as output:
    for line in newlist:
        output.write(f'{line}\n')