from copy import copy, deepcopy
monkeys=[]; items=[] ; operations=[] ; tests=[] ; if_false_list=[]; if_true_list=[]

def read_input():
    instr= open("day11/input").readlines()
    for i in range(0,len(instr),7):
        monkeys.append(int(instr[i].strip().split()[1].split(':')[0]))
        items.append([int(j.strip()) for j in instr[i+1].split(':')[1].split(',')])
        operations.append(instr[i+2].strip().split("=")[1].split()[1::])
        tests.append(int(instr[i+3].strip().split("by")[1].split()[0]))
        if_true_list.append(int(instr[i+4].strip().split("monkey")[1].split()[0]))
        if_false_list.append(int(instr[i+5].strip().split("monkey")[1].split()[0]))

def monkey_business(rounds,worry,items):
    count=([0]*len(monkeys))  
    for round in range(rounds):
        do_round(worry,items,count)
    print(sorted(count)[-1]*sorted(count)[-2]) 

def do_round(worry,items,count):
    for monkey in monkeys:
        count[monkey]=+count[monkey]+len(items[monkey])
        for item in items[monkey]:
            if operations[monkey][0]=="+":
                if operations[monkey][1]=="old":
                    item=int(item*2//worry)%magic_number
                else:
                    item=int((item+int(operations[monkey][1]))//worry)%magic_number
            elif operations[monkey][0]=="*":
                if operations[monkey][1]=="old":
                    item=int(item**2//worry)%magic_number
                else:
                    item=int(item*int(operations[monkey][1])//worry)%magic_number
            if item%tests[monkey]==0:
                items[if_true_list[monkey]].append(item)
            else:
                items[if_false_list[monkey]].append(item)
        items[monkey]=[]

read_input()
#optimalisation
magic_number=1
for i in tests:
    magic_number=magic_number*i
monkey_business(20,3,deepcopy(items))
monkey_business(10000,1,deepcopy(items))

