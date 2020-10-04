with open("gift.conf", "r", encoding="utf8") as File1:
    lines = File1.read().split('\n')
output_lines = []
index = 0
for line in lines:
    if line == "    }":
        index = 0
        output_lines.append(line)
    elif line.strip().startswith('"') and line.strip().endswith('{'):
        output_lines.append(f'      "{index}"' + " {")
        index += 1
    else:
        output_lines.append(line)
with open("output.conf", 'a', encoding='utf-8') as output:
    for line in output_lines:
        output.write(f'{line}\n')