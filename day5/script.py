f=open("day5/input")
instruction_input=False
input=[]
stack_input=[]
for line in f:
    if not line.strip():
        instruction_input=True
    else:
        if (instruction_input):
            input.append((line.split()[1],line.split()[3],line.split()[5]))
        else:
            stack_input.append(line)

nbr_of_stacks=len(stack_input[-1].split())
stack=[]

for i in range(nbr_of_stacks):
    stackbuilder=""
    for line in reversed(stack_input):
        if('[' in line):
            if not (line[i*4+1]==' '):
                stackbuilder=stackbuilder+line[i*4+1]
            else:
                break
    stack.append(stackbuilder)

part1_stack=stack.copy()
part2_stack=stack.copy()
    
def part1(instruction):
    for i in range(int(instruction[0])):
        to_move=part1_stack[int(instruction[1])-1][-1]
        part1_stack[int(instruction[1])-1]=part1_stack[int(instruction[1])-1][:-1]
        part1_stack[int(instruction[2])-1]=part1_stack[int(instruction[2])-1]+to_move

    
def part2(instruction):
    to_move=part2_stack[int(instruction[1])-1][int(instruction[0])*-1:]
    part2_stack[int(instruction[1])-1]=part2_stack[int(instruction[1])-1][:int(instruction[0])*-1]
    part2_stack[int(instruction[2])-1]=part2_stack[int(instruction[2])-1]+to_move
    

for i in input:
    part1(i)

solution=""
for i in part1_stack:
    solution=solution+i[-1]
print(solution)

for i in input:
    part2(i)

solution=""
for i in part2_stack:
    solution=solution+i[-1]
print(solution)