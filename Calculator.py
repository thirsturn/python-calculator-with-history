print("Select operation.")
print("1.Add      : +")
print("2.Subtract : -")
print("3.Multiply : *")
print("4.Divide   : /")
print("5.Power    : ^")
print("6.Remainder: %")
print("7.Terminate: #")
print("8.Reset    : $")
print("8.History  : ?")
choice=input("Enter choice(+,-,*,/,^,%,#,$,?): ")
print(choice)
if (choice!="?")&(choice!="#"):
    x=choice

history=[] #history list

#start of defining functions

def add(N1,N2):
    h=[]
    p=N1+N2
    print(N1,"+",N2,"=",p)
    h.append(N1)
    h.append(N2)
    h.append(p)
    h.append(x)
    history.append(h)

def sub(N1,N2):
    h=[]
    p=N1-N2
    print(N1,"-",N2,"=",p)
    h.append(N1)
    h.append(N2)
    h.append(p)
    h.append(x)
    history.append(h)

def mul(N1,N2):
    h=[]
    p=N1*N2
    print(N1,"*",N2,"=",p)
    h.append(N1)
    h.append(N2)
    h.append(p)
    h.append(x)
    history.append(h)

def div(N1,N2):
    
    if N2==0:
        h=[]
        print("float division by zero")
        print(N1,"/",N2,"=","None")
        h.append(N1)
        h.append(N2)
        h.append("None")
        h.append(x)
        history.append(h)
    else:
        h=[]
        p=N1/N2
        print(N1,"/",N2,"=",p)
        h.append(N1)
        h.append(N2)
        h.append(p)
        h.append(x)
        history.append(h)

def powe(N1,N2):
    h=[]
    p=N1**N2
    print(N1,"^",N2,"=",p)
    h.append(N1)
    h.append(N2)
    h.append(p)
    h.append(x)
    history.append(h)

def remainder(N1,N2):
    h=[]
    p=N1%N2
    print(N1,"%",N2,"=",p)
    h.append(N1)
    h.append(N2)
    h.append(p)
    h.append(x)
    history.append(h)
def hist():
    if history==[]:
        print('No past calculations to show')
    else:
        for q in range(len(history)):
            print(history[q][0],history[q][3],history[q][1],"=",history[q][2])
#ending of defining functions
while choice!="#":
    if choice=="?":
        hist()
        print("Select operation.")
        print("1.Add      : +")
        print("2.Subtract : -")
        print("3.Multiply : *")
        print("4.Divide   : /")
        print("5.Power    : ^")
        print("6.Remainder: %")
        print("7.Terminate: #")
        print("8.Reset    : $")
        print("8.History  : ?")
        choice=input("Enter choice(+,-,*,/,^,%,#,$,?): ")
        print(choice)
        if (choice!="?")&(choice!="#"):
            x=choice
        elif choice=="#":
            break
    try:
        n1=input("Enter first number: ")
        print(n1)
        if n1=="#":
            break
        N1=float(n1)
        try:
            n2=input("Enter second number: ")
            print(n2)
            if n2=="#":
                break
            N2=float(n2)
            if choice=="+":
                add(N1,N2)          #add is a function
            elif choice=="-":
                sub(N1,N2)          #sub is a function to subtraction
            elif choice=="*":
                mul(N1,N2)          #mul is a function to multiply
            elif choice=="^":
                powe(N1,N2)         #powe is a function to find power
            elif choice=="/":
                div(N1,N2)          #div is use to divition 
            elif choice=="%":
                remainder(N1,N2)    #remainder is a function for doing remainder operator
            elif choice=="$":
                continue
            print("Select operation.")
            print("1.Add      : +")
            print("2.Subtract : -")
            print("3.Multiply : *")
            print("4.Divide   : /")
            print("5.Power    : ^")
            print("6.Remainder: %")
            print("7.Terminate: #")
            print("8.Reset    : $")
            print("8.History  : ?")
            choice=input("Enter choice(+,-,*,/,^,%,#,$,?): ")
            print(choice)
            if (choice!="?")&(choice!="#"):
                x=choice
            elif choice=="#":
                break

        except:
            print("Select operation.")
            print("1.Add      : +")
            print("2.Subtract : -")
            print("3.Multiply : *")
            print("4.Divide   : /")
            print("5.Power    : ^")
            print("6.Remainder: %")
            print("7.Terminate: #")
            print("8.Reset    : $")
            print("8.History  : ?")
            choice=input("Enter choice(+,-,*,/,^,%,#,$,?): ")
            print(choice)
            if (choice!="?")&(choice!="#"):
                x=choice
            elif choice=="#":
                break

    except :
        print("Select operation.")
        print("1.Add      : +")
        print("2.Subtract : -")
        print("3.Multiply : *")
        print("4.Divide   : /")
        print("5.Power    : ^")
        print("6.Remainder: %")
        print("7.Terminate: #")
        print("8.Reset    : $")
        print("8.History  : ?")
        choice=input("Enter choice(+,-,*,/,^,%,#,$,?): ")
        print(choice)
        if (choice!="?")&(choice!="#"):
            x=choice
        elif choice=="#":
                break


print("Done. Terminating")
