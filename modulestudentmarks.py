def printinfo(name,age,mathsmark,sciencemark,socialmark,englishmark,tamilmark,total,avg,per):
  print("name : ",name)
  print("age : ",age)
  print("mathsmark : ",mathsmark)
  print("sciencemark : ",sciencemark)
  print("socialmark : ",socialmark)
  print("englishmark : ",englishmark)
  print("tamilmark : ",tamilmark)
  print("total mark : ",total)
  print("the avg mark is",avg)
  print("the per mark is",per)
  return;
name=input("enter ur  name:")
age=int(input("enter ur age : "))
mathsmark=int(input("enter ur mathsmark:"))
sciencemark=int(input("enter ur sciencemark:"))
socialmark=int(input("enter ur socialmark:"))
englishmark=int(input("enter ur englishmark:")) 
tamilmark=int(input("enter ur tamilmark:"))
total=int(mathsmark)+int(sciencemark)+int(socialmark)+int(englishmark)+int(tamilmark)
avg=(total/5)*100
per=((total/500)*100)
printinfo(name=name,age=age,mathsmark=mathsmark,sciencemark=sciencemark,socialmark=socialmark,englishmark=englishmark,tamilmark=tamilmark,total=total,avg=avg,per=per)

