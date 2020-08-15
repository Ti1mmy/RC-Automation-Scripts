import pyperclip
index = 0
inputs = []
while True:
    a = input()
    if a:
        inputs.append(a.split("COMMAND:")[1])
    else:
        break
lis = ""
for give in inputs:
    lis += (f'        Gift{index}' + ' {\n')
    lis += (f'            "0" ' + "{\n")
    lis += f'                reward="COMMAND:{give}\n'
    lis += '            }\n'
    lis += '        }\n'
    index += 1
pyperclip.copy(lis)
print(lis)