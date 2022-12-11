f=open("day10/input")
instr=[]
for line in f:
    instr.append(line.strip())
cycle=1
X=1
instr_index=0
wait=False
result=dict()
result[1]=1
while instr_index<len(instr):
    cycle=cycle + 1
    if wait==False:
        if not instr[instr_index]=='noop':
            wait=True
        instr_index=instr_index+1
    elif wait==True:
        X=X+int(instr[instr_index-1].split()[1])
        wait=False
    result[cycle]=X
    
#part1
sum=0
for i in (20,60,100,140,180,220):
    sum+=result[i]*i
print(sum)
#part2
for cycle in range(1,241):
    if result[cycle]-1<=(cycle-1)%40 and result[cycle]+1>=(cycle-1)%40:
        print('#', end = '')
    else:
        print('.', end = '')
    if cycle%40==0:
        print()