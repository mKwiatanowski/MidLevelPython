
instruction = ['day hello', 'say how are you', 'abort', 'ask for money','say thank you', 'say bye']
instructionApproved = []

for instr in instruction:
    print("Adding instruction: ", instr)
    instructionApproved.append(instr)

    if instr == 'abort':
        print('Aborting!!!')
        instructionApproved.clear()
        break

# jeśli został wcześniej użyty break to polecenie else się nie wykona
# instrukcja else wykonuje się tylko wtedy gdy nie została przerwana przez instrukcje break
else:
    print("Following actions will be taken: ", instructionApproved)


print('-'*30)
instructionApproved.clear()

i = 0
while i < len(instruction):
    print("Adding instruction: ", instruction[i])
    instructionApproved.append(instruction[i])

    if instruction[i] == 'abort':
        print('Aborting!!!')
        instructionApproved.clear()
        break

    i += 1

# jeśli został wcześniej użyty break to polecenie else się nie wykona
else:
    print("Following actions will be taken: ", instructionApproved)












