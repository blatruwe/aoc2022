f=open("day3/input")  
priority=0
i=0
elf1=""
elf2=""
elf3=""
priority=0
for line in f:
    i=i+1
    if(i==1):
        elf1=line.strip()
    if(i==2):
        elf2=line.strip()
    if(i==3):
        elf3=line.strip()
        common = set.intersection(*map(set,(elf1,elf2,elf3)))
        common_letter=str(common.pop())
        if common_letter.isupper():
            priority=priority+ord(common_letter)-64+26
        else:
            priority=priority+ord(common_letter)-96
        print(common_letter)
        i=0
print(priority)



