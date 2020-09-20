with open("menus.conf", "r", encoding="utf8") as File1:
    lines = File1.read().split('\n')

command = []
output_lines = []
command_index = 0
for i in range(len(lines)):
    if "commands=[" in lines[i]:
        command.append(lines[i + 1].strip())
print(len(command))
for i in range(len(lines)):
    if "&bOpens" in lines[i] and 'Shop"' in lines[i]:
        print(command_index)
        print(command[command_index])
        print(lines[i])
        output_lines.append(f"{lines[i]},")
        output_lines.append(f'"&dAlias: /{command[command_index]}"')
        command_index += 1
    elif "&bReturn to" in lines[i]:
        print(command_index)
        print(command[command_index])
        print(lines[i])
        output_lines.append(f"{lines[i]},")
        output_lines.append(f'"&dAlias: /{command[command_index]}"')
        command_index += 1
    elif "&bGo to" in lines[i]:
        print(command_index)
        print(command[command_index])
        print(lines[i])
        output_lines.append(f"{lines[i]},")
        output_lines.append(f'"&dAlias: /{command[command_index]}"')
        command_index += 1
    else:
        output_lines.append(lines[i])
with open("output.conf", "a", encoding="utf-8") as output:
    for line in output_lines:
        output.write(f'{line}\n')