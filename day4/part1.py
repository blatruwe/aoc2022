
sum=0
f=open("day4/input")
for line in f:
    assignment1_list=list(range(int(line.split(',')[0].split('-')[0]),int(line.split(',')[0].split('-')[1])+1))
    assignment2_list=list(range(int(line.strip().split(',')[1].split('-')[0]),int(line.strip().split(',')[1].split('-')[1])+1))
    all_in_list=True
    for i in assignment1_list:
        if not i in assignment2_list:
             all_in_list=False
    if all_in_list:
        sum=sum+1
        continue
    all_in_list=True
    for i in assignment2_list:
        if not i in assignment1_list:
             all_in_list=False
    if all_in_list:
        sum=sum+1
print(sum)