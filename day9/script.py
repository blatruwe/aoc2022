f=open("day9/input")
instr=[]
for line in f:
    instr.append((line.split()[0],int(line.split()[1].strip())))

def moveknot(dir,l):
    if l==0:
        if dir=='R':
            rope[0]=(rope[0][0]+1,rope[0][1])
        elif dir=='U':
            rope[0]=(rope[0][0],rope[0][1]+1)
        elif dir=='D':
            rope[0]=(rope[0][0],rope[0][1]-1)
        elif dir=='L':
            rope[0]=(rope[0][0]-1,rope[0][1])
    else:
        dx=rope[l-1][0]-rope[l][0]
        dy=rope[l-1][1]-rope[l][1]
        if abs(dx)==2 and dy==0:
            rope[l]=(rope[l][0]+dx//abs(dx),rope[l][1])
        elif dx==0 and abs(dy)==2 :
            rope[l]=(rope[l][0],rope[l][1]+dy//abs(dy))
        elif(abs(dx)==2 and abs(dy)>=1) or (abs(dx)>=1 and abs(dy)==2) :
            rope[l]=(rope[l][0]+dx//abs(dx),rope[l][1]+dy//abs(dy))


for rope_size in (2,10):
    tailpositions=[(0,0)]
    rope=[]
    for i in range(rope_size):
        rope.append((0,0))
    for dir,pos in instr:
        for i in range(pos):
            for l in range(0,len(rope)):
                moveknot(dir,l)
            if rope[-1] not in tailpositions:
                tailpositions.append(rope[-1])
    print(len(tailpositions))