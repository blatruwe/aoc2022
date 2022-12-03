f=open("day2/input.txt",'r')
#f=open("day2/input.short.txt")
score=0
for line in f:
    start=line.split()[0]
    response=line.split()[1]
    if (start=='A'): #rock
        if (response=="X"): #loose
            score=score+0
            score=score+3
        elif (response=='Y'): #draw
            score=score+3
            score=score+1
        elif (response=='Z'): #win
            score=score+6
            score=score+2
    elif (start=='B'): #paper
        if (response=="X"): #loose
            score=score+0
            score=score+1
        elif (response=='Y'): #draw
            score=score+3
            score=score+2
        elif (response=='Z'): #win
            score=score+6
            score=score+3
    elif (start=='C'): #scissors
        if (response=="X"): #loose
            score=score+0
            score=score+2
        elif (response=='Y'): #draw
            score=score+3
            score=score+3
        elif (response=='Z'): #win
            score=score+6
            score=score+1
 #   print(start,response)
    print(score)