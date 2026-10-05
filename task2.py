import random

n=random.randint(1,100)
a=0
s=100

while True:
    try:
        g=int(input("Guess the number: "))
        a+=1
        if g==n:
            print("Correct!")
            print("Attempts:",a)
            print("Score:",max(0,s-(a-1)*10))
            break
        elif g<n:
            print("Too low")
        else:
            print("Too high")
    except ValueError:
        print("Enter a number")

f=input("Enter file name: ")

try:
    with open(f,"r") as x:
        t=x.read().lower()
        w=t.split()
        d={}
        for i in w:
            i=i.strip(".,!?;:'\"()[]{}")
            if i:
                d[i]=d.get(i,0)+1

    print("Total words:",len(w))
    print("Word frequency:")
    for i,j in d.items():
        print(i,j)
except FileNotFoundError:
    print("File not found")
