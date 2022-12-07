
import time
start_time = time.time()

f=open("day7/input")
directory={}
dir_listing=False
pwd=[]
dir_content=[]
for line in f:
    if "$" in line and dir_listing:
        dir_listing=False
        directory[''.join([str(elem) for elem in pwd])]=dir_content
    if "$ cd" in line:
        input=line.strip().split()[-1]
        if input=="..":
            pwd.pop()
            pwd.pop()
        else:
            if not input=='/':
                pwd.append(input)            
            pwd.append('/')
        continue
    elif "$ ls" in line:
        dir_listing=True
        dir_content=[]
        continue
    elif dir_listing:
        if line.split()[0] == "dir":
            dir_content.append(( (''.join([str(elem) for elem in pwd]) + line.split()[1].strip()+'/',0)))
        else:
            dir_content.append(((line.split()[1].strip()),int(line.split()[0].strip())))
if dir_listing:
    directory[''.join([str(elem) for elem in pwd])]=dir_content

def calculate_dir_size(dir):
    total_size=0
    for content,size in directory[dir]:
        if size:
            total_size=total_size+size
        else:
            total_size=total_size+calculate_dir_size(content)
    return total_size

#part1
sum=0
for dir in directory:
    if calculate_dir_size(dir)<=100000:
        sum=sum+calculate_dir_size(dir)
print(sum)

#part2
candidate_to_delete=[]
to_free_up=30000000-70000000+calculate_dir_size('/')
for dir in directory:
    if (calculate_dir_size(dir)>=to_free_up):
        candidate_to_delete.append(calculate_dir_size(dir))
print(min(candidate_to_delete))


print("--- %s seconds ---" % (time.time() - start_time))