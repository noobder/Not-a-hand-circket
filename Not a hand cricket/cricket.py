import random
import os
def run():
    return random.randint(0,6)


def oddoreven(a,b):
    if (a+b)%2==0:
        return "even"
    else:
        return "odd"
def pmatch(choice):
    scorep=0
    scorec=0
    if choice=="batting":
        while True:
            print("player batting")
            pla=int(input("player: "))
            if pla not in range(0,7) :
                print("must be a number between 0 and 6")
                continue
                
            com=run()
            print("computer: ",com)
           
            if com!=pla:
                scorep+=pla
                print("score: ",scorep)
                continue
            elif com==pla:
                print("player out")
                print(f"player score is : {scorep}")
                print("computer")
                pla=0
                com=0
                choice="bowling"
                while True:
                    
                    print("player bowling")
                    pla=int(input("runs: "))
                    if pla not in range(0,7):
                        print("must be a number between 0 and 6")
                        continue
                
                    com=run()
                    print("computer: ",com)
                    
                    if com!=pla:
                        scorec+=com
                        print("score: ",scorec)
                        
                        
                    if com==pla and scorep>scorec:
                        print(f"player win by {scorep-scorec} runs")
                        break 
                        
                    if scorep<scorec:
                        print(f"computer win by {scorec-scorep} runs" )
                        break 
                            
                    if com==pla and scorep==scorec:
                             print("draw match")
                             break 
            break
    elif choice=="bowling":
        while True:
            print("player bowling")
            pla=int(input("player: "))
            if pla not in range(0,7):
                print("must be a number between 0 and 6")
                continue
                
            com=run()
            print("computer: ",com)
            
            if com!=pla:
                scorec+=pla
                print("score: ",scorec)
                continue
            elif com==pla:
                print("computer out")
                print(f"computer score is : {scorep}")
                print("player")
                com=0
                pla=0
                choice="batting"
                while True:
                    print("player batting")
                    pla=int(input("runs: "))
                    if pla not in range(0,7) :
                        print("must be a number between 0 and 6")
                        continue
                
                    com=run()
                    print("computer: ",com)
                    
                    if com!=pla:
                        scorep+=pla
                        print("score: ",scorec)
                        
                    if com==pla and scorep<scorec:
                        print(f"computer win by {scorec-scorep} runs")
                        break 
                        
                    if scorep>scorec:
                        print(f"player win by {scorep-scorec} runs" )
                        break 
                            
                    if com==pla and scorep==scorec:
                             print("draw match")
                             break 
            break
def cmatch(choice):
    scorep=0
    scorec=0
    if choice=="batting":
        while True:
            print("player bowling")
            pla=int(input("player: "))
            if pla not in range(0,7):
                print("must be a number between 0 and 6")
                continue
                
            com=run()
            print("computer: ",com)
            
            if com!=pla:
                scorec+=com
                print("score: ",scorec)
                continue
            elif com==pla:
                print("computer out")
                print(f"computer score is : {scorec}")
                print("computer")
                pla=0
                com=0
                choice="bowling"
                while True:
                    print("player batting")
                    pla=int(input("player: "))
                    if pla not in range(0,7) :
                        print("must be a number between 0 and 6")
                        continue
                    com=run()
                    print("computer: ",com)
                   
                    if com!=pla:
                        scorep+=pla
                        print("score: ",scorep)

                    if com==pla and scorep<scorec:
                        print(f"computer win by {scorec-scorep} runs")
                        break 
                        
                    if scorep>scorec:
                        print(f"player win by {scorep-scorec} runs" )
                        break 
                            
                    if com==pla and scorep==scorec:
                             print("draw match")
                             break 
            break
    elif choice=="bowling":
        while True:
            print("player batting")
            pla=int(input("player: "))
            if pla not in range(0,7) :
                print("must be a number between 0 and 6")
                continue
            com=run()
            print("computer: ",com)
            
            if com!=pla:
                scorep+=pla
                print("score: ",scorep)
                continue
            elif com==pla:
                print("player out")
                print(f"player score is : {scorep}")
                com=0
                pla=0
                choice="batting"
                while True:                    
                    print("player bowling")
                    pla=int(input("player: "))
                    
                    if pla not in range(0,7):
                            print("must be a number between 0 and 6")
                            continue

                    com=run()
                    print("computer: ",com)
                    
                    if com!=pla:
                        scorec+=com
                        print("score: ",scorec)
                        
                    if com!=pla:
                        scorep+=pla
                        print("score: ",scorec)
                    if com==pla and scorep<scorec:
                        print(f"computer win by {scorec-scorep} runs")
                        break 
                        
                    if scorep>scorec:
                        print(f"player win by {scorep-scorec} runs" )
                        break 
                            
                    if com==pla and scorep==scorec:
                             print("draw match")
                             break 
            break


def match():
    print("odd or even")
    l=["batting","bowling"]
    t=input()
    nump=int(input("num between 0 and 6 : "))
    numc=random.randint(0,6)
    print(numc)
    v=oddoreven(nump,numc)
    if (v=="odd" and t=="odd") or (v=="even" and t=="even") :
        print(f"its {t} player wins")
        choice=input("batting or bowling :")
        pmatch(choice)
        
    else:
        print("computer wins")
        choice=l[random.randint(0,1)]
        print(f"choose to {choice}")
        cmatch(choice)
        
def check(sp,sc):
    if sp>sc:
        print("player wins")
    
    
match()