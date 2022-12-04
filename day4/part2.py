
sum=0
f=open("day4/input")
for line in f:
    assignment1_list=list(range(int(line.split(',')[0].split('-')[0]),int(line.split(',')[0].split('-')[1])+1))
    assignment2_list=list(range(int(line.strip().split(',')[1].split('-')[0]),int(line.strip().split(',')[1].split('-')[1])+1))
    overlap=False
    for i in assignment1_list:
        if i in assignment2_list:
            overlap=True
            break
        if(overlap):
            break
    if (overlap):         
        sum=sum+1
             


print(sum)