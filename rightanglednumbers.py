a = int(input("Enter the Total Number : "))
for i in range(0,a):
    for j in range(0,a-1-i):
     print("",end = '  ')
    for z in range(0,2*i+1):
     print(str(j)+"",end="")
