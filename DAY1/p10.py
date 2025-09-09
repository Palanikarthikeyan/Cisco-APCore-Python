Emp = ["101,raj,sales,pune,1000",
       "102,leo,prod,bglore,2000",
       "103,paul,HR,bglore,3000",
       "104,shiv,QA,mumbai,4000",
       "105,shan,HR,hyd,5000"]

total=0
for var in Emp:
    eid,ename,edept,ecity,ecost = var.split(",")
    print(f'{ename.title()} Working City is:{ecity.upper()}')
    total = total + int(ecost)
else:
    print('-'*30)
    print(f"Sum of Emp's Cost:{total}")
    print('-'*30)

