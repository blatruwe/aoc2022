
sum=0
f=open("day4/input")
for line in f:
    if list(set(list(range(int(line.split(',')[0].split('-')[0]),int(line.split(',')[0].split('-')[1])+1)))&set(list(range(int(line.strip().split(',')[1].split('-')[0]),int(line.strip().split(',')[1].split('-')[1])+1)))):
        sum=sum+1
print(sum)