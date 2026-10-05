import csv

f="expenses.csv"

try:
    open(f,"r").close()
except FileNotFoundError:
    with open(f,"w",newline="") as x:
        w=csv.writer(x)
        w.writerow(["date","category","amount","note"])

while True:
    print("\n1.Add\n2.View\n3.Filter\n4.Summary\n5.Exit")
    ch=input("Choose: ")

    if ch=="1":
        d=input("Date: ")
        c=input("Category: ")
        a=input("Amount: ")
        n=input("Note: ")

        try:
            float(a)
            with open(f,"a",newline="") as x:
                csv.writer(x).writerow([d,c,a,n])
            print("Expense added")
        except ValueError:
            print("Invalid amount")

    elif ch=="2":
        with open(f,"r") as x:
            for r in csv.DictReader(x):
                print(r["date"],r["category"],r["amount"],r["note"])

    elif ch=="3":
        c=input("Category: ")
        with open(f,"r") as x:
            for r in csv.DictReader(x):
                if r["category"].lower()==c.lower():
                    print(r["date"],r["amount"],r["note"])

    elif ch=="4":
        d={}
        with open(f,"r") as x:
            for r in csv.DictReader(x):
                c=r["category"]
                d[c]=d.get(c,0)+float(r["amount"])

        for c,a in d.items():
            print(c,a)

    elif ch=="5":
        break

    else:
        print("Invalid choice")
