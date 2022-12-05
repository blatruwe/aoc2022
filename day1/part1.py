f = open("day1/input_part1", "r")

elf_list=[]
sum=0
for line in f : 
    if(not line.strip()):
        elf_list.append(sum)
        sum=0
    else:
        sum=sum+int(line.strip())
elf_list.append(sum)

print( max(elf_list))


#part 2

s=sorted(elf_list)
total=s[-1]+s[-2]+s[-3]
print(total)