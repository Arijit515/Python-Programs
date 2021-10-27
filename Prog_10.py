name = input ("Enter Name:")
basic = float(input("Enter Basic Monthly Salary:"))
da = 0
hra = 0
incomeTax = 0
if basic>=10000:
    da=basic*40/100
    hra=basic*30/100
elif basic>=5000 and basic<10000:
    da=basic*40/100
    hra=basic*25/100
elif basic>=2000 and basic<5000:
    da=basic*30/100
    hra=basic*20/100
elif basic<2000:
    da=basic*30/100
    hra=basic*15/100
salary=basic+da+hra
if salary>50000:
    it=(salary-50000)*30/100
    netsal=salary-it
print("Name is ",name)
print("Basic pay ",basic)
print("DA ",da)
print("HRA ",hra)
print("Income tax monthly",it)
print("Net Monthly salary",netsal)