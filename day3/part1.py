f=open("day3/input")  
priority=0
for line in f:
    size=len(line.strip())
    helft=int(size/2)
    part1=line.strip()[0:helft]
    part2=line.strip()[helft::]
    common=set(part1).intersection(part2)
    common_letter=str(common.pop())
    if common_letter.isupper():
        priority=priority+ord(common_letter)-64+26
    else:
        priority=priority+ord(common_letter)-96

print(priority)