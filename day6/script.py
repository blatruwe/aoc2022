f=open("day6/input")

def check_unique(str):
    for i in range(len(str)):
        for j in range(i + 1,len(str)):
            if(str[i] == str[j]):
                return False
    return True

def check_start(stream,length):
    for i in range(len(stream)):
        if(check_unique(stream[i:i+length])):
            return i+length

for line in f:
    print(check_start(line,4)) #part 1
    print(check_start(line,14)) #part 2