f=open("day8/input")
forest=[]
for line in f:
    row=list(line.strip())
    forest.append(row)

#part1
def check_visible(y,x):
    visible=True
    for i in range(0,x):
        if(forest[y][i]>=forest[y][x]):
            visible=False
    if visible:
        return True
    visible=True
    for i in range(x+1,len(forest[0])):
        if(forest[y][i]>=forest[y][x]): 
            visible=False
    if visible:
        return True
    visible=True    
    for i in range(0,y):
        if(forest[i][x]>=forest[y][x]):
            visible=False
    if visible:
        return True
    visible=True
    for i in range(y+1,len(forest)):
        if(forest[i][x]>=forest[y][x]):
            visible=False
    return visible
        
sum =  0
for j in range(1,len(forest)-1):
    for i in range(1,len(forest[0])-1):
        if not (check_visible(j,i)):
            sum=sum+1
total=len(forest[0])*len(forest)
print(total-sum)

#part2
def check_scenic_score(y,x):
    score=1
    for i in reversed(range(1,x)):
        if(forest[y][i]<forest[y][x]):
            score=score+1
        else:
            break
    total_score=score
    score=1
    for i in range(x+1,len(forest[0])-1):
        if(forest[y][i]<forest[y][x]): 
            score=score+1
        else:
            break
    total_score=total_score*score
    score=1
    for i in reversed(range(1,y)):
        if(forest[i][x]<forest[y][x]):
            score=score+1
        else:
            break
    total_score=total_score*score
    score=1
    for i in range(y+1,len(forest)-1):
        if(forest[i][x]<forest[y][x]):
            score=score+1
        else:
            break
    total_score=total_score*score
    return total_score

max=0
for j in range(1,len(forest)-1):
    for i in range(1,len(forest[0])-1):
        score=check_scenic_score(i,j)
        if (score>max):
            max=score
print(max)
